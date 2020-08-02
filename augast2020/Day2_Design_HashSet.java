import java.util.*;
class MyHashSet {

    /** Initialize your data structure here. */
    HashMap<Integer, Integer> map = new HashMap();
    public MyHashSet() {
        this.map = map;
    }
    
    public void add(int key) {
        if (this.map.get(key) == null)
        {
            this.map.put(key, key);
        }
        
    }
    
    public void remove(int key) {
        if(this.map.get(key) != null)
        {
            this.map.remove(key);
        }
    }
    
    /** Returns true if this set contains the specified element */
    public boolean contains(int key) {
        if(this.map.get(key) != null)
        {
            return true;
        }
        else
        {
            return false;
        }
    }
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet obj = new MyHashSet();
 * obj.add(key);
 * obj.remove(key);
 * boolean param_3 = obj.contains(key);
 */