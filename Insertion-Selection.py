'''
Name:Siddesh Mishra  
Roll no:06  
Implementation of insertion and selection sort  
'''
import time
def insertion(A,n):
    to=time.time()
    for j in range(1,n):
        key=A[j]
        i=j-1
        while i>=0 and A[i]>key:
            A[i+1]=A[i]
            i=i-1
        A[i+1]=key
        print("Pass",j,A)
    print("After Insertion sort List is:",A)
    t1=time.time() - to
    print("time=",t1)

def selection(A,n):
    to=time.time()
    for i in range(n):
        j=i
        for k in range(i+1,n):
            if A[k]<A[j]:
                j=k
        temp=A[i]
        A[i]=A[j]
        A[j]=temp
        print("pass",i+1,A)
    print("After Selection sort List is:",A)
    t1=time.time() - to
    print("time=",t1)

n=int(input("Number of elements in the array:-"))
a=list(map(int,input("elements of array:-").strip().split()))[ :n]
option=int(input("1.Insertion sort\n2.Selection sort\n"))
insertion(a,n)if option==1 else selection(a,n)
