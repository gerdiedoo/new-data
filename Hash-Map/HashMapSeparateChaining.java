package cassandratest;

public class HashMapSeparateChaining<Key, Value>
{
	private static final int INIT_BUCKETS_SIZE = 888;
	private int capacity;
	private int chains; // no. of buckets
	private Node[] ht;
	
	// helper linked list data type
	private static class Node
	{
		private Object key;
		private Object val;
		private Node next;
		
		public Node(Object key, Object val, Node next)
		{
			this.key = key;
			this.val = val;
			this.next = next;
		}
	}
	
	// initiaiate separate chaining hash map
	public HashMapSeparateChaining()
	{
		this(INIT_BUCKETS_SIZE);
	}

	public HashMapSeparateChaining(int chains)
	{
		this.chains = chains;
		ht = new Node[chains];
	}

	// generate hash value
	private int hash(Key key)
	{
		int hash = 0;
		for (int i = 0; i < key.toString().length(); i++)
		{
			hash = hash + (int) key.toString().charAt(i);
		}
		hash %= INIT_BUCKETS_SIZE;
//		System.out.println("hash(" + key + ") = " + hash);
		return hash;		
	}

	@SuppressWarnings("unchecked")
	public Value get(Key key)
	{
		int h = hash(key);
//		System.out.println("hash(" + key + ") = " + h);
		for (Node x = ht[h]; x != null; x = x.next)
		{
			if (key.equals(x.key)) 
			{
				return (Value) x.val;
			}
		}
		return null;
	}

	public void put(Key key, Value val)
	{
		int h = hash(key);
//		System.out.println("hash(" + key + ") = " + h);
		for (Node x = ht[h]; x != null; x = x.next)
		{
			if (key.equals(x.key))
			{
				x.val = val;
				return;
			}
		}
		capacity++;
		ht[h] = new Node(key, val, ht[h]);
	}	
}
		
