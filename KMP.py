'''
Siddesh Mishra
Exp4 KMP algorithm
Roll no:06
'''
def KMPSearch(pat, txt):
    M = len(pat)
    N = len(txt)
 
    lps = [0]*M
    j = 0 # index for pat[]
 
    computeLPSArray(pat, M, lps)
    i = 0 # index for txt[]
    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1
        if j == M:
            print ("\nFound pattern at index", str(i-j))
            j = lps[j-1]
        elif i < N and pat[j] != txt[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
 
def computeLPSArray(pat, M, lps):
    len = 0 # length of the previous longest prefix suffix
    lps[0] # lps[0] is always 0
    i = 1
    while i < M:
        if pat[i]== pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            if len != 0:
                len = lps[len-1]
            else:
                lps[i] = 0
                i += 1
    print('Prefix Table is:')
    for i in range(M):
        print(pat[i],end="|")
    print('\n')
    for i in range(M):
        print(lps[i],end="|")
 
txt = input('Enter the text:')
pat = input('Enter the pattern to be searched:')
KMPSearch(pat, txt)