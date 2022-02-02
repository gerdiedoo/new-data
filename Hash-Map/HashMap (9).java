

/**
 * - Introduction to HashMap
 * 
 * There is a native implementation of HashMap since Java 1.2 (1998)
 * Hash table based implementation of the Map interface.
 * This implementation provides all of the optional map operations, and permits
 * null values and the null key.
 * The HashMap class is roughly equivalent to Hashtable, except that it is
 * unsynchronized and permits nulls.
 * This class makes no guarantees as to the order of the map; in particular, it
 * does not guarantee that the order will remain constant over time.
 * 
 * Source:
 * https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/HashMap.html
 * 
 * - Complexity Analysis of Worst-Case + Best Case
 * 
 * The principal idea is that once the number of items in a hash bucket grows
 * beyond a certain threshold, that bucket will switch from using a linked list
 * of entries to a balanced tree.
 * In the case of high hash collisions, this will improve worst-case performance
 * from O(n) to O(log n).
 * 
 * Source: http://openjdk.java.net/jeps/180
 * 
 */
public class HashMap {

    public static void main(String[] args) {

        // a hashmap can use any type for key and value, let's try to use integer number
        // for key and String for value
        java.util.HashMap<Integer, String> hashMapOfString = new java.util.HashMap<Integer, String>();

        // Let store a hash map like this:
        // 1 -> number one
        // 2 -> number two
        // 3 -> number three

        hashMapOfString.put(1, "number one");
        hashMapOfString.put(2, "number two");
        hashMapOfString.put(3, "number three");

        // let's print
        System.out.println(hashMapOfString);
        // {1=number one, 2=number two, 3=number three}

        // let's update 3
        hashMapOfString.put(3, "number threeeeee");

        // let's print again
        System.out.println(hashMapOfString);
        // {1=number one, 2=number two, 3=number threeeeee}

        // let's remove the first one
        hashMapOfString.remove(1);

        // let's print again
        System.out.println(hashMapOfString);
        // {2=number two, 3=number threeeeee}

        // let's print key 2
        System.out.println("2 -> " + hashMapOfString.get(2));
        // 2 -> number two

    }
}