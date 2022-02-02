/***
 * 
 * Introduction-
 * The Map object holds key-value pairs and remembers the original insertion order of the keys. 
 * Any value (both objects and primitive values) may be used as either a key or a value. 
 *
 */

/***
 * 
 * Time Complexity
 * 
 * Name 	Insert 	Access 	Search 	Delete 	Comments
 * HashMap 	O(1) 	O(1) 	O(1) 	O(1) 	Rehashing might affect insertion time.
 * 
 */

/***
 * 
 * Example-
 * 
 * Keys         Values
 * 
 * 5c5ad            5
 * 5d6dn            11
 * 463gv            12
 * 
 */

//HashMap implementation in JS

class Hashmap {
    constructor() {
      this._storage = [];
    }
  
    hashStr(str) {
      let finalHash = 0;
      for (let i = 0; i < str.length; i++) {
        const charCode = str.charCodeAt(i);
        finalHash += charCode;
      }
      return finalHash;
    }
  
    set(key, val) {
      let idx = this.hashStr(key);
  
      if (!this._storage[idx]) {
        this._storage[idx] = [];
      }
  
      this._storage[idx].push([key, val]);
    }
  
    get(key) {
      let idx = this.hashStr(key);
  
      if (!this._storage[idx]) {
        return undefined;
      }
  
      for (let keyVal of this._storage[idx]) {
        if (keyVal[0] === key) {
          return keyVal[1];
        }
      }
    }
  }

const m = new Hashmap();
m.set('name', 'Jake');
console.log(m.get('name'));