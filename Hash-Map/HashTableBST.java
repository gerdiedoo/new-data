public class HashTableBST<K extends Comparable<K>, V extends Comparable<V>> implements KWHashMap<K,V> {

    private BinaryTree<Entry<K,V>>[] table;
    private int numKeys;
    private static final int CAPACITY = 101;
    private static final double LOAD_THRESHOLD = 3.0;

    public HashTableBST(){
        table = new BinaryTree[CAPACITY];
    }

    /**
     * This method gets key and returns the value according to key.
     * @param key key
     * @return value of element
     */
    @Override
    public V get(Object key) {

        int index = key.hashCode() % table.length;
        if(index<0){
            index += table.length;
        }
        if(table[index] == null){
            return null;
        }
        K k = (K) key;
        Entry<K,V> val = table[index].getSearch(new Entry<>(k,null));

        return val.getValue();
    }

    /**
     * @return true if table empty
     */
    @Override
    public boolean isEmpty() {
        return table.length ==0;
    }

    /**
     * This method insert new element into the table.
     * @param key of new element
     * @param value of element
     * @return null if element already exist in table.
     */
    @Override
    public V put(K key, V value) {
        int index = key.hashCode() % table.length;
        if(index<0){
            index += table.length;
        }
        if(table[index] == null){
            table[index] = new BinaryTree<>();
        }

        boolean flag = table[index].searchKey(new Entry<>(key,value));

        if(!flag){
            table[index].insert(new Entry<>(key,value));
            numKeys++;
            if(numKeys >(LOAD_THRESHOLD*table.length))
                rehash();
        }


        return null;
    }

    /**
     * this method creates new table and takes element from old table for new table.
     */
    private void rehash(){
        BinaryTree<Entry<K,V>> [] oldTable = table;
        table = new BinaryTree[2*oldTable.length+1];

        numKeys = 0;
        for(int i=0; i<oldTable.length ; i++){
            if((oldTable[i] != null) ){
                table[i] = oldTable[i];
            }
        }

    }


    /**
     * This method removes the object according to key
     * @param key key
     * @return removed object value.
     */
    @Override
    public V remove(Object key) {

        int index = key.hashCode() % table.length;
        if(index<0){
            index += index +table.length;
        }

        if(table[index] == null){
            return null;
        }

        K k = (K) key;
        Entry<K,V> val = table[index].deleteSearch(new Entry<>(k,null));


        return val.getValue();
    }


    /**
     * @return table size
     */
    @Override
    public int size() {
        return table.length;
    }

    /**
     * Inner class
     * @param <K> generic type
     * @param <V> generic type
     */
    static class Entry<K extends Comparable<K>,V extends Comparable<V>> implements Comparable<Entry<K,V>>  {

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

        /**
         * This method compares 2 Entry object according to key .
         * @param o 2nd object
         * @return 0 , 1 or -1.
         */
        @Override
        public int compareTo(Entry<K, V> o) {
            return this.key.compareTo(o.getKey());
        }
    }





}
