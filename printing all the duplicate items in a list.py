l=[]
a=int(input("Enter the no of elements in the list: ")) #getting the range of the list
for i in range(0,a):
    b=int(input("Enter a number: ")) #adding all the elements to the list
    l.append(b)
d=[] #blank list required to store the duplicate elements
c=0
for i in l:
    e=c #cloning variable c
    if i!=c: #checking if the value of i (list element) is same as that of 'c'
        c=i
    else: 
        e=i #re-defining the value of e. Note that the value of 'c' (line 9) also changes
        if i not in d: #checking whether the given number is already present in list 'd'
            d.append(e)
print (d)
