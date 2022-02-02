public class HashMap<K, V> {

    private List<Pair<K, V>>[] values;
    private int numberOfValues;

    public HashMap() {
        this.values = new List[32];
        this.numberOfValues = 0;
    }

    /**
     * @param key
     * @param value
     * @return adds a new key-value pair into the HashMap. If the key already exists, its old value get replaced by a new.
     */
    public void add(K key, V value) {
        List<Pair<K, V>> valuePairList = getValuePairList(key);
        int index = findIndexByKey(valuePairList, key);

        if (index < 0) {
            valuePairList.add(new Pair<>(key, value));
            this.numberOfValues++;
        } else {
            valuePairList.get(index).setValue(value);
        }

        // If more than 75% of index's are being utilized, create a new, double the size of a list
        if (1.0 * this.numberOfValues / this.values.length > 0.75) {
            doubleArraySize();
        }
    }


    /**
     * @param key
     * @return returns a value of a key-value pair. Returns 'null', if the value doesn't exist.
     */
    public V get(K key) {
        int hash = Math.abs(key.hashCode() % this.values.length);
        if (this.values[hash] == null) {
            return null;
        }

        List<Pair<K, V>> valuePairsList = this.values[hash];

        for (int i = 0; i < valuePairsList.size(); i++) {
            if (valuePairsList.get(i).getKey().equals(key)) {
                return valuePairsList.get(i).getValue();
            }
        }

        return null;
    }

    /**
     * @param key
     * @return removes a value-pair from the array by its key. Returns removed value if successful, otherwise returns a null.
     */
    public V remove(K key) {
        List<Pair<K, V>> values = getValuePairList(key);
        if (values.size() == 0) {
            return null;
        }

        int index = findIndexByKey(values, key);
        if (index < 0) {
            return null;
        }

        Pair<K, V> pair = values.get(index);
        values.remove(pair);
        return pair.getValue();
    }

    private void doubleArraySize() {
        List<Pair<K, V>>[] temp = new List[this.values.length * 2];

        for (int i = 0; i < this.values.length; i++) {
            copyValues(temp, i);
        }

        this.values = temp;
    }

    private void copyValues(List<Pair<K, V>>[] temp, int fromIndex) {
        for (int i = 0; i < this.values[fromIndex].size(); i++) {
            Pair<K, V> value = this.values[fromIndex].get(i);

            // new hash required for even distribution of values
            int hash = Math.abs(value.getKey().hashCode() % temp.length);
            if (temp[hash] == null) {
                temp[hash] = new List<>();
            }

            temp[hash].add(value);
        }
    }

    private List<Pair<K, V>> getValuePairList(K key) {
        int hash = Math.abs(key.hashCode() % this.values.length);
        if (this.values[hash] == null) {
            this.values[hash] = new List<>();
        }

        return this.values[hash];
    }

    private int findIndexByKey(List<Pair<K, V>> list, K key) {
        for (int i = 0; i < list.size(); i++) {
            if (list.get(i).getKey().equals(key)) {
                return i;
            }
        }

        return -1;
    }
}
