def lcs(str1, str2):
    a = len(str1)
    b = len(str2)
    string_matrix = [[0 for i in range(b+1)] for i in range(a+1)]  
    direction_matrix = [[0 for i in range(b+1)] for i in range(a+1)]  
    for i in range(1, a+1):
        for j in range(1, b+1):
            if i == 0 or j == 0:
                string_matrix[i][j] = 0
            elif str1[i-1] == str2[j-1]:
                string_matrix[i][j] = 1 + string_matrix[i-1][j-1]
                direction_matrix[i][j]='D'
            elif string_matrix[i-1][j] >= string_matrix[i][j-1]:
                string_matrix[i][j]=string_matrix[i-1][j]
                direction_matrix[i][j]='U'
            else:
                string_matrix[i][j]=string_matrix[i][j-1]
                direction_matrix[i][j]='L'
               
    for i in range(0,a+1):
        for j in range(0,b+1):
            print(string_matrix[i][j], end=' ')
        print('')
    print()
    for i in range(0,a+1):
        for j in range(0,b+1):
            print(direction_matrix[i][j], end=' ')
        print('')
    index=string_matrix[a][b]
    res = [""] * index
    i = a
    j = b
    while i > 0 and j > 0:
        if str1[i-1] == str2[j-1]:
            res[index-1] = str1[i-1]
            i -= 1
            j -= 1
            index -= 1
        elif string_matrix[i-1][j] > string_matrix[i][j-1]:
            i -= 1
        else:
            j -= 1
    return res
if __name__ == '__main__':
    str1 = input('Enter first string:')
    str2 = input('Enter second string:')
    string1 = ''.join(lcs(str1, str2))
    print("Length of LCS is:", len(string1),"\nsubsequence is:", string1)
 
