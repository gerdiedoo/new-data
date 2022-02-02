/**
 *
 * @author moham
 */

public class HashTableLin {
    public Integer[] table;
    private int maxLoad, size, load;
    private double loadFactor;
    public int probeCount = 0;
    
    public HashTableLin(int maxLoad, double load){
        this.maxLoad = maxLoad;
        this.loadFactor = load;
        
        int minSize = (int) (maxLoad/load);
        
        while(this.isPrime(minSize) == false){
            minSize++;
        }
        
        table = new Integer[minSize];
        
        this.size = minSize;
        this.load = 0;
    }
    
    
    public void insert(int n){
        
        int hashIndex = n % this.size;
        
        if((this.load +1) > this.maxLoad){
            this.rehash();
            this.insert(n);
        }
        else{
            load++;
            
            while(this.table[hashIndex] != null){
                probeCount++;
                
                //we check if the number is already in the table
                if(this.table[hashIndex] == n){
                    return;
                }
                
                //linear probing
                if(hashIndex < (this.size-1)){
                    hashIndex++;
                }
                else{
                    hashIndex = 0;
                }
            }
            
            this.table[hashIndex] = n;
        }
    }
    
    public void rehash(){
        HashTableLin temp; //this will be used to create a larger hash table
        
        temp = new HashTableLin((this.size * 2), this.loadFactor);
        
        for(int i=0; i<this.size; i++){
            if(this.table[i] != null){
                temp.insert(this.table[i]);
            }
        }
        
        //making this equal temp.
        this.table = temp.table;
        this.maxLoad = temp.maxLoad;
        this.size = temp.size;
        this.load = temp.load;
    }
    
    public boolean isIn(int n){
        int hashIndex = n % this.size;
        
        while(this.table[hashIndex] != null){
            //we check if the number is in the table
            if(this.table[hashIndex] == n){
                return true;
            }

            //linear probing
            if(hashIndex < (this.size-1)){
                hashIndex++;
            }
            else{
                hashIndex = 0;
            }
        }
        
        return false;
    }
    
    public void printKeys(){
        for(int i=0; i<this.size; i++){
            if(this.table[i] != null){
                System.out.println(this.table[i]);
            }
        }
    }
    
    public void printKeysAndIndexes(){
        System.out.println("Key ==> Index");
        for(int i=0; i<this.size; i++){
            if(this.table[i] != null){
                System.out.println(this.table[i] + " ==> " + i);
            }
        }
    }
    
    public int getMaxLoad(){
        return this.maxLoad;
    }
    
    public int getNumOfKeys(){
        return this.load;
    }
    
    public int getTableSize(){
        return this.size;
    }
    
    public double getLoadFactor(){
        return this.loadFactor;
    }
    
    
    private boolean isPrime(int num){
        int tracker = 0;
        
        for(int i=2; i<(Math.sqrt(num)); i++){
            if(num%i == 0){
                tracker++;
            }
        }
        
        if(tracker == 0) return true;
        else return false;
    }
}
