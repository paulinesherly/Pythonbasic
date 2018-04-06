print ("Hai Pauline")
x = 5/4
print(5/4)

a = dict(name='Tim', age = 3 , School ='no')
b = dict(name2= 'paul', age2 = 0.2, School2 = 'no', **a )
print(b)
print(('name' in a))
y= input("Getting a input for y ")
print(y)

#while loop
while x<10:
   # print(x)
    x+=1
b = 1

#for loop
for i in range(0,b):
    print(x)
    
#if,elif    
str = "hai"
if (str==0):
    print("false")
elif (str):
    print("true --- 'Correct' ")
elif (str=="hai"):
    print("hai")
else:
    print("nothing is 'Correct' ")


#creating a function
    


#x = samplefunc(b,str)
#print(x)

#writing ,appending and reading a file
text = "This is my new file \n Written by python"
saveFile = open('exampleFile.txt','w')
saveFile.write(text)
saveFile.close()


class ageList:

    def child(age):
        if(age<13):
            print("it's a child")
        else:
            print("Invalid age")

    def teen(age):
        if(age>13 & age<20):
            print("He/she is a teenager")
        else:
            print("Invalid age")

    def middleage(age):
        if(age>20 & age<50):
            print("He/she is middle-aged")
        else:
            print("Invalid age")

    def old(age):
        if(age>50):
            print("He/she is old")
        else:
            print("Invalid age")

ageList.teen(20)


list1 = [[1,2,3],   
         [4,5,6],   
         [7,8,9]]

list2 = [[3,2,1],
         [6,5,4],
         [9,8,7]]

x = 0;y = 0; d = 0;e = 0;
list3 = []
for num in list1:
    for num2 in list2:
       # print(num,num2)
        try:
            samplist = [num, num2]
            list3.append(num)
            list3.append(num2)
            print(list3)

        except Exception as e:
            print(e)

print('printing list3 :',list3)
        
