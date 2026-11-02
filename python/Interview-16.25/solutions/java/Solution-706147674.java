// leetcode.cn/problems/lru-cache-lcci/  (面试题 16.25)
// submission 706147674  accepted 2026-03-12  runtime 19 ms  memory 58 MB

class LRUCache {

    private final int capacity;
    private final Map<Integer, CacheNode> map;
    private final CacheNode head, tail;

    public LRUCache(int capacity) {
        this.capacity = capacity;
        this.map = new HashMap<>();
        head = new CacheNode(0, 0);
        tail = new CacheNode(0, 0);
        head.next = tail;
        tail.prev = head;
    }

    

    public int get(int key) {
        CacheNode node = map.get(key);
        if (node == null) return -1;
        unlink(node);
        addToHead(node);
        return node.val;
    }

    public void put(int key, int value) {
        CacheNode node = map.get(key);
        if (node != null) {
            node.val = value;
            unlink(node);
            addToHead(node);
            return;
        }
        CacheNode newNode = new CacheNode(key, value);
        map.put(key, newNode);
        addToHead(newNode);

        if (map.size() > capacity) {
            CacheNode removed = removeFromTail();
            map.remove(removed.key);
        }
    }

    private void unlink(CacheNode node) {
        node.prev.next = node.next;
        node.next.prev = node.prev;
        node.prev = null;
        node.next = null;
    }

    private void addToHead(CacheNode node) {
        node.next = head.next;
        node.prev = head;

        head.next = node;
        node.next.prev = node;
    }

    private CacheNode removeFromTail() {
        CacheNode node = tail.prev;
        unlink(node);
        return node;
    }

    private class CacheNode {
        public int key;
        public int val;
        public CacheNode prev;
        public CacheNode next;

        public CacheNode(int key, int val) {
            this.key = key;
            this.val = val;
        }
    }

}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */
