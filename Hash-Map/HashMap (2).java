import java.util.*;
/*
Nipun Singh
ns2se@virgina.edu

Used seperate chaining to handle Key's that end up hashing into the same bucket. LinkedList was the datastructure used to handle the chains.
Used a load factor of 0.75 since empirically this gives the best peformance, and is what the standard HashMap uses in Java.

*/
public class HashMap
{
   private int size;
   private int initializedSize;
   private int itemsInHashMap;
   private LinkedList<Object[]>[] map;
   
   public HashMap(){}
   
   public HashMap(int size)
   {
      this.initializedSize = size;
      this.size = size*4/3; //load factor 0.75 because its optimal for space/time tradeoff
      itemsInHashMap = 0;
      map = new LinkedList[this.size];
   }
      
   public float load()
   {
      return (float) itemsInHashMap / size;
   }
   
   public boolean set(String key, Object value)
   {
      int bucket = Math.abs(key.hashCode() % size);
      
      if(map[bucket] == null)
      {
         if(itemsInHashMap >= initializedSize) //not enough space
            return false; 
         LinkedList valueList = new LinkedList();
         Object[] valuePair = {key, value};
         valueList.add(valuePair);
         map[bucket] = valueList;
      }
      
      else
      {
         LinkedList valueList = map[bucket];       
         Iterator iter = valueList.iterator();
         Object[] newValuePair = {key, value};
         
         while(iter.hasNext())
         {
            Object[] temp = (Object[]) iter.next();
            if(temp[0] == key) //value already in bucket
            {
               iter.remove(); 
               itemsInHashMap--;
               break;
            }  
         }
         if(itemsInHashMap >= initializedSize) //check if enough space
            return false; 
         valueList.add(newValuePair);
      }
      itemsInHashMap++;
      return true;   
   }
   
   public Object get(String key)
   {
      int bucket = Math.abs(key.hashCode() % size);

      if (map[bucket] != null)
      {
         LinkedList valueList = map[bucket];
         Iterator iter = valueList.iterator();
         while(iter.hasNext())
         {
            Object[] temp = (Object[]) iter.next();
            
            if(temp[0] == key)
               return temp[1];  
         }
      }
      
      return null;
   }
   
   public Object delete(String key)
   {
      int bucket = Math.abs(key.hashCode() % size);

      if (map[bucket] != null)
      {
         LinkedList valueList = map[bucket];
         Iterator iter = valueList.iterator();
         while(iter.hasNext())
         {
            Object[] temp = (Object[]) iter.next();
            
            if(temp[0] == key)
            {
               Object returnValue = temp[1];
               iter.remove();
               itemsInHashMap--;
               return returnValue;
            }
         }
      }
      return null;
   }
}