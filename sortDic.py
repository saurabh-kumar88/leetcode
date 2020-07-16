# sorting dic by values

from collections import Counter

string  = "etree"
freq = Counter(string)



a = {}
a['ind'] = 45
a['can'] = -40
a['uk'] = 25
a['aus'] = 45

value_list = list(a.values())
key_list = list(a.keys())

sorted_by_value = {}

if __name__ == "__main__":
    # print(freq)
    # ans = ""
    # for i in sorted(freq.keys()):
    #   ans += i * freq[i]
    
    # print(ans)

    print(a)
    for value in sorted(a.values()):
      Key = key_list[value_list.index(value)]

      print( value ," : ", key_list[value_list.index(value)] )
      del[Key]
      
      sorted_by_value[Key] = value

    # print(sorted_by_value)
    # for x in sorted_by_value.keys():
    #   print(x , " : ", sorted_by_value[x])



