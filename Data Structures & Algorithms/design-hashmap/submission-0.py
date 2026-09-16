class ListNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:

    def __init__(self):
        self.map = [ListNode(-1, -1) for _ in range(10**4)]

    def put(self, key: int, value: int) -> None:
        curr = self.map[key % 10**4]

        while curr.next:
            if key == curr.next.key:
                curr.next.val = value
                return

            curr = curr.next

        curr.next = ListNode(key, value)

    def get(self, key: int) -> int:
        curr = self.map[key % 10**4]

        while curr.next:
            if key == curr.next.key:
                return curr.next.val
            curr = curr.next

        return -1

    def remove(self, key: int) -> None:
        curr = self.map[key % 10**4]

        while curr.next:
            if curr.next and curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)