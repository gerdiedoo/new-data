import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

/**
 * A class representing a hash map with linear probing collision handling.
 *
 * @author Christopher Tam
 *
 * @param <K>
 *            the type for the key of entries.
 * @param <V>
 *            the type for the value of entries.
 */
public class HashMap<K, V> implements HashMapInterface<K, V> {

    // Do not make any new instance variables.
    private MapEntry<K, V>[] table;
    private int size;

    public HashMap() {
        clear();
    }

    @Override
    public V add(K key, V value) {
        if (key == null || value == null) {
            throw new IllegalArgumentException("Argument cannot be null.");
        }
        if (this.getNextLoadFactor() > MAX_LOAD_FACTOR) {
            resize();
        }
        int index = this.getAddIndex(key);
        MapEntry<K, V> entry = this.table[index];
        V result = null;
        if (entry == null) {
            this.table[index] = new MapEntry<K, V>(key, value);
        } else if (entry.getKey().equals(key)) {
            if (!entry.isRemoved()) {
                result = entry.getValue();
            }
            entry.setValue(value);
            entry.setRemoved(false);
        } else {
            entry.setKey(key);
            entry.setValue(value);
            entry.setRemoved(false);
        }
        if (result == null) {
            size++;
        }
        return result;
    }

    @Override
    public V remove(K key) {
        if (key == null) {
            throw new IllegalArgumentException("Argument cannot be null.");
        }
        int index = this.getAddIndex(key);
        MapEntry<K, V> entry = this.table[index];
        if (entry != null && entry.getKey().equals(key) && !entry.isRemoved()) {
            entry.setRemoved(true);
            size--;
            return entry.getValue();
        }

        return null;
    }

    @Override
    public V get(K key) {
        if (key == null) {
            throw new IllegalArgumentException("Argument cannot be null.");
        }
        int index = this.getAddIndex(key);
        MapEntry<K, V> entry = this.table[index];
        return (entry != null && !entry.isRemoved()
                && entry.getKey().equals(key) ? entry.getValue() : null);
    }

    @Override
    public boolean contains(K key) {
        return get(key) != null;
    }

    @SuppressWarnings("unchecked")
    @Override
    public void clear() {
        this.table = (MapEntry<K, V>[]) new MapEntry[STARTING_SIZE];
        this.size = 0;
    }

    @Override
    public int size() {
        return this.size;
    }

    @Override
    public Set<K> keySet() {
        HashSet<K> result = new HashSet<K>(size);
        for (int i = 0; i < this.table.length; i++) {
            MapEntry<K, V> entry = this.table[i];
            if (entry != null && !entry.isRemoved()) {
                result.add(entry.getKey());
            }
        }
        return result;
    }

    @Override
    public List<V> values() {
        ArrayList<V> result = new ArrayList<V>(size);
        for (int i = 0; i < this.table.length; i++) {
            MapEntry<K, V> entry = this.table[i];
            if (entry != null && !entry.isRemoved()) {
                result.add(entry.getValue());
            }
        }
        return result;
    }

    /**
     * Calculates the load factor if another element is added the HashMap.
     *
     * @return Returns the load factor.
     */
    private double getNextLoadFactor() {
        return (double) (size + 1) / (double) this.table.length;
    }

    /**
     * Doubles the size of the HashMap and inserts the elements into the new
     */
    @SuppressWarnings("unchecked")
    private void resize() {
        MapEntry<K, V>[] temp = this.table;
        this.table = (MapEntry<K, V>[]) new MapEntry[temp.length * 2];
        this.size = 0;
        for (int i = 0; i < temp.length; i++) {
            MapEntry<K, V> entry = temp[i];
            if (entry != null && !entry.isRemoved()) {
                this.add(entry.getKey(), entry.getValue());
            }
        }
    }

    /**
     * Gets the index of a given array-backed HashMap to add the given key.
     *
     * @param key
     *            The key to add.
     * @return Returns the index to add to.
     */
    private int getAddIndex(K key) {
        int index = Math.abs(key.hashCode()) % this.table.length;

        MapEntry<K, V> curEntry = this.table[index];
        int firstRemoved = -1;
        int curIndex = index;
        boolean looped = false;

        while (curEntry != null && !curEntry.getKey().equals(key)
                && (!looped || curIndex != index)) {
            if (firstRemoved == -1 && curEntry.isRemoved()) {
                // Record first removed
                firstRemoved = index;
            }

            if (++curIndex >= this.table.length) {
                // Loop back around to the first of the table
                curIndex = 0;
                looped = true;
            }

            curEntry = this.table[curIndex];
        }
        if (curEntry != null && curEntry.getKey().equals(key)) {
            return curIndex;
        } else {
            return (firstRemoved == -1 ? curIndex : firstRemoved);
        }
    }
}
