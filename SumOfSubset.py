'''
Siddesh Mishra
SECMPNB1
EXP 9:Sum of Subsets
'''
def sum_of_subset(list1, sum):
    x=[1]*t
    if sum < 0:
        return
    if len(list1) == 0:
        if sum == 0:
            yield []
        return False
    for i in sum_of_subset(list1[1:], sum):
        yield i
    for i in sum_of_subset(list1[1:], sum - list1[0]):
        yield [list1[0]] + i 

list1 = list(map(int,input("Entre Set Value : ").split()))
n = int(input("Entre Sum Value:"))
t= len(list1) 
sub_sets = sum_of_subset(list1,n )
list2 = list(sub_sets)
q = len(list2)
x=[0]*t
if q == 0:
	print("No Subsets Exists")
else:
	print(f"Following Are The Subsets To give The Sum : {n}")
	for i in range(q):
		for j in range(len(list2[i])):
			pos=list1.index(list2[i][j])
			x.pop(pos)
			x.insert(pos,1)
		print(x)
		x.clear()
		x=[0]*t