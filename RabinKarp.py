# Siddesh Mishra
# Exp3
# Roll no:06
def search(pattern,text,q):
    m=len(pattern)
    n=len(text)
    p=0
    t=0
    h=1
    i=0
    j=0
    d=int(input('Enter the radix to use: '))
    for i in range(m-1):
        h=(h*d)%q
    for i in range(m):
        p=(d*p + ord(pattern[i]))%q
        t=(d*t + ord(text[i]))%q
    for i in range(n-m+1):
        if p==t:
            for j in range(m):
                if text[i+j]!=pattern[j]:
                    print('spurious hit at position:'+str(i+1))
                    break
            j+=1
            if j==m:
                print('Pattern is found at position:'+str(i+1))
        if i<n-m:
            t=(d*(t-ord(text[i])*h)+ ord(text[i+m]))%q
            
            if t<0:
                t=t+q
            
text=input('Enter the Text: ')
pattern=input('Enter the pattern to be searched in text: ')
q=int(input('Enter the prime q: '))
search(pattern,text,q)