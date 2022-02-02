// Implementierung von Streuwerttabellen mit offener Adressierung.
public class HashTableOpenAddressing implements HashTable {
  private final HashSequence seq;
  private final Entry[] arr;
  
  // Streuwerttabelle mit Sondierungsfunktion s.
  public HashTableOpenAddressing(HashSequence seq) {
    this.seq = seq;
    this.arr = new Entry[seq.size()];
  }
  
  private HelperObj helperFunc(Object key){
    int ind = seq.first(key);
    int remembered = -1;
    
    for(int j = 0; j < seq.size(); j++){
      if(arr[ind] == null) return new HelperObj(remembered == -1?ind:remembered, HelperObj.nichtVorhanden);
      if(arr[ind].isDelMarker() && remembered == -1) remembered = ind;
      if(!arr[ind].isDelMarker() && arr[ind].getKey().equals(key)) return new HelperObj(ind, HelperObj.vorhanden);
      ind = seq.next();
    }
    
    if(remembered != -1) return new HelperObj(remembered, HelperObj.nichtVorhanden);
    return new HelperObj(-1, HelperObj.tabelleVoll);
  }
  
  @Override
  public boolean put(Object key, Object val) {
    if(key == null || val == null) return false;
    
    HelperObj h = helperFunc(key);
    if(h.status == HelperObj.tabelleVoll) return false;
    
    arr[h.index] = new Entry(false, key, val);
    return true;
  }
  
  @Override
  public Object get(Object key) {
    if(key == null) return null;
    
    HelperObj h = helperFunc(key);
    
    if(h.status == HelperObj.vorhanden){
      Entry entry = arr[h.index];
      return entry.getVal();
    }
    
    return null;
  }
  
  @Override
  public boolean remove(Object key) {
    if(key == null) return false;
    
    HelperObj h = helperFunc(key);
    if(h.status == HelperObj.nichtVorhanden || h.status == HelperObj.tabelleVoll) return false;
    arr[h.index] = new Entry(true, null, null);
    
    return true;
  }
  
  @Override
  public void dump() {
    for (int i = 0; i < arr.length; i++) {
      if (arr[i] != null && !arr[i].isDelMarker()) {
        Entry entry = arr[i];
        System.out.println(String.format("%d %s %s", i, entry.getKey(), entry.getVal()));
      }
    }
  }
  
  private static class HelperObj {
    static final int nichtVorhanden = -1;
    static final int vorhanden = 1;
    static final int tabelleVoll = 0;
    
    final int index;
    final int status;
  
    private HelperObj(int index, int status) {
      this.index = index;
      this.status = status;
    }
  }
  
  private static class Entry {
    private final boolean isDelMarker;
    private final Object key;
    private final Object val;
  
    private Entry(boolean isDelMarker, Object key, Object val) {
      this.isDelMarker = isDelMarker;
      this.key = key;
      this.val = val;
    }
  
    private boolean isDelMarker() {
      return isDelMarker;
    }
  
    private Object getVal() {
      return val;
    }
  
    private Object getKey() {
      return key;
    }
  }
}