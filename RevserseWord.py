s = "hello world   "

word= ""

i = len(s) - 1 
res = []

while i>=0:
    while i>=0 and  s[i]== " ":
        i-=1

    if i<0:
        break       

    end_idx = i
    
    while i >=0 and s[i]!= " ":
        i-=1
    start_idx =i+1
    word = s[start_idx:end_idx+1]
    res.append(word)


    ans= " ".join(res)

     

print(ans)
    
