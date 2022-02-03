# 148. Sort List


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# -> simple linked list

class Solution(object):
    def merge(self, l, r):
        """
            l, r -> left, right
            search -> moving node / result -> pointer that saves search node's initial head(result.next)
            l, r에서 하나씩 비교하며 넣기. 반씩 나누기 때문에 결과적으로 남는 노드는 하나가 된다.
            남은 노드를 search.next에 할당하면 정렬된 search가 완성됨. 정렬된 linked list의 헤더는 result.next가 가리킴
        """
        if not l or not r: return l or r
        result = search = ListNode()
        while l and r: 
            if l.val < r.val:
                search.next, l = l, l.next
            else:
                search.next, r = r, r.next
            search = search.next
        search.next = l or r
        return result.next

    def sortList(self, head):
        """
            slow , fast로 linked list를 반으로 자른다. slow는 짝수일 경우 절반 직전, 홀수일 경우 절반의 바로 전 노드가 된다.
            절반의 시작점은 따라서 slow.next가 되고, 남은 slow의 링크를 끊기 위해 slow.next에 none을 할당해 준다.
            -> head, half는 각각 잘린 linked list가 되고, 이를 재귀적으로 sort-merge과정을 반복한다(merge sort)
        """
        if not (head or head.next): return head
        slow, fast = head, head.next

        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        
        half = slow.next
        slow.next = None
        l, r = self.sortList(head), self.sortList(half)
        return self.merge(l, r)
