// Implementierung von Streuwerttabellen mit Verkettung.
class HashTableChaining implements HashTable {
  private final ChainedList[] arr;
  private final HashFunction func;
  
  // Streuwerttabelle mit Streuwertfunktion f.
  public HashTableChaining(HashFunction f) {
    arr = new ChainedList[f.size()];
    func = f;
  }
  
  @Override
  public boolean put(Object key, Object val) {
    if (key == null || val == null) return false;
    
    int i = func.compute(key);
    
    //Falls an der Stelle im Array noch keine Liste ist wird diese ertsellt und key, val als erstes Objekt eingefügt
    if (arr[i] == null) {
      arr[i] = new ChainedList(key, val);
      return true;
    }
    
    ChainedList.ListElement searchRes = arr[i].search(key);
    
    //Falls key noch nicht enthalten ist wird key, val hinzugefügt
    if (searchRes == null) {
      arr[i].add(key, val);
      return true;
    }
    
    //Falls key schon vorhanden ist wird val überschrieben
    searchRes.setVal(val);
    return true;
  }
  
  @Override
  public Object get(Object key) {
    if (key == null) return null;
    
    int i = func.compute(key);
    
    //Falls an der Stelle i keine Liste steht, ist key nicht in der HashMap
    if (arr[i] == null) return null;
    //Falls an der Stelle i eine Liste ist, aber key nicht in der Liste ist, ist key auch nicht in der HashMap
    if (arr[i].search(key) == null) return null;
    
    //Falls keine vorhergegangene Bedingung korrekt war, muss key in der HashMap sein. Also wird val ausgegeben
    return arr[i].search(key).getVal();
  }
  
  @Override
  public boolean remove(Object key) {
    if (key == null) return false;
    
    int i = func.compute(key);
    
    //Falls an der Stelle i keine Liste steht, ist key nicht in der HashMap
    if (arr[i] == null) return false;
    
    //Ansonsten wird remove auf der Liste aufgerufen, falls key nicht in der Liste ist gibt remove(key) aus der Liste false zurück.
    //Falls key in der Liste ist wird true zurückgegeben und der Eintrag gelöscht
    return arr[i].remove(key);
  }
  
  @Override
  public void dump() {
    StringBuilder out = new StringBuilder();
    for (int i = 0; i < arr.length; i++) {
      if (arr[i] != null) {
        out.append(arr[i].dump(i));
      }
    }
    System.out.print(out);
  }
  
  private static class ChainedList {
    private ListElement first;
  
    private ChainedList(Object firstKey, Object firstVal) {
      this.first = new ListElement(null, firstKey, firstVal);
    }
  
    private void add(Object key, Object val) {
      first = new ListElement(first, key, val);
    }
  
    private boolean remove(Object key) {
      if (first == null) return false;
      
      if (first.key.equals(key)) {
        first = first.next;
        return true;
      }
      
      ListElement prevKeyElem = first;
      while (prevKeyElem.next != null && !prevKeyElem.next.key.equals(key)) {
        prevKeyElem = prevKeyElem.next;
      }
      
      if (prevKeyElem.next == null) return false;
      
      prevKeyElem.next = prevKeyElem.next.next;
      return true;
    }
  
    private ListElement search(Object key) {
      if (first == null) return null;
      return first.search(key);
    }
  
    private String dump(int index) {
      if (first == null) return "";
      return first.dump(index);
    }
    
    private static class ListElement {
      private ListElement next;
      private final Object key;
      private Object val;
      
      private ListElement(ListElement next, Object key, Object val) {
        this.next = next;
        this.key = key;
        this.val = val;
      }
  
      private void setVal(Object val) {
        this.val = val;
      }
  
      private Object getVal() {
        return val;
      }
  
      private ListElement search(Object key) {
        if (this.key.equals(key)) {
          return this;
        }
        if (next == null) return null;
        return next.search(key);
      }
  
      private String dump(int index) {
        String out = String.format("%d %s %s\n", index, key, val);
        if (next == null) return out;
        return out += next.dump(index);
      }
    }
  }
}