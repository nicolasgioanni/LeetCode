# NeetCode 150 Notes

<!-- AUTO-GENERATED FILE. DO NOT EDIT MANUALLY. -->
*Last updated: 2025-10-22 05:34 UTC*

[Source spreadsheet](https://docs.google.com/spreadsheets/d/e/2PACX-1vRw_Ro70SyoCP4FIHwwfkDdwVhXWU_lKwfl6Rw3tXlD1nFD5gfPVk1B0SufuQATexITGzPiwNmeUav0/pub?gid=757254648&single=true&output=csv)

## Array & Hashing

**Contains Duplicate** *([Problem](https://leetcode.com/problems/contains-duplicate/) | [Solution](../Problems/0217.%20Contains%20Duplicate))*
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)
- **Notes:** Hashset, check if the value is in seen otherwise, add it to seen

**Encode and Decode Strings** *([Problem](https://leetcode.com/problems/encode-and-decode-strings/) | [Solution](../Problems/0271.%20Encode%20and%20Decode%20Strings))*
- **Time Complexity:** O(n)
- **Space Complexity:** O(n + m)
- **Notes:**
  <ul>
    <li>Encode saving the new string as (length, unique char, string)</li>
    <li>Decode Looping until we hit our right bound, using pointers front, middle, and end
      <ul>
        <li>Front points to our first number for our string length</li>
        <li>Middle points to our unique char</li>
        <li>End points to the end of our string</li>
      </ul>
    </li>
  </ul>

**Group Anagrams** *([Problem](https://leetcode.com/problems/group-anagrams/) | [Solution](../Problems/0049.%20Group%20Anagrams))*
- **Time Complexity:** O(nm)
- **Space Complexity:** O(nm)
- **Notes:**
  <ul>
    <li>Loop through strings storing list of counts as the key and string as value (defaultdict(list))</li>
    <li>ASCII values for count</li>
  </ul>

**Longest Consecutive Sequence** *([Problem](https://leetcode.com/problems/longest-consecutive-sequence/) | [Solution](../Problems/0128.%20Longest%20Consecutive%20Sequence))*
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)
- **Notes:**
  <ul>
    <li>Use a set to iterate quickly</li>
    <li>Loop over every unique number
      <ul>
        <li>Check if it is a start of a sequence</li>
        <li>If it is, continue to check the numbers after if it is a sequence
          <ul>
            <li>Then compare it to the length of the max</li>
          </ul>
        </li>
      </ul>
    </li>
  </ul>

**Product of Array Except Self** *([Problem](https://leetcode.com/problems/product-of-array-except-self/) | [Solution](../Problems/0238.%20Product%20of%20Array%20Except%20Self))*
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) or O(n)
- **Notes:**
  <ul>
    <li>Result list</li>
    <li>Prefix, equal first then multiply update</li>
    <li>Postfix, multiply first then multiply update</li>
  </ul>

**Top K Frequent Elements** *([Problem](https://leetcode.com/problems/top-k-frequent-elements/) | [Solution](../Problems/0347.%20Top%20K%20Frequent%20Elements))*
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)
- **Notes:**
  <ul>
    <li>Hashmap for count and dict of lists per number in input list storing count as key and number as values</li>
    <li>Loop to get count of each number</li>
    <li>Loop to store each number and its count in dict</li>
    <li>Return the k most frequent numbers</li>
  </ul>

**Two Sum** *([Problem](https://leetcode.com/problems/two-sum/) | [Solution](../Problems/0001.%20Two%20Sum))*
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)
- **Notes:**
  <ul>
    <li>Loop through every value
      <ul>
        <li>If our target - the value we are looking at is in our hashmap of seen values, return them</li>
        <li>Otherwise, add it to our hashmap</li>
      </ul>
    </li>
  </ul>

**Valid Anagram** *([Problem](https://leetcode.com/problems/valid-anagram/) | [Solution](../Problems/0242.%20Valid%20Anagram))*
- **Time Complexity:** O(n + m)
- **Space Complexity:** O(1)
- **Notes:**
  <ul>
    <li>Two ways to solve this:
      <ol type="1">
        <li>Hashmaps to keep track of char count and then compare</li>
        <li>ASCII values list, adding count of 1 and subtracting count of 2, at the end, the list should have counts of all 0s</li>
      </ol>
    </li>
  </ul>

**Valid Sudoku** *([Problem](https://leetcode.com/problems/valid-sudoku/) | [Solution](../Problems/0036.%20Valid%20Sudoku))*
- _No details provided._

## Two Pointers

**Container With Most Water** *([Problem](https://leetcode.com/problems/container-with-most-water/) | [Solution](../Problems/0011.%20Container%20With%20Most%20Water))*
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
- **Notes:**
  <ul>
    <li>Two pointers</li>
    <li>Loop through ends (pointers)</li>
    <li>Calculate area</li>
    <li>Update pointers based on which value is smaller</li>
  </ul>

**Three Sum** *([Problem](https://leetcode.com/problems/3sum/) | [Solution](../Problems/0015.%20Three%20Sum))*
- **Time Complexity:** O(n^2)
- **Space Complexity:** O(1) or O(n)
- **Notes:**
  <ul>
    <li>Result list and sort the input list
      <ul>
        <li>Enumerate though each value in the list</li>
        <li>Check if the smallest value is greater than target</li>
        <li>After the first iteration, check if prev value is the same as current value</li>
        <li>Loop through pointers which are the ends after the value we enumerate</li>
        <li>Calculate threeSum, and update pointers based on whether equal, greater or less than target
          <ul>
            <li>When equal, update both pointers and duplicate check</li>
          </ul>
        </li>
      </ul>
    </li>
  </ul>

**Trapping Rain Water** *([Problem](https://leetcode.com/problems/trapping-rain-water/) | [Solution](../Problems/0042.%20Trapping%20Rain%20Water))*
- _No details provided._

**Two Sum II Input Array Is Sorted** *([Problem](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | [Solution](../Problems/0167.%20Two%20Sum%20II%20Input%20Array%20Is%20Sorted))*
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
- **Notes:**
  <ul>
    <li>Loop 2 pointers
      <ul>
        <li>Calculate twoSum, and update pointers based on whether greater or less than target</li>
      </ul>
    </li>
  </ul>

**Valid Palindrome** *([Problem](https://leetcode.com/problems/valid-palindrome/) | [Solution](../Problems/0125.%20Valid%20Palindrome))*
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
- **Notes:**
  <ul>
    <li>Loop through Two pointers
      <ul>
        <li>Increment/decrement whether pointer value is within ascii values to avoid non numeric values</li>
        <li>Compare characters at pointer values</li>
        <li>Update pointers</li>
      </ul>
    </li>
  </ul>

## Sliding Window

**Best Time to Buy and Sell Stock** *([Problem](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | [Solution](../Problems/0121.%20Best%20Time%20to%20Buy%20and%20Sell%20Stock))*
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
- **Notes:**
  <ul>
    <li>Two pointers
      <ul>
        <li>Loop until our sell pointer crosses input array bounds</li>
        <li>If sell is greater than buy, get the max of our old and current profit</li>
        <li>Otherwise, this means we have a new low buy, so update pointers accordingly</li>
      </ul>
    </li>
  </ul>

**Longest Repeating Character Replacement** *([Problem](https://leetcode.com/problems/longest-repeating-character-replacement/) | [Solution](../Problems/0424.%20Longest%20Repeating%20Character%20Replacement))*
- **Time Complexity:** O(n)
- **Space Complexity:** O(m)
- **Notes:**
  <ul>
    <li>Dictionary to store unique letters as keys and counts as values</li>
    <li>Two pointers, loop with right pointer, update counts and max length
      <ul>
        <li>While the most frequency letter plus k is less than the length of the string
          <ul>
            <li>Update the letters count and left pointer</li>
          </ul>
        </li>
      </ul>
    </li>
  </ul>

**Longest Substring Without Repeating Characters** *([Problem](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | [Solution](../Problems/0003.%20Longest%20Substring%20Without%20Repeating%20Characters))*
- **Time Complexity:** O(n)
- **Space Complexity:** O(m)
- **Notes:**
  <ul>
    <li>Hashmap to store char as key and its index as the value</li>
    <li>Two pointers
      <ul>
        <li>Loop through our right pointer, adding them to hashmap</li>
        <li>If duplicate (already in seen) & last seen duplicate char index greater than our left pointer</li>
        <li>Update left pointer to last seen duplicate char index + 1 (to skip it)</li>
      </ul>
    </li>
  </ul>

**Minimum Window Substring** *([Problem](https://leetcode.com/problems/minimum-window-substring/) | [Solution](../Problems/0076.%20Minimum%20Window%20Substring))*
- **Time Complexity:** O(n + m)
- **Space Complexity:** O(m)
- **Notes:**
  <ul>
    <li>Check if are target substring is empty else continue</li>
    <li>Hashmaps for window and target substring</li>
    <li>Two pointers, loop until our right pointer hits the right bound (end of input string)
      <ul>
        <li>Continously add unique char and their count to our window</li>
        <li>If we have the count for all the unique letters we need save it if is it smaller than our old substring</li>
        <li>Update our left pointer and decrease the count until we don't have what we need anymore</li>
      </ul>
    </li>
  </ul>

**Permutation In String** *([Problem](https://leetcode.com/problems/permutation-in-string/) | [Solution](../Problems/0567.%20Permutation%20In%20String))*
- _No details provided._

**Sliding Window Maximum** *([Problem](https://leetcode.com/problems/sliding-window-maximum/) | [Solution](../Problems/0239.%20Sliding%20Window%20Maximum))*
- _No details provided._

## Stack

**Car Fleet** *([Problem](https://leetcode.com/problems/car-fleet/) | [Solution](../Problems/0853.%20Car%20Fleet))*
- _No details provided._

**Daily Temperatures** *([Problem](https://leetcode.com/problems/daily-temperatures/) | [Solution](../Problems/0739.%20Daily%20Temperatures))*
- _No details provided._

**Evaluate Reverse Polish Notation** *([Problem](https://leetcode.com/problems/evaluate-reverse-polish-notation/) | [Solution](../Problems/0150.%20Evaluate%20Reverse%20Polish%20Notation))*
- _No details provided._

**Generate Parentheses** *([Problem](https://leetcode.com/problems/generate-parentheses/) | [Solution](../Problems/0022.%20Generate%20Parentheses))*
- _No details provided._

**Largest Rectangle In Histogram** *([Problem](https://leetcode.com/problems/largest-rectangle-in-histogram/) | [Solution](../Problems/0084.%20Largest%20Rectangle%20In%20Histogram))*
- _No details provided._

**Min Stack** *([Problem](https://leetcode.com/problems/min-stack/) | [Solution](../Problems/0155.%20Min%20Stack))*
- _No details provided._

**Valid Parentheses** *([Problem](https://leetcode.com/problems/valid-parentheses/) | [Solution](../Problems/0020.%20Valid%20Parentheses))*
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)
- **Notes:**
  <ul>
    <li>Stack and Hashmap to map parentheses
      <ul>
        <li>Loop through every char and check if it is open or close, add opens as needed and check stack if looking at close</li>
        <li>Return whether we have no more opens in our stack or if we run into the wrong close</li>
      </ul>
    </li>
  </ul>

## Binary Search

**Binary Search** *([Problem](https://leetcode.com/problems/binary-search/) | [Solution](../Problems/0704.%20Binary%20Search))*
- **Time Complexity:** O(logn)
- **Space Complexity:** O(1)
- **Notes:**
  <ul>
    <li>Two pointers and loop until they cross, it's okay if they're equal
      <ul>
        <li>If the middle pointer is less than target, update right pointer</li>
        <li>Else means middle pointer is greater than target, update left pointer</li>
      </ul>
    </li>
  </ul>

**Find Minimum In Rotated Sorted Array** *([Problem](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) | [Solution](../Problems/0153.%20Find%20Minimum%20In%20Rotated%20Sorted%20Array))*
- **Time Complexity:** O(log n)
- **Space Complexity:** O(1)
- **Notes:**
  <ul>
    <li>Two pointers, loop until they cross
      <ul>
        <li>If our middle pointer is less than our right, its impossible to have a smaller number than middle</li>
        <li>Else means it is greater and our right subarray has the smaller value than our middle</li>
        <li>Last case, middle and left pointer will be the same, and if it's greater than our right, l = m + 1 = r, next iteration pointers cross</li>
      </ul>
    </li>
  </ul>

**Koko Eating Bananas** *([Problem](https://leetcode.com/problems/koko-eating-bananas/) | [Solution](../Problems/0875.%20Koko%20Eating%20Bananas))*
- **Time Complexity:** O(lognm)
- **Space Complexity:** O(1)
- **Notes:**
  <ul>
    <li>Two pointers, between values 1 and max rate per hour
      <ul>
        <li>Loop until pointers cross, it's okay if they're equal</li>
        <li>Calculate total hours it takes to eat all bananas with middle rate (math.ceil(float(x) / m))</li>
        <li>If valid, update right pointer</li>
        <li>Else this means we didn't finish eating in time, update left (to eat more per hour)</li>
      </ul>
    </li>
  </ul>

**Median of Two Sorted Arrays** *([Problem](https://leetcode.com/problems/median-of-two-sorted-arrays/) | [Solution](../Problems/0004.%20Median%20of%20Two%20Sorted%20Arrays))*
- _No details provided._

**Search a 2D Matrix** *([Problem](https://leetcode.com/problems/search-a-2d-matrix/) | [Solution](../Problems/0074.%20Search%20a%202D%20Matrix))*
- **Time Complexity:** O(lognm)
- **Space Complexity:** O(1)
- **Notes:**
  <ul>
    <li>Four pointers, 2 for rows top and bottom, 2 for columns left and right
      <ul>
        <li>Loop until the row pointers cross, it's okay if they're equal, get middle row</li>
        <li>If the first value in the middle row is less than target, update bottom row</li>
        <li>If the last value in the middle row is greater than target, update top row</li>
        <li>Else, means target must be in row and perform traditional binary search</li>
      </ul>
    </li>
  </ul>

**Search In Rotated Sorted Array** *([Problem](https://leetcode.com/problems/search-in-rotated-sorted-array/) | [Solution](../Problems/0033.%20Search%20In%20Rotated%20Sorted%20Array))*
- **Time Complexity:** O(log n)
- **Space Complexity:** O(1)
- **Notes:**
  <ul>
    <li>Two pointers and loop until they cross, it's okay if they're equal
      <ul>
        <li>If our middle is the target, return, otherwise, two subcases</li>
        <li>Elif middle is greater than our left pointer (left side is sorted)
          <ul>
            <li>And If our target is greater than our middle pointer or less than our left pointer (meaning it's not in our sorted side), update left</li>
            <li>Else, our target is in our sorted side and update right</li>
          </ul>
        </li>
        <li>Else, meaning our right side is sorted
          <ul>
            <li>And our target is less than our middle pointer but greater than our right pointer (meaning it's not in our sorted sid), update right</li>
            <li>Else, our target is in our sorted side and update left</li>
          </ul>
        </li>
      </ul>
    </li>
  </ul>

**Time Based Key Value Store** *([Problem](https://leetcode.com/problems/time-based-key-value-store/) | [Solution](../Problems/0981.%20Time%20Based%20Key%20Value%20Store))*
- _No details provided._

## Linked List

**Add Two Numbers** *([Problem](https://leetcode.com/problems/add-two-numbers/) | [Solution](../Problems/0002.%20Add%20Two%20Numbers))*
- _No details provided._

**Copy List With Random Pointer** *([Problem](https://leetcode.com/problems/copy-list-with-random-pointer/) | [Solution](../Problems/0138.%20Copy%20List%20With%20Random%20Pointer))*
- _No details provided._

**Find The Duplicate Number** *([Problem](https://leetcode.com/problems/find-the-duplicate-number/) | [Solution](../Problems/0287.%20Find%20The%20Duplicate%20Number))*
- _No details provided._

**Linked List Cycle** *([Problem](https://leetcode.com/problems/linked-list-cycle/) | [Solution](../Problems/0141.%20Linked%20List%20Cycle))*
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
- **Notes:**
  <ul>
    <li>Slow/fast pointers
      <ul>
        <li>Loop until fast and its next are None constantly checking if the pointers nodes are ever equal</li>
      </ul>
    </li>
  </ul>

**LRU Cache** *([Problem](https://leetcode.com/problems/lru-cache/) | [Solution](../Problems/0146.%20LRU%20Cache))*
- _No details provided._

**Merge K Sorted Lists** *([Problem](https://leetcode.com/problems/merge-k-sorted-lists/) | [Solution](../Problems/0023.%20Merge%20K%20Sorted%20Lists))*
- **Time Complexity:** O(n log k)
- **Space Complexity:** O(log k)
- **Notes:**
  <ul>
    <li>Two pointers, Divide and conquer (recursive)
      <ul>
        <li>Divide: Get the range of lists, divide until we only look at 1 which is sorted (pointers are same)</li>
        <li>Two pointers/conquer: Used to look at two nodes from divide and begin merging sorted lists into 1 sorted list</li>
      </ul>
    </li>
    <li>Key: Recursivly divide until we only have a list from both left and right halves, then slowly merge them until we have 1 resulting list</li>
  </ul>

**Merge Two Sorted Lists** *([Problem](https://leetcode.com/problems/merge-two-sorted-lists/) | [Solution](../Problems/0021.%20Merge%20Two%20Sorted%20Lists))*
- **Time Complexity:** O(n + m)
- **Space Complexity:** O(1)
- **Notes:**
  <ul>
    <li>1) Edge case, 2) determine head node, 3) merge loop, 4) attach rest
      <ul>
        <li>Edge case if lists are None</li>
        <li>Compare list.val and set as head and tail, move to next node in list we took node from</li>
        <li>Loop while both lists have nodes, attaching smaller node to tail.next and updating tail to tail.next</li>
        <li>Tail.next is the node that is not None</li>
      </ul>
    </li>
  </ul>

**Remove Nth Node From End of List** *([Problem](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) | [Solution](../Problems/0019.%20Remove%20Nth%20Node%20From%20End%20of%20List))*
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
- **Notes:**
  <ul>
    <li>Slow/fast pointers, slow = head, fast = n
      <ul>
        <li>If n is the size of the list (meaning fast is None) return the next node after the head</li>
        <li>Else we loop until the node after fast is None (because we want slow to point to the node before our nth end node)
          <ul>
            <li>Then, redirect links</li>
          </ul>
        </li>
      </ul>
    </li>
  </ul>

**Reorder List** *([Problem](https://leetcode.com/problems/reorder-list/) | [Solution](../Problems/0143.%20Reorder%20List))*
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
- **Notes:**
  <ul>
    <li>Slow/fast pointers, reverse second half, merge lists:
      <ul>
        <li>Slow/fast pointers to find second half, slow.next is our start second half, fast to find our end bound</li>
        <li>Then we need to reverse the links so we start at the end and point to the middle (second half points backwards)</li>
        <li>While second, save next nodes, change the nodes our currents point to, update our current nodes to temps</li>
      </ul>
    </li>
  </ul>

**Reverse Linked List** *([Problem](https://leetcode.com/problems/reverse-linked-list/) | [Solution](../Problems/0206.%20Reverse%20Linked%20List))*
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
- **Notes:**
  <ul>
    <li>Think of creating a new List starting with None, and redirecting every node to point to that new list 1 by 1
      <ul>
        <li>Update our current nodes next to point to our previous</li>
        <li>Change our prevous pointer to be our current node (to continue iterating)</li>
        <li>Change our old current nodes next (before we changed it) to be our new current</li>
      </ul>
    </li>
  </ul>

**Reverse Nodes In K Group** *([Problem](https://leetcode.com/problems/reverse-nodes-in-k-group/) | [Solution](../Problems/0025.%20Reverse%20Nodes%20In%20K%20Group))*
- _No details provided._

## Trees

**Balanced Binary Tree** *([Problem](https://leetcode.com/problems/balanced-binary-tree/) | [Solution](../Problems/0110.%20Balanced%20Binary%20Tree))*
- _No details provided._

**Binary Tree Level Order Traversal** *([Problem](https://leetcode.com/problems/binary-tree-level-order-traversal/) | [Solutions](../Problems/0102.%20Binary%20Tree%20Level%20Order%20Traversal))*
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)
- **Notes:**
  <ul>
    <li>Iterate the tree using a queue while loop
      <ul>
        <li>Get the amount of nodes at that depth (length of queue)</li>
        <li>For every node at that depth, pop it (queue.popleft()), and add it to a temp list for that depth if not null</li>
        <li>If the temp list is not null (meaning nodes were present at that depth, add the temp list to the result list</li>
      </ul>
    </li>
  </ul>

**Binary Tree Maximum Path Sum** *([Problem](https://leetcode.com/problems/binary-tree-maximum-path-sum/) | [Solutions](../Problems/0124.%20Binary%20Tree%20Maximum%20Path%20Sum))*
- _No details provided._

**Binary Tree Right Side View** *([Problem](https://leetcode.com/problems/binary-tree-right-side-view/) | [Solution](../Problems/0199.%20Binary%20Tree%20Right%20Side%20View))*
- _No details provided._

**Construct Binary Tree From Preorder And Inorder Traversal** *([Problem](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) | [Solutions](../Problems/0105.%20Construct%20Binary%20Tree%20From%20Preorder%20And%20Inorder%20Traversal))*
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)
- **Notes:**
  <ul>
    <li>Idea: Preorder gives the root; Inorder tells us how to split into subtress
      <ul>
        <li>Make a Inorder index dictonary to map the inorder values to indices for O(1) loopups</li>
        <li>Nested recursive function with four pointer parameters: preorder left and right, inorder left and right
          <ul>
            <li>Base case: Make sure that our left pointers for both preorder and in order do not cross eachother (okay is equal)</li>
            <li>Root: Always build our root node with the preorder list index at our preorder left pointer</li>
            <li>Split: We find the index of that value in the preorder list, in the inorder list (rootIndex) using our dictionary</li>
            <li>Left Size (leftHalf): Compute how many nodes are in the left subtree by subtracting the inorder index (root Index) by our inorder left pointer</li>
          </ul>
        </li>
      </ul>
    </li>
    <li>Recurse Left:
      <ul>
        <li>preLeft: Move forward by 1 (skip over the root in preorder).</li>
        <li>preRight: Move our pointer to our current preLeft + the number of nodes in the leftHalf</li>
        <li>inLeft: Keep the same inLeft</li>
        <li>inRight: Move our pointer to the middle (rootIndex) - 1 to exclude our current root node (everything to the left of the root in inorder)</li>
      </ul>
    </li>
    <li>Recurse Right:
      <ul>
        <li>preLeft: Move the pointer over by 1 + our current preLeft + the length of the leftHalf</li>
        <li>preRight: Keep the same preRight</li>
        <li>inLeft: Move our pointer to the rootIndex + 1 (everything to the right of the root in inorder).</li>
        <li>inRight: Keep the same inRight</li>
      </ul>
    </li>
    <li>Note: Only compare or use index values together if they are part of the same list</li>
  </ul>

**Count Good Nodes In Binary Tree** *([Problem](https://leetcode.com/problems/count-good-nodes-in-binary-tree/) | [Solution](../Problems/1448.%20Count%20Good%20Nodes%20In%20Binary%20Tree))*
- _No details provided._

**Diameter of Binary Tree** *([Problem](https://leetcode.com/problems/diameter-of-binary-tree/) | [Solution](../Problems/0543.%20Diameter%20of%20Binary%20Tree))*
- _No details provided._

**Invert Binary Tree** *([Problem](https://leetcode.com/problems/invert-binary-tree/) | [Solution](../Problems/0226.%20Invert%20Binary%20Tree))*
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)
- **Notes:** 1) Edge case, 2) swap left and right nodes, 3) Recursively call on both left and right nodes (the ones we changed)

**Kth Smallest Element In a Bst** *([Problem](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) | [Solutions](../Problems/0230.%20Kth%20Smallest%20Element%20In%20a%20Bst))*
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)
- **Notes:**
  <ul>
    <li>Inorder Traversal: Loop while stack or node we're looking at is not null
      <ul>
        <li>Go left as far as possible, pushing nodes onto a stack</li>
        <li>Then, begin popping the smallest value, decrementing k, and going to that nodes's right child</li>
      </ul>
    </li>
  </ul>

**Lowest Common Ancestor of a Binary Search Tree** *([Problem](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) | [Solution](../Problems/0235.%20Lowest%20Common%20Ancestor%20of%20a%20Binary%20Search%20Tree))*
- **Time Complexity:** O(h)
- **Space Complexity:** O(1)
- **Notes:**
  <ul>
    <li>Case 1: Both nodes are greater than our current node, we go right</li>
    <li>Case 2: Both nodes are less than our current node, we go left</li>
    <li>Case 3: This means a split occured (one node is to the left and the other is to the right) or one node equals our current, LCA found</li>
  </ul>

**Maximum Depth of Binary Tree** *([Problem](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | [Solution](../Problems/0104.%20Maximum%20Depth%20of%20Binary%20Tree))*
- **Time Complexity:** O(n)
- **Space Complexity:** O(h) - O(log n), O(n)
- **Notes:**
  <ul>
    <li>Case 1 (no node): if root is None, that side of the tree is empty, so depth = 0.</li>
    <li>Case 2 (node exists): return 1 (for the current node) plus the max depth of the left and right subtrees.</li>
  </ul>

**Same Tree** *([Problem](https://leetcode.com/problems/same-tree/) | [Solution](../Problems/0100.%20Same%20Tree))*
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)
- **Notes:**
  <ul>
    <li>Base case: return true if nodes are null
      <ul>
        <li>Then if both not null and equal, recursively return the comparision of the left and right nodes of both trees</li>
        <li>Otherwise, false</li>
      </ul>
    </li>
  </ul>

**Serialize And Deserialize Binary Tree** *([Problem](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) | [Solution](../Problems/0297.%20Serialize%20And%20Deserialize%20Binary%20Tree))*
- _No details provided._

**Subtree of Another Tree** *([Problem](https://leetcode.com/problems/subtree-of-another-tree/) | [Solutions](../Problems/0572.%20Subtree%20of%20Another%20Tree))*
- **Time Complexity:** O(nm)
- **Space Complexity:** O(n + m)
- **Notes:**
  <ul>
    <li>Iterate the tree using a basic stack or recursive call
      <ul>
        <li>If found subtree, perform same tree check (either recursively with a seperate function or iteratively with a stack)</li>
      </ul>
    </li>
  </ul>

**Validate Binary Search Tree** *([Problem](https://leetcode.com/problems/validate-binary-search-tree/) | [Solutions](../Problems/0098.%20Validate%20Binary%20Search%20Tree))*
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)
- **Notes:**
  <ul>
    <li>Nested function with 3 parameters (node, left bound, right bound):
      <ul>
        <li>Our first root node can be in between negative infinity and infinity</li>
        <li>As we iterate recursively, we must update our left and right bounds accordingly
          <ul>
            <li>Going left, update right bound to previous nodes value</li>
            <li>Going right, update left bound to previous nodes value</li>
          </ul>
        </li>
      </ul>
    </li>
  </ul>

## Backtracking

**Combination Sum II** *([Problem](https://leetcode.com/problems/combination-sum-ii/) | [Solution](../Problems/0040.%20Combination%20Sum%20II))*
- _No details provided._

**Combination Sum** *([Problem](https://leetcode.com/problems/combination-sum/) | [Solution](../Problems/0039.%20Combination%20Sum))*
- _No details provided._

**Letter Combinations of a Phone Number** *([Problem](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) | [Solution](../Problems/0017.%20Letter%20Combinations%20of%20a%20Phone%20Number))*
- _No details provided._

**N Queens** *([Problem](https://leetcode.com/problems/n-queens/) | [Solution](../Problems/0051.%20N%20Queens))*
- _No details provided._

**Palindrome Partitioning** *([Problem](https://leetcode.com/problems/palindrome-partitioning/) | [Solution](../Problems/0131.%20Palindrome%20Partitioning))*
- _No details provided._

**Permutations** *([Problem](https://leetcode.com/problems/permutations/) | [Solution](../Problems/0046.%20Permutations))*
- _No details provided._

**Subsets II** *([Problem](https://leetcode.com/problems/subsets-ii/) | [Solution](../Problems/0090.%20Subsets%20II))*
- _No details provided._

**Subsets** *([Problem](https://leetcode.com/problems/subsets/) | [Solution](../Problems/0078.%20Subsets))*
- _No details provided._

**Word Search** *([Problem](https://leetcode.com/problems/word-search/) | [Solution](../Problems/0079.%20Word%20Search))*
- _No details provided._

## Tries

**Design Add And Search Words Data Structure** *([Problem](https://leetcode.com/problems/design-add-and-search-words-data-structure/) | [Solution](../Problems/0211.%20Design%20Add%20And%20Search%20Words%20Data%20Structure))*
- _No details provided._

**Implement Trie Prefix Tree** *([Problem](https://leetcode.com/problems/implement-trie-prefix-tree/) | [Solution](../Problems/0208.%20Implement%20Trie%20Prefix%20Tree))*
- _No details provided._

**Word Search II** *([Problem](https://leetcode.com/problems/word-search-ii/) | [Solution](../Problems/0212.%20Word%20Search%20II))*
- _No details provided._

## Graphs

**Clone Graph** *([Problem](https://leetcode.com/problems/clone-graph/) | [Solution](../Problems/0133.%20Clone%20Graph))*
- _No details provided._

**Course Schedule II** *([Problem](https://leetcode.com/problems/course-schedule-ii/) | [Solution](../Problems/0210.%20Course%20Schedule%20II))*
- _No details provided._

**Course Schedule** *([Problem](https://leetcode.com/problems/course-schedule/) | [Solutions](../Problems/0207.%20Course%20Schedule))*
- _No details provided._

**Graph Valid Tree** *([Problem](https://leetcode.com/problems/graph-valid-tree/) | [Solutions](../Problems/0261.%20Graph%20Valid%20Tree))*
- _No details provided._

**Max Area of Island** *([Problem](https://leetcode.com/problems/max-area-of-island/) | [Solution](../Problems/0695.%20Max%20Area%20of%20Island))*
- _No details provided._

**Number of Connected Components In An Undirected Graph** *([Problem](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/) | [Solutions](../Problems/0323.%20Number%20of%20Connected%20Components%20In%20An%20Undirected%20Graph))*
- _No details provided._

**Number of Islands** *([Problem](https://leetcode.com/problems/number-of-islands/) | [Solutions](../Problems/0200.%20Number%20of%20Islands))*
- _No details provided._

**Pacific Atlantic Water Flow** *([Problem](https://leetcode.com/problems/pacific-atlantic-water-flow/) | [Solutions](../Problems/0417.%20Pacific%20Atlantic%20Water%20Flow))*
- _No details provided._

**Redundant Connection** *([Problem](https://leetcode.com/problems/redundant-connection/) | [Solution](../Problems/0684.%20Redundant%20Connection))*
- _No details provided._

**Rotting Oranges** *([Problem](https://leetcode.com/problems/rotting-oranges/) | [Solution](../Problems/0994.%20Rotting%20Oranges))*
- _No details provided._

**Surrounded Regions** *([Problem](https://leetcode.com/problems/surrounded-regions/) | [Solution](../Problems/0130.%20Surrounded%20Regions))*
- _No details provided._

**Walls And Gates** *([Problem](https://leetcode.com/problems/walls-and-gates/) | [Solution](../Problems/0286.%20Walls%20And%20Gates))*
- _No details provided._

**Word Ladder** *([Problem](https://leetcode.com/problems/word-ladder/) | [Solution](../Problems/0127.%20Word%20Ladder))*
- _No details provided._

## Advanced Graphs

**Alien Dictionary** *([Problem](https://leetcode.com/problems/alien-dictionary/) | [Solution](../Problems/0269.%20Alien%20Dictionary))*
- _No details provided._

**Cheapest Flights Within K Stops** *([Problem](https://leetcode.com/problems/cheapest-flights-within-k-stops/) | [Solution](../Problems/0787.%20Cheapest%20Flights%20Within%20K%20Stops))*
- _No details provided._

**Min Cost to Connect All Points** *([Problem](https://leetcode.com/problems/min-cost-to-connect-all-points/) | [Solution](../Problems/1584.%20Min%20Cost%20to%20Connect%20All%20Points))*
- _No details provided._

**Network Delay Time** *([Problem](https://leetcode.com/problems/network-delay-time/) | [Solution](../Problems/0743.%20Network%20Delay%20Time))*
- _No details provided._

**Reconstruct Itinerary** *([Problem](https://leetcode.com/problems/reconstruct-itinerary/) | [Solution](../Problems/0332.%20Reconstruct%20Itinerary))*
- _No details provided._

**Swim In Rising Water** *([Problem](https://leetcode.com/problems/swim-in-rising-water/) | [Solution](../Problems/0778.%20Swim%20In%20Rising%20Water))*
- _No details provided._

## 1-D Dynamic Programming

**Climbing Stairs** *([Problem](https://leetcode.com/problems/climbing-stairs/) | [Solution](../Problems/0070.%20Climbing%20Stairs))*
- _No details provided._

**Coin Change** *([Problem](https://leetcode.com/problems/coin-change/) | [Solution](../Problems/0322.%20Coin%20Change))*
- _No details provided._

**Decode Ways** *([Problem](https://leetcode.com/problems/decode-ways/) | [Solution](../Problems/0091.%20Decode%20Ways))*
- _No details provided._

**House Robber II** *([Problem](https://leetcode.com/problems/house-robber-ii/) | [Solution](../Problems/0213.%20House%20Robber%20II))*
- _No details provided._

**House Robber** *([Problem](https://leetcode.com/problems/house-robber/) | [Solution](../Problems/0198.%20House%20Robber))*
- _No details provided._

**Longest Increasing Subsequence** *([Problem](https://leetcode.com/problems/longest-increasing-subsequence/) | [Solution](../Problems/0300.%20Longest%20Increasing%20Subsequence))*
- _No details provided._

**Longest Palindromic Substring** *([Problem](https://leetcode.com/problems/longest-palindromic-substring/) | [Solution](../Problems/0005.%20Longest%20Palindromic%20Substring))*
- _No details provided._

**Maximum Product Subarray** *([Problem](https://leetcode.com/problems/maximum-product-subarray/) | [Solution](../Problems/0152.%20Maximum%20Product%20Subarray))*
- _No details provided._

**Min Cost Climbing Stairs** *([Problem](https://leetcode.com/problems/min-cost-climbing-stairs/) | [Solution](../Problems/0746.%20Min%20Cost%20Climbing%20Stairs))*
- _No details provided._

**Palindromic Substrings** *([Problem](https://leetcode.com/problems/palindromic-substrings/) | [Solution](../Problems/0647.%20Palindromic%20Substrings))*
- _No details provided._

**Partition Equal Subset Sum** *([Problem](https://leetcode.com/problems/partition-equal-subset-sum/) | [Solution](../Problems/0416.%20Partition%20Equal%20Subset%20Sum))*
- _No details provided._

**Word Break** *([Problem](https://leetcode.com/problems/word-break/) | [Solution](../Problems/0139.%20Word%20Break))*
- _No details provided._

## 2-D Dynamic Programming

**Best Time to Buy And Sell Stock With Cooldown** *([Problem](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/) | [Solution](../Problems/0309.%20Best%20Time%20to%20Buy%20And%20Sell%20Stock%20With%20Cooldown))*
- _No details provided._

**Burst Balloons** *([Problem](https://leetcode.com/problems/burst-balloons/) | [Solution](../Problems/0312.%20Burst%20Balloons))*
- _No details provided._

**Coin Change II** *([Problem](https://leetcode.com/problems/coin-change-ii/) | [Solution](../Problems/0518.%20Coin%20Change%20II))*
- _No details provided._

**Distinct Subsequences** *([Problem](https://leetcode.com/problems/distinct-subsequences/) | [Solution](../Problems/0115.%20Distinct%20Subsequences))*
- _No details provided._

**Edit Distance** *([Problem](https://leetcode.com/problems/edit-distance/) | [Solution](../Problems/0072.%20Edit%20Distance))*
- _No details provided._

**Interleaving String** *([Problem](https://leetcode.com/problems/interleaving-string/) | [Solution](../Problems/0097.%20Interleaving%20String))*
- _No details provided._

**Longest Common Subsequence** *([Problem](https://leetcode.com/problems/longest-common-subsequence/) | [Solution](../Problems/1143.%20Longest%20Common%20Subsequence))*
- _No details provided._

**Longest Increasing Path In a Matrix** *([Problem](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/) | [Solution](../Problems/0329.%20Longest%20Increasing%20Path%20In%20a%20Matrix))*
- _No details provided._

**Regular Expression Matching** *([Problem](https://leetcode.com/problems/regular-expression-matching/) | [Solution](../Problems/0010.%20Regular%20Expression%20Matching))*
- _No details provided._

**Target Sum** *([Problem](https://leetcode.com/problems/target-sum/) | [Solution](../Problems/0494.%20Target%20Sum))*
- _No details provided._

**Unique Paths** *([Problem](https://leetcode.com/problems/unique-paths/) | [Solution](../Problems/0062.%20Unique%20Paths))*
- _No details provided._

## Greedy

**Gas Station** *([Problem](https://leetcode.com/problems/gas-station/) | [Solution](../Problems/0134.%20Gas%20Station))*
- _No details provided._

**Hand of Straights** *([Problem](https://leetcode.com/problems/hand-of-straights/) | [Solution](../Problems/0846.%20Hand%20of%20Straights))*
- _No details provided._

**Jump Game II** *([Problem](https://leetcode.com/problems/jump-game-ii/) | [Solution](../Problems/0045.%20Jump%20Game%20II))*
- _No details provided._

**Jump Game** *([Problem](https://leetcode.com/problems/jump-game/) | [Solution](../Problems/0055.%20Jump%20Game))*
- _No details provided._

**Maximum Subarray** *([Problem](https://leetcode.com/problems/maximum-subarray/) | [Solution](../Problems/0053.%20Maximum%20Subarray))*
- _No details provided._

**Merge Triplets to Form Target Triplet** *([Problem](https://leetcode.com/problems/merge-triplets-to-form-target-triplet/) | [Solution](../Problems/1899.%20Merge%20Triplets%20to%20Form%20Target%20Triplet))*
- _No details provided._

**Partition Labels** *([Problem](https://leetcode.com/problems/partition-labels/) | [Solution](../Problems/0763.%20Partition%20Labels))*
- _No details provided._

**Valid Parenthesis String** *([Problem](https://leetcode.com/problems/valid-parenthesis-string/) | [Solution](../Problems/0678.%20Valid%20Parenthesis%20String))*
- _No details provided._

## Intervals

**Insert Interval** *([Problem](https://leetcode.com/problems/insert-interval/) | [Solution](../Problems/0057.%20Insert%20Interval))*
- _No details provided._

**Meeting Rooms II** *([Problem](https://leetcode.com/problems/meeting-rooms-ii/) | [Solution](../Problems/0253.%20Meeting%20Rooms%20II))*
- _No details provided._

**Meeting Rooms** *([Problem](https://leetcode.com/problems/meeting-rooms/) | [Solution](../Problems/0252.%20Meeting%20Rooms))*
- _No details provided._

**Merge Intervals** *([Problem](https://leetcode.com/problems/merge-intervals/) | [Solution](../Problems/0056.%20Merge%20Intervals))*
- _No details provided._

**Minimum Interval to Include Each Query** *([Problem](https://leetcode.com/problems/minimum-interval-to-include-each-query/) | [Solution](../Problems/1851.%20Minimum%20Interval%20to%20Include%20Each%20Query))*
- _No details provided._

**Non Overlapping Intervals** *([Problem](https://leetcode.com/problems/non-overlapping-intervals/) | [Solution](../Problems/0435.%20Non%20Overlapping%20Intervals))*
- _No details provided._

## Math & Geometry

**Detect Squares** *([Problem](https://leetcode.com/problems/detect-squares/) | [Solution](../Problems/2013.%20Detect%20Squares))*
- _No details provided._

**Happy Number** *([Problem](https://leetcode.com/problems/happy-number/) | [Solution](../Problems/0202.%20Happy%20Number))*
- _No details provided._

**Multiply Strings** *([Problem](https://leetcode.com/problems/multiply-strings/) | [Solution](../Problems/0043.%20Multiply%20Strings))*
- _No details provided._

**Plus One** *([Problem](https://leetcode.com/problems/plus-one/) | [Solution](../Problems/0066.%20Plus%20One))*
- _No details provided._

**Pow** *([Problem](https://leetcode.com/problems/pow/) | [Solution](../Problems/Pow))*
- _No details provided._

**Rotate Image** *([Problem](https://leetcode.com/problems/rotate-image/) | [Solution](../Problems/0048.%20Rotate%20Image))*
- _No details provided._

**Set Matrix Zeroes** *([Problem](https://leetcode.com/problems/set-matrix-zeroes/) | [Solution](../Problems/0073.%20Set%20Matrix%20Zeroes))*
- _No details provided._

**Spiral Matrix** *([Problem](https://leetcode.com/problems/spiral-matrix/) | [Solution](../Problems/0054.%20Spiral%20Matrix))*
- _No details provided._

## Bit Manipulation

**Counting Bits** *([Problem](https://leetcode.com/problems/counting-bits/) | [Solution](../Problems/0338.%20Counting%20Bits))*
- _No details provided._

**Missing Number** *([Problem](https://leetcode.com/problems/missing-number/) | [Solution](../Problems/0268.%20Missing%20Number))*
- _No details provided._

**Number of 1 Bits** *([Problem](https://leetcode.com/problems/number-of-1-bits/) | [Solution](../Problems/0191.%20Number%20of%201%20Bits))*
- _No details provided._

**Reverse Bits** *([Problem](https://leetcode.com/problems/reverse-bits/) | [Solution](../Problems/0190.%20Reverse%20Bits))*
- _No details provided._

**Reverse Integer** *([Problem](https://leetcode.com/problems/reverse-integer/) | [Solution](../Problems/0007.%20Reverse%20Integer))*
- _No details provided._

**Single Number** *([Problem](https://leetcode.com/problems/single-number/) | [Solution](../Problems/0136.%20Single%20Number))*
- _No details provided._

**Sum of Two Integers** *([Problem](https://leetcode.com/problems/sum-of-two-integers/) | [Solution](../Problems/0371.%20Sum%20of%20Two%20Integers))*
- _No details provided._

## Heap

**Design Twitter** *([Problem](https://leetcode.com/problems/design-twitter/) | [Solution](../Problems/0355.%20Design%20Twitter))*
- _No details provided._

**Find Median From Data Stream** *([Problem](https://leetcode.com/problems/find-median-from-data-stream/) | [Solution](../Problems/0295.%20Find%20Median%20From%20Data%20Stream))*
- _No details provided._

**K Closest Points to Origin** *([Problem](https://leetcode.com/problems/k-closest-points-to-origin/) | [Solution](../Problems/0973.%20K%20Closest%20Points%20to%20Origin))*
- _No details provided._

**Kth Largest Element In a Stream** *([Problem](https://leetcode.com/problems/kth-largest-element-in-a-stream/) | [Solution](../Problems/0703.%20Kth%20Largest%20Element%20In%20a%20Stream))*
- _No details provided._

**Kth Largest Element In An Array** *([Problem](https://leetcode.com/problems/kth-largest-element-in-an-array/) | [Solution](../Problems/0215.%20Kth%20Largest%20Element%20In%20An%20Array))*
- _No details provided._

**Last Stone Weight** *([Problem](https://leetcode.com/problems/last-stone-weight/) | [Solution](../Problems/1046.%20Last%20Stone%20Weight))*
- _No details provided._

**Task Scheduler** *([Problem](https://leetcode.com/problems/task-scheduler/) | [Solution](../Problems/0621.%20Task%20Scheduler))*
- _No details provided._

## Priority Queue

**Design Twitter** *([Problem](https://leetcode.com/problems/design-twitter/) | [Solution](../Problems/0355.%20Design%20Twitter))*
- _No details provided._

**Find Median From Data Stream** *([Problem](https://leetcode.com/problems/find-median-from-data-stream/) | [Solution](../Problems/0295.%20Find%20Median%20From%20Data%20Stream))*
- _No details provided._

**K Closest Points to Origin** *([Problem](https://leetcode.com/problems/k-closest-points-to-origin/) | [Solution](../Problems/0973.%20K%20Closest%20Points%20to%20Origin))*
- _No details provided._

**Kth Largest Element In a Stream** *([Problem](https://leetcode.com/problems/kth-largest-element-in-a-stream/) | [Solution](../Problems/0703.%20Kth%20Largest%20Element%20In%20a%20Stream))*
- _No details provided._

**Kth Largest Element In An Array** *([Problem](https://leetcode.com/problems/kth-largest-element-in-an-array/) | [Solution](../Problems/0215.%20Kth%20Largest%20Element%20In%20An%20Array))*
- _No details provided._

**Last Stone Weight** *([Problem](https://leetcode.com/problems/last-stone-weight/) | [Solution](../Problems/1046.%20Last%20Stone%20Weight))*
- _No details provided._

**Task Scheduler** *([Problem](https://leetcode.com/problems/task-scheduler/) | [Solution](../Problems/0621.%20Task%20Scheduler))*
- _No details provided._