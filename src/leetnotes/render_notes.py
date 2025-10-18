"""Markdown renderers for study note documents."""

from __future__ import annotations

import os
from datetime import datetime
from html import escape as html_escape
from pathlib import Path
from typing import Any
from urllib.parse import quote

from . import config, normalize
from .models import MetadataMap, NotesProfile
from .repo import folder_name_from_title

def _relative_solution_url(from_dir: Path, solution_path: Path) -> str:
    """Return a percent-encoded relative path from from_dir to solution_path."""

    rel = Path(os.path.relpath(solution_path, start=from_dir))
    encoded = "/".join(quote(part) for part in rel.parts)
    if not encoded.startswith((".", "/")):
        encoded = f"./{encoded}"
    return encoded


def _bullet_style_for_level(level: int) -> dict[str, str]:
    """Return rendering metadata for a given unordered note depth."""

    styles = getattr(config, "NOTE_BULLET_LEVEL_STYLES", ())
    if not styles:
        return {}
    index = min(level, len(styles) - 1)
    return dict(styles[index])


def _apply_marker(text: str, marker: str | None) -> str:
    """Prefix a note line with a custom marker when provided."""

    if not marker:
        return text
    marker_html = html_escape(marker)
    return f"{marker_html}&nbsp;{text}" if text else marker_html

def _build_note_tree(entries: list[normalize.NoteEntry]) -> list[dict[str, Any]]:
    """Convert flat note entries into a parent/child hierarchy."""

    root: dict[str, Any] = {"level": -1, "text": "", "ordered": False, "children": []}
    stack: list[dict[str, Any]] = [root]

    for entry in entries:
        level = entry.level
        while stack and level <= stack[-1]["level"]:
            stack.pop()
        parent = stack[-1]
        node: dict[str, Any] = {
            "level": level,
            "text": entry.text,
            "ordered": entry.ordered,
            "children": [],
        }
        parent["children"].append(node)
        stack.append(node)

    return root["children"]


def _render_note_nodes(nodes: list[dict[str, Any]], base_indent: int) -> list[str]:
    """Render note nodes as Markdown/HTML lines anchored at base_indent."""

    lines: list[str] = []
    idx = 0
    while idx < len(nodes):
        ordered = bool(nodes[idx]["ordered"])
        group: list[dict[str, Any]] = []
        while idx < len(nodes) and bool(nodes[idx]["ordered"]) == ordered:
            group.append(nodes[idx])
            idx += 1
        if not group:
            continue
        current_level = min(node["level"] for node in group)
        if ordered:
            lines.extend(_render_ordered_group(group, base_indent))
        else:
            lines.extend(_render_bullet_group(group, base_indent, current_level))
    return lines


def _render_bullet_group(group: list[dict[str, Any]], base_indent: int, level: int) -> list[str]:
    indent = "  " * base_indent
    style_config = _bullet_style_for_level(level)
    attr_parts: list[str] = [f'data-note-level="{level}"']
    class_names = ["note-list", f"note-level-{level}"]
    if extra_class := style_config.get("class"):
        class_names.append(extra_class)
    if class_names:
        attr_parts.append(f'class="{" ".join(class_names)}"')
    if style_value := style_config.get("style"):
        attr_parts.append(f'style="{style_value}"')
    attr_text = f" {' '.join(attr_parts)}" if attr_parts else ""
    lines: list[str] = [f"{indent}<ul{attr_text}>"]
    marker_prefix = style_config.get("marker")
    for node in group:
        item_indent = "  " * (base_indent + 1)
        children = node["children"]
        li_classes = ["note-item", f"note-level-{node['level']}"]
        if marker_prefix:
            li_classes.append("note-item-with-marker")
        li_attr_parts = [f'data-note-level="{node["level"]}"', f'class="{" ".join(li_classes)}"']
        li_attr_text = " " + " ".join(li_attr_parts) if li_attr_parts else ""
        display_text = _apply_marker(node["text"], marker_prefix)
        if children:
            lines.append(f"{item_indent}<li{li_attr_text}>{display_text}")
            lines.extend(_render_note_nodes(children, base_indent + 2))
            lines.append(f"{item_indent}</li>")
        else:
            lines.append(f"{item_indent}<li{li_attr_text}>{display_text}</li>")
    lines.append(f"{indent}</ul>")
    return lines


