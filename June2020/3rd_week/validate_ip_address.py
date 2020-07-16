import re

class Solution:
  def validIPAddress(self, IP: str) -> str:
    
    if '.' in IP:
      return self.isValid_ipv4( IP.split(".") )
    elif ':' in IP and "::" not in IP:
      return self.isValid_ipv6( IP.split(":") )
    else:
      return "Neither"
  
  def isValid_ipv4(self,IP_arr):
    # check 1 : len()
    if len(IP_arr) != 4 or '' in IP_arr:
      return "Neither"
    # check 2 : leading zeros white space or special char
    special_symbols = re.compile('[@_!#$%^&*()<>?/\|}{~:]') 
    for group in IP_arr:
      if re.findall("\s|[a-zA-Z]", group) or special_symbols.search( group ) :
        return "Neither"
      
      # check 3: leading zeros
      if len([i for i in re.finditer('0', group)]) > 1:
        return "Neither"
            
      if len([i for i in re.finditer('0', group)])==1 and int(group) != 0:
        return "Neither"
      
      # check 4: number range
      if int(group) < 0 or int(group) > 255: # check 3 : range
        return "Neither"
      
    return "IPv4"

  def isValid_ipv6(self, IP_arr):
      
    # check 1: len()
    if len(IP_arr) != 8 or '' in IP_arr:
      return "Neither"

    # check 2: first byte of first group
    if re.findall(r"\b0", IP_arr[0]):
      return "Neither"

    # check 3: each group should be only four byte long
    special_symbols = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    for group in IP_arr:
      if len(group) != 4:
        return "Neither"
      elif re.findall("[g-zG-Z]", group) or re.findall("[+-]", group) or special_symbols.search(group):
        return "Neither"
      
    return "IPv6"
    

    




# driver code

# ipAddress = "172.16.254.1"
# o/p : "IPv4"
# ipAddress = "2001:0db8:85a3:0:0:8A2E:0370:7334"
# o/p : "IPv6"
# ipAddress = "256.256.256.256"
# o/p : "Neither"
# ipAddress = "2001:0db8:85a3:00000:0:8A2E:0370:7334"
# o/p : "Neither"
# ipAddress = "192.0.0.1"
# o/p : "IPv4"
# ipAddress = "1.0.1."
# o/p : "IPv4"
# ipAddress = "172.16.254.1"
# o/p : "IPv4"
ipAddress = "00.0.0.0"
# o/p : "Neither"

if __name__ == "__main__":
    obj = Solution()
    print(obj.validIPAddress(ipAddress))

    
     

     