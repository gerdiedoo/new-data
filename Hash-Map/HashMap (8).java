package com.halilcanm;

public class HashMap<K,V> {

    private Entry<K,V>[] table;
    private int size = 16; //default size

    static class Entry<K, V> {
        K key;
        V value;
        Entry <K, V> next;

        public Entry(K key, V value, Entry<K,V> next) {
            this.key = key;
            this.value = value;
            this.next = next;
        }
    }

    public HashMap(int initSize) {
        this.size = initSize;

        table = new Entry[size];
    }

    private int hashKey (K key) {
        return Math.abs(key.hashCode()) % size;
    }

    public boolean set (K key, V value) {
        if (key == null) {
            return false;
        }

        int hash = hashKey(key);
        Entry<K,V> newEntry = new Entry<K,V>(key, value, null);

        if(table[hash] == null) {
            table[hash] = newEntry;
        } else {
            Entry<K,V> previous = null;
            Entry<K,V> current = table[hash];

            while(current != null) {
                if (current.key.equals(key)) {
                    if(previous == null) {
                        newEntry.next = current.next;
                        table[hash] = newEntry;
                        return true;
                    } else {
                        newEntry.next = current.next;
                        previous.next = newEntry;
                        return true;
                    }
                }
                previous = current;
                current = previous.next;
            }
            previous.next = newEntry;
        }
        return false;
    }

    public V get(K key){
        int hash = hashKey(key);
        if(table[hash] == null) {
            return null;
        } else {
            Entry<K,V> scroll = table[hash];
            while(scroll != null) {
                if(scroll.key.equals(key)) {
                    return scroll.value;
                }
                scroll = scroll.next;
            }
            return null;
        }
    }

    public boolean delete(K key) {
        int hash = hashKey(key);

        if (table[hash] == null) {
            return false;
        } else {
            Entry<K,V> previous = null;
            Entry<K,V> current = table[hash];

            while (current != null) {
                if (current.key.equals(key)) {
                    if (previous == null) {
                        table[hash] = table[hash].next;
                        return true;
                    } else {
                        previous.next = current.next;
                        return true;
                    }
                }
            }
        }
        return false;
    }

    public float load() {
        float totalSize = (float)size;
        float fullBuckets = 0f;

        for (int i = 0; i < size; i++) {
            if (table[i] != null) {
                fullBuckets += 1.0f;
            }
        }
        return fullBuckets/totalSize;
    }

    public void quickDraw() {
        for (int i = 0; i < size; i++) {
            System.out.print(" Bucket# = " + i + " ");
            if (table[i] != null) {
                Entry<K,V> previous = null;
                Entry<K,V> current = table[i];
                while (current != null) {
                    System.out.print("-{" + current.key + "=" + current.value + "}");
                    previous = current;
                    current = current.next;
                }
            }
            System.out.println();
        }
        System.out.println();
        System.out.println("Note: The implementation accepts any primitive data type for both K or V");
    }
}