def _render_ordered_group(group: list[dict[str, Any]], base_indent: int) -> list[str]:
    indent = "  " * base_indent
    lines: list[str] = [f"{indent}<ol type=\"1\">"]
    for node in group:
        item_indent = "  " * (base_indent + 1)
        children = node["children"]
        if children:
            lines.append(f"{item_indent}<li>{node['text']}")
            lines.extend(_render_note_nodes(children, base_indent + 2))
            lines.append(f"{item_indent}</li>")
        else:
            lines.append(f"{item_indent}<li>{node['text']}</li>")
    lines.append(f"{indent}</ol>")
    return lines


def build_notes_markdown(
    fieldnames: list[str],
    rows: list[dict[str, str]],
    source_url: str,
    metadata: MetadataMap,
    profile: NotesProfile,
) -> str:
    """Render the notes markdown document for the provided profile."""

    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    lines: list[str] = [
        f"# {profile.notes_title}",
        "",
        "<!-- AUTO-GENERATED FILE. DO NOT EDIT MANUALLY. -->",
        f"*Last updated: {timestamp}*",
        "",
        f"[Source spreadsheet]({source_url})",
        "",
    ]

    if not fieldnames:
        lines.append("_No data available from spreadsheet._")
        lines.append("")
        return "\n".join(lines)

    preferred_order = [field for field in config.STANDARD_FIELDS if field in fieldnames]
    extra_fields = [field for field in fieldnames if field not in preferred_order]
    ordered_fields = preferred_order + extra_fields

    category_entries: dict[str, list[tuple[str, list[str]]]] = {}

    for row in rows:
        problem = (row.get("Problem") or "Untitled Problem").strip() or "Untitled Problem"
        problem_meta = metadata.get(problem)
        folder_name = problem_meta.folder_name if problem_meta else folder_name_from_title(problem)
        link = problem_meta.link if problem_meta else None
        solution_rel_path = _relative_solution_url(
            profile.notes_output_path.parent,
            profile.problems_dir / folder_name / "solution.py",
        )
        if link:
            links_text = f"*([Problem]({link.url}) | [Solution]({solution_rel_path}))*"
        else:
            links_text = f"*([Solution]({solution_rel_path}))*"
        problem_title = normalize.escape_ordered_list_prefix(problem)
        heading_text = f"**{problem_title}**"
        problem_line = f"{heading_text} {links_text}".strip()

        section_lines: list[str] = []

        for field in ordered_fields:
            if field in {"Problem", "Category"}:
                continue
            raw_value = row.get(field) or ""
            value = normalize.format_cell(raw_value)
            if not value and field != "Notes":
                continue

            if field == "Notes":
                note_entries = normalize.format_notes(raw_value)
                if not note_entries:
                    continue
                if (
                    len(note_entries) == 1
                    and note_entries[0].level == 0
                    and not note_entries[0].ordered
                ):
                    section_lines.append(f"- **Notes:** {note_entries[0].text}")
                else:
                    section_lines.append("- **Notes:**")
                    tree = _build_note_tree(note_entries)
                    section_lines.extend(_render_note_nodes(tree, base_indent=1))
                continue

            section_lines.append(f"- **{field}:** {value}")

        if not section_lines:
            section_lines.append("- _No details provided._")

        category_raw = (row.get("Category") or "").strip()
        categories = normalize.split_categories(category_raw)
        if not categories:
            categories = [config.DEFAULT_CATEGORY]

        for category in categories:
            canonical = config.CATEGORY_ALIASES.get(category, category) or config.DEFAULT_CATEGORY
            category_entries.setdefault(canonical, []).append((problem_line, section_lines.copy()))

    if not category_entries:
        return "\n".join(lines)

    ordered_categories = [
        category
        for category in config.CATEGORY_ORDER
        if category in category_entries and category != config.DEFAULT_CATEGORY
    ]
    ordered_categories.extend(
        category
        for category in category_entries
        if category not in config.CATEGORY_ORDER and category != config.DEFAULT_CATEGORY
    )
    if config.DEFAULT_CATEGORY in category_entries:
        ordered_categories.append(config.DEFAULT_CATEGORY)

    for category in ordered_categories:
        lines.append(f"## {category}")
        lines.append("")
        for problem_line, detail_lines in category_entries[category]:
            lines.append(problem_line)
            lines.extend(detail_lines)
            lines.append("")

    if lines and lines[-1] == "":
        lines.pop()

    return "\n".join(lines)


__all__ = ["build_notes_markdown"]

