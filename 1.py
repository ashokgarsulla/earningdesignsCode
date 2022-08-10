string = "C1e7h3P4k12";
string = "b3c6M4d15";
d = {}
stack = []
digColl = ""
result = ""
for i in range(len(string),-1,-1):
    if(i<len(string)):
        if(string[i] >= '0' and string[i]<='9'):
            stack.append(string[i])
        elif ((string[i] >= 'a' and string[i]<='z') or (string[i] >= 'A' and string[i]<='Z')):
            digColl = ""
            while len(stack)!=0 :
                digColl+=stack.pop(-1)
            for j in range(0,int(digColl)):
                result+=string[i]
result = result[::-1]
print(result)    
