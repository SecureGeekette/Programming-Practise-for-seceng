234. Palindrome Linked List

Given the head of a singly linked list, return true if it is a 
palindrome or false otherwise.

Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false
 
Constraints:
The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9

Solution:

O(n) space complexity because we're making a new list, 0(n) time complexity
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        curr = head
        ll_nodes = []

        while curr:
            ll_nodes.append(curr.val)
            curr = curr.next

        start = 0
        end = len(ll_nodes) - 1

        while start <= end:
            if ll_nodes[start] != ll_nodes[end]:
                return False
            start += 1
            end -= 1
        
        return True


Let's try to figure out ways to do this in O(1) space complexity

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        slow = head
        fast = head

        #find middle (slow)
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #reverse second half of linked list
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt

        #check palindrome
        start = head
        end = prev

        #checking if we reached the midpoint
        while end:
            if start.val != end.val:
                return False
            start = start.next
            end = end.next

        return True

