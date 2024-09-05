l=[]
a=int(input("Enter the no of elements in the list: ")) #getting the range of the list
for i in range(0,a):
    b=int(input("Enter a number: ")) #adding all the elements to the list
    l.append(b)
c=0
for i in l:
    e=c #cloning variable c
    if i!=c: #checking if the value of i (list element) is same as that of 'c'
        c=i
    else:
        e=i #re-defining the value of e. Note that the value of 'c' (line 8) also changes
        l.remove(i) #removing all the duplicate elements
print ("List after deleting all the recurring elements: ",l)
