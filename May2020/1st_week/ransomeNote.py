import re
from collections import Counter

"Ransome note problem"

def ranSomeNote(ransomeNote, magazine):
        
        RANSOME_DICT = Counter(ransomeNote)
        MAGAZINE_DICT = Counter(magazine)

        for key in RANSOME_DICT.keys():
            if MAGAZINE_DICT[key] >= RANSOME_DICT[key]:
                pass
            else:
                return False

        return True


ransomeNote = "fffbfg"
magazine = "efffffbbbbbbbggggggghjkhjgjh"

string = "leetcode"
string2 = "loveleetcode"

def firstUniqueChar(string):

    if string.__len__ == 0:
        return -1
    count = Counter(string)
    for key in count.keys():
        if count[key] == 1:
            #return "First non repeating char : {}, index : {} ".format( key, string.index(key) ) 
            return string.index(key)
            break
    return -1
    



if __name__ == "__main__":
    print( ranSomeNote(ransomeNote,   magazine) )
    
    # RANSOME_DICT = Counter(ransomeNote)
    # MAGAZINE_DICT = Counter(magazine)
    
    # print( RANSOME_DICT )
    # print( MAGAZINE_DICT )
    # for key in RANSOME_DICT.keys():
    #     if MAGAZINE_DICT[key] >= RANSOME_DICT[key]:
    #         pass
    #     else:
    #         print(False)
    
    # print( firstUniqueChar(string) )
    
    print( firstUniqueChar("cc") )

    


                

