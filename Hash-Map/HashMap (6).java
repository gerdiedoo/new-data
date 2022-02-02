package com.contactsunny.poc.HashMapImplementation.hashMap;

import com.contactsunny.poc.HashMapImplementation.exceptions.InvalidIndexException;

public class HashMap<K, V> {

    private static final int ARRAY_SIZE = 16;

    private Node<K, V>[] nodeList = new Node[ARRAY_SIZE];

    public void put(K key, V value) throws InvalidIndexException {

        long hashCode = this.getHashCode(key);
        int index = this.getIndex(hashCode);

        if (index > ARRAY_SIZE) {
            throw new InvalidIndexException("Invalid key, please check again!");
        }

        if (this.nodeList[index] != null) {
            Node<K, V> exitingNode = this.nodeList[index];

            while (exitingNode.getNext() != null) {
                exitingNode = exitingNode.getNext();
            }

            Node<K, V> newNode = new Node<>();
            newNode.setKey(key);
            newNode.setValue(value);
            newNode.setHashCode(hashCode);

            exitingNode.setNext(newNode);

        } else {
            Node<K, V> newNode = new Node<>();
            newNode.setKey(key);
            newNode.setValue(value);
            newNode.setHashCode(hashCode);

            this.nodeList[index] = newNode;
        }
    }

    private long getHashCode(K key) {

        String keyString = key.toString();
        return keyString.hashCode();
    }

    private int getIndex(long hashCode) {

        return Math.toIntExact(hashCode % ARRAY_SIZE);
    }

    public void printHashMap() {

        System.out.println("==============================================");
        System.out.println("Printing map:");

        int index = 0;

        while (index < ARRAY_SIZE) {

            Node<K, V> node = this.nodeList[index];

            if (node != null) {

                int listIndex = 0;

                while (node != null) {

                    if (listIndex > 0) {
                        System.out.print(" || ");
                    }

                    System.out.print(node.getKey().toString() + " -> ");
                    System.out.print(node.getValue().toString());

                    node = node.getNext();
                    listIndex++;

                }

                System.out.println("");
            }

            index++;
        }

        System.out.println("==============================================");
    }
}
