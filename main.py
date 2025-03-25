 a = 10
 print ("Type of a: ", type(a))

 b=10.5
 print("Type of b:", type(b))

 c= 2+3j
 print("Type of c:", type(c))

 d = 'w'
 print("type of d:", type(d))

 string1= "hello"
 string2 = 'world !'
 string3 = '''

     A triple string 
     can take multiple line of 
     code amd will still work
 '''

 print(string1 + string2 + string3)
 print ('first character of string1:', string1[0])
 print('last character of string2:' ,string2[-1])


 tuple1 = ()
 print ("The type of tuple", type(tuple1))
 tuple1 = (1, 2, 3, "Geeks")
 print ("tuple1:", tuple1)
 print ("first item in tuple1", tuple[0])
 
 dict1 = {1: 'Geeks', 2:'for', 3:'Geeks'}
 dict2 = {'Name': "Wanja",'Age': "22"}
 print ("The dict2 Name", dict2['Name'])

#nested if
 num = int(input( "Enter a number:"))
 if num >= 0:
     if num == 0:
        print (num, "is neither positive or negative, it is zero")
     else:
         print(num, "is a positive value")
 else:
     print(num, "is a negative value.")

 print("outside body of if statement")

#if statements 
 num = int(input( "Enter a number:"))
 if num > 0:
     print(num, "is it a positive value.")
 elif num == 0:
     print (num, "is neither positive or negative, it is zero")
 else:
     print(num, "is a negative value")

 print("outside body of if statement")

 ''' for loop'''
 sum = 0 
 numbers = [2,3,4,5,6,11,15,20,12]
 for i in numbers:
     sum += i 
 print ("the sum of the numbers is", sum)


 print (range(10))
 alist= list(range(10))
 print(alist) # print the whole list
 print(alist[6]) # specific item

 print(range(0,10,2))
 listb = list(range(0,10,2))
 print("print the listb", listb)

 ''' combining for and range'''
 sum = 0
 for var in range(1, 11):
     sum += var
 print(sum)    

# #iteration of a list through an index
 music = ["pop", "jazz", "rock", "classical"]
  # using a for loop to iterate over the list and print each item
 for i in range(len(music)):
     print(music[i])

# ''' while looping example'''
 n = int(input("enter how many natural numbers you want to add:"))
 sum = 0
 i= 1 

 while i <= n:
     sum += i
     print ("The sum of the ", i, "natural number is:" , sum )
     i += 1

# ''' break statements'''
 for val in "string":
     print('in for loop', val)
     if val == "i":
         break
 print('out of loop')


#  add 2 numbers to illustrate return
def add(a, b):
    return (a+b)

print (add.__doc__)  
print(add(4, 5))  # prints: 9
