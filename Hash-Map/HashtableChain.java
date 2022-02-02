import java.nio.IntBuffer;
import java.util.LinkedList;

public class HashtableChain<K extends Comparable<K>, V extends Comparable<V>> implements KWHashMap<K, V> {
    // Insert inner class Entry<K, V> here.
    /** The table */
    private LinkedList<Entry<K, V>>[] table;
    /** The number of keys */
    private int numKeys;
    /** The capacity */
    private static final int CAPACITY = 400000;
    /** The maximum load factor */
    private static final double LOAD_THRESHOLD = 3.0;
    // Constructor
    public HashtableChain() {
        table = new LinkedList[CAPACITY];
    }

    /** Method get for class HashtableChain.
     @param key The key being sought
     @return The value associated with this key if found;
     otherwise, null
     */
    @Override
    public V get(Object key) {
        int index = key.hashCode() % table.length;
        if (index < 0)
            index += table.length;
        if (table[index] == null)
            return null; // key is not in the table.
        // Search the list at table[index] to find the key.
        for (Entry<K, V> nextItem : table[index]) {
            if (nextItem.getKey().equals(key))
                return nextItem.getValue();
        }
        // assert: key is not in the table.
        return null;
    }

    /**
     * @return true if table is empty
     */
    @Override
    public boolean isEmpty() {
        return size()==0;
    }

    /** Method put for class HashtableChain.
     table and numKeys is incremented. If the key is already
     in the table, its value is changed to the argument
     value and numKeys is not changed.
     @param key The key of item being inserted
     @param value The value for this key
     @return The old value associated with this key if
     found; otherwise, null
     */
    @Override
    public V put(K key, V value) {
        int index = key.hashCode() % table.length;
        if (index < 0)
            index += table.length;
        if (table[index] == null) {
        // Create a new linked list at table[index].
            table[index] = new LinkedList<>();
        }
        // Search the list at table[index] to find the key.
        for (Entry<K, V> nextItem : table[index]) {
            // If the search is successful, replace the old value.
            if (nextItem.getKey().equals(key)) {
                // Replace value for this key.
                V oldVal = nextItem.getValue();
                nextItem.setValue(value);
                return oldVal;
            }
        }
        // assert: key is not in the table, add new item.
        table[index].addFirst(new Entry<>(key, value));
        numKeys++;
        if (numKeys > (LOAD_THRESHOLD * table.length))
            rehash();
        return null;
    }

    /**
     * Rehash method.
     */
    private void rehash() {
        // Save a reference to oldTable.
        LinkedList<Entry<K, V>>[] oldTable = table;
        // Double capacity of this table.
        table = new LinkedList[(CAPACITY *2) +1];
        // Reinsert all items in oldTable into expanded table.
        numKeys = 0;
        for (int i = 0; i < oldTable.length; i++) {
            if ((oldTable[i] != null)) {
                // Insert entry in expanded table
                table[i].addAll(oldTable[i]);
            }
        }
    }

    /**
     * Removes element from table
     * @param key removed element
     * @return null if element is not in the table . If element is in the table  , it returns value of element.
     */
    @Override
    public V remove(Object key) {
        int index = key.hashCode() % table.length;
        if(index<0){
            index += table.length;
        }
        if (table[index] == null){
            return null;
        }

        for (Entry<K, V> nextItem : table[index]) {
            // If the search is successful, replace the old value.
            if (nextItem.getKey().equals(key)) {
                // Replace value for this key.
                V oldVal = nextItem.getValue();
                nextItem.setValue(null);
                return oldVal;
            }
        }

        return null;
    }

    /**
     * @return size of table.
     */
    @Override
    public int size() {
        return table.length;
    }
    private static class Entry<K extends Comparable<K>,V extends Comparable<V>> implements Comparable<Entry<K,V>>  {

        private final K key;
        private V value;
        public boolean inTable;

        public boolean isInTable() {
            return inTable;
        }

        public K getKey() {
            return key;
        }

        public V getValue() {
            return value;
        }

        public void setValue(V value) {
            this.value = value;
        }

        public Entry(K key , V value){
            this.key = key;
            this.value = value;
            inTable = true;
        }

        @Override
        public int compareTo(Entry<K, V> o) {
            return this.key.compareTo(o.getKey());
        }
    }
}
