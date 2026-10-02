def powerplay(index ,curr,s,result):
    if(index==len(s)):
        result.append(curr)
        return result
        
    powerplay(index+1,curr,s,result)
    powerplay(index+1,curr+s[index],s,result)
class Solution:
	def powerSet(self, s):
		result=[]
		powerplay(0,"",s,result)
		result.sort()
	
		return 	result
