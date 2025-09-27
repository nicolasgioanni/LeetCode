﻿"""Smoke tests for leetnotes renderers."""

from __future__ import annotations

from leetnotes import config
from leetnotes.models import ProblemLink, ProblemMetadata
from leetnotes.render_index import build_problem_index
from leetnotes.render_notes import build_notes_markdown


BLIND75 = config.get_profile("blind75")
NEETCODE150 = config.get_profile("neetcode150")


def test_build_notes_markdown_includes_problem_links() -> None:
    fieldnames = ["Problem", "Category", "Notes"]
    rows = [
        {
            "Problem": "Two Sum",
            "Category": "Array & Hashing",
            "Notes": "Remember to use a hash map.",
        }
    ]
    link = ProblemLink(title="Two Sum", slug="two-sum", frontend_id="1")
    metadata = {
        "Two Sum": ProblemMetadata(folder_name="0001. Two Sum", link=link),
    }

    result = build_notes_markdown(fieldnames, rows, "https://example.com", metadata, BLIND75)

    assert "**Two Sum**" in result
    assert "[Problem](https://leetcode.com/problems/two-sum/)" in result
    assert "[Solution](../Problems/0001.%20Two%20Sum/solution.py)" in result
    assert "Remember to use a hash map." in result


def test_build_problem_index_groups_by_category() -> None:
    rows = [
        {
            "Problem": "Two Sum",
            "Category": "Array & Hashing",
        },
        {
            "Problem": "Binary Search",
            "Category": "Binary Search",
        },
    ]
    metadata = {
        "Two Sum": ProblemMetadata(folder_name="0001. Two Sum", link=None),
        "Binary Search": ProblemMetadata(folder_name="0704. Binary Search", link=None),
    }

    result = build_problem_index(rows, metadata, BLIND75)

    assert "## Array & Hashing" in result
    assert "## Binary Search" in result
    assert "./0001.%20Two%20Sum/solution.py" in result
    assert "./0704.%20Binary%20Search/solution.py" in result


def test_alternate_profile_updates_solution_links() -> None:
    fieldnames = ["Problem", "Category"]
    rows = [
        {
            "Problem": "LRU Cache",
            "Category": "Linked List",
        }
    ]
    metadata = {
        "LRU Cache": ProblemMetadata(folder_name="0146. LRU Cache", link=None),
    }

    notes_output = build_notes_markdown(fieldnames, rows, "https://example.com", metadata, NEETCODE150)
    index_output = build_problem_index(rows, metadata, NEETCODE150)

    assert "../Problems/NeetCode150/0146.%20LRU%20Cache/solution.py" in notes_output
    assert "./0146.%20LRU%20Cache/solution.py" in index_output
    assert "# NeetCode 150 Notes" in notes_output
    assert "# NeetCode 150 Problem Index" in index_output