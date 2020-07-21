"""
146. LRU缓存机制
运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制。它应该支持以下操作： 获取数据 get 和 写入数据 put 。

获取数据 get(key) - 如果关键字 (key) 存在于缓存中，则获取关键字的值（总是正数），否则返回 -1。
写入数据 put(key, value) - 如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字/值」。当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。

进阶:
你是否可以在 O(1) 时间复杂度内完成这两种操作？

示例:

LRUCache cache = new LRUCache( 2 /* 缓存容量 */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // 返回  1
cache.put(3, 3);    // 该操作会使得关键字 2 作废
cache.get(2);       // 返回 -1 (未找到)
cache.put(4, 4);    // 该操作会使得关键字 1 作废
cache.get(1);       // 返回 -1 (未找到)
cache.get(3);       // 返回  3
cache.get(4);       // 返回  4
"""


# 定义双向链表的节点
class DoubleLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value

        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.head = DoubleLinkedNode()
        self.tail = DoubleLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        # 如果在哈希表中，return，并且移至链表头部
        if key in self.cache:
            node = self.cache[key]
            self.moveToHead(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # 如果存在，先通过哈希表定位，再修改 value，并且移至链表头部
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)
        # 如果不存在，加入哈希表，并且添加至链表头部。 如果已经超出容量，那么要删除链表尾部数据
        else:
            node = DoubleLinkedNode(key, value)
            self.cache[key] = node
            self.size += 1
            self.addToHead(node)

            if self.size > self.capacity:
                tail = self.removeTail()
                self.cache.pop(tail.key)
                self.size -= 1

    # 添加至头部
    def addToHead(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    # 移动至头部的其中一步，要把原来那个点删了
    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    # 移动至头部
    def moveToHead(self, node):
        self.removeNode(node)
        self.addToHead(node)

    # size超出容量
    def removeTail(self):  # 需要return，因为哈希表也要更新
        node = self.tail.prev
        self.removeNode(node)
        return node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
