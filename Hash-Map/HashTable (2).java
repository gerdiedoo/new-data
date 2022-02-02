import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.Arrays;

public class HashTable extends Hashable implements Table {
	private HashBucket[] table;
	private int depth, size;
	
	public HashTable() {
		this.depth = initialDepth;
		this.size = 1<<depth;
		this.table = new HashBucket[size];
	}

	@Override
	public void insert(String word) {
		word = word.toLowerCase(); // So that Ali and ali will be same or Mehmet and mehmet, all of them were made small letter. 
		this.insert(word, 1);
	}
	
	private void insert(String word, int count) { // delete that word how many count there are
		int key = hash(word)%size;
		if(table[key] == null) { // create new bucket if where it will come is empty
			table[key] = new HashBucket();
		}
		if(table[key].isFull()) { // if it is empty
			if(this.depth - table[key].getDepth() == 0) { // when global and local depth is equal, global table will grow up
				doublingSize();
				insert(word, count);
			}else if(this.depth - table[key].getDepth() > 0) { // if global depth is greater than local depth, local words needs to be distributed again
				int localKey = key % (1<<table[key].getDepth()); // according to local depth
				int depthDifference = this.depth - table[key].getDepth(); // difference between depths
				table[key].incrementDepth(); // first, increases its depth
				HashBucket newBucket = new HashBucket(table[key].getDepth()); // then, created the new bucket to be distributed
				// now, we got two buckets, one is table[key], the other is new bucket
				
				// we need to distribute all elements inside table[key] and the word which arrived yet.
				for (int i = localKey; i < size; i+=(size>>depthDifference)) { //now, we got indexes more than one to show table[key]
					if(i%(1<<table[key].getDepth()) != key%(1<<table[key].getDepth())) { // this indexes are evaluated according to word which came yet, if they are not same, the bucket which is created newly, has tobe showed 
						table[i] = newBucket;
					}
				}
				table[key].transfer(newBucket, key); // last, the words exist in the bucket[key] but not in newBucket will be transfered
				insert(word, count); // and new one is added, now buckets will be added directly, because they are not full 
			}else {
				System.out.println("Error #1\nLocal depth is higher than global depth!");
			}
		}else {
			table[key].insert(word, count);
		}
	}

	@Override
	public boolean search(String word) {
		word = word.toLowerCase(); // first, letters will be make small
		int key = hash(word)%size;
		HashBucket bucket = table[key];
		if(table[key] == null) { // if where it will come is empty word already doesnt' exist
			System.out.println(word + " bulunamadý.");
			return false;  
		}
		WordNode node = bucket.find(word);
		if(node == null) { // if it's not in the bucket,it must be in
			System.out.println(word + " bulunamadý.");
			return false; 
		}
		bucket.print(node);
		System.out.println("Global Depth: " + depth);
		System.out.println();
		return true;
	}

	@Override
	public void loadFromFile(String fileName)  {
		BufferedReader br = null;
		FileReader fr = null;
		try {
			fr = new FileReader(fileName);
			br = new BufferedReader(fr);
			
			String sCurrentLine;
			while ((sCurrentLine = br.readLine()) != null) {
				sCurrentLine = sCurrentLine.trim();
				String words[] = sCurrentLine.split(" ");
				for(String word:words) {
					word = word.trim();
					if(word.equals("")) continue;
					insert(word);
				}
			}
		} catch (FileNotFoundException e) { // if file could not be found
			e.printStackTrace();
		} catch (IOException e) { // if buffered reader cannot read the file
			e.printStackTrace();
		}
	}
	
	private void doublingSize() { // increases depth, doubles table size
		int size = 1<<depth;
		this.depth++;
		this.table = Arrays.copyOf(table, size*2); // ready java function, doubles size by protecting the data in the table
		for (int i = 0; i < size; i++) { // match the fields that occurs new with old ones
			table[size+i] = table[i];
		}
		this.size = 1<<depth;
	}
	
	public int getDepth() {
		return depth;
	}
	
	public void print() {
		System.out.println("----------Extendible Hashing----------");
		System.out.println("Global Depth: " + depth);
		for (int i = 0; i < size; i++) {
			if(table[i] != null) {
				System.out.println("");
				table[i].print();
			}
		}
	}

}