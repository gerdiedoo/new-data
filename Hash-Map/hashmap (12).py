from linklist import LinkList


class HashMap:

    def __init__(self, size=100):
        self._entry_count = 0
        self._entry_load_limit = 1
        self._size = size
        self._buckets = [None] * self._size

    def _get_load_ratio(self):
        return self._entry_count / self._size

    def put(self, key, value):
        self._entry_count += 1
        if self._get_load_ratio() >= self._entry_load_limit:
            self._resize_bucket_list()
            self.put(key, value)
        else:
            bucket_index = self._calculate_bucket_index(key)
            if self._buckets[bucket_index] is None:
                self._buckets[bucket_index] = self._new_hash_entry(key, value)
            else:
                self._update_bucket_entries(bucket_index, key, value)

    def _resize_bucket_list(self):
        new_bucket_size = self._entry_count * 2
        new_bucket = [None] * new_bucket_size
        for entry_list in self._buckets:
            if entry_list is None:
                continue
            current_node = entry_list.first_node
            while current_node is not None:
                self._rehash_entries(current_node, new_bucket, new_bucket_size)
                current_node = current_node.next
        self._buckets = new_bucket
        self._size = new_bucket_size

    def _rehash_entries(self, current_node, new_bucket, new_buket_size):
        hash_key = hash(current_node.key)
        rehashed_index = hash_key % new_buket_size
        if new_bucket[rehashed_index] is None:
            new_bucket[rehashed_index] = self._new_hash_entry(current_node.key, current_node.value)
        else:
            self._update_bucket_entries(rehashed_index, current_node.key, current_node.value)

    def get(self, key):
        bucket_index = self._calculate_bucket_index(key)
        current_node = self._buckets[bucket_index].first_node
        while current_node.next is not None:
            current_node = current_node.next
        return current_node.value if current_node else None

    def _calculate_bucket_index(self, key):
        return hash(key) % self._size

    @staticmethod
    def _new_hash_entry(key, value):
        bucket_list = LinkList()
        bucket_list.add_node(key, value)
        return bucket_list

    def _update_bucket_entries(self, bucket_index, key, value):
        value_list = self._buckets[bucket_index]
        if value_list.contains_value(value):
            return
        else:
            value_list.add_node(key, value)

    def remove(self, key):
        bucket_index = self._calculate_bucket_index(key)
        current_link_list = self._buckets[bucket_index]
        current_link_list.delete_node_with_key(key)

    def size(self):
        return self._entry_count

    def clear(self):
        self.__init__()

    def contains(self, key):
        bucket_index = self._calculate_bucket_index(key)
        current_list = self._buckets[bucket_index]
        return current_list.contains_key(key)
