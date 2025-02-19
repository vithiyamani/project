# print elements from third index
my_list = [10, 20, 30, 40, 50, 60, 70]
print(my_list[3:])

#leap year
year=int(input("enter a year"))
if(year%400==0 or year%4==0 and year%100!=0):
    print("leap year")
else:
    print("not a leap year")
    
#even or odd without using if 

n=int(input("enterthe number"))
result=["even","odd"][n%2]
print(f"the number{result}.")

#sum of integers

numbers = [1, 2, 3, 4, 5]
total = sum(numbers)
print("The sum of the integers is:", total)

#swap the numbers

a = 5
b = 10
temp = a
a = b
b = temp
print("After swapping: a =", a, "b =", b)

#reverse a list

my_list = [1, 2, 3, 4, 5]
my_list.reverse()
print("Reversed list:", my_list)

#pyramid star pattern

n = 5
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    print("*" * (2 * i - 1))
    
#square pattern 

n = 5
for i in range(n):
    print("*" * n)
    
 #unique numbers
 
from collections import Counter


pairs_list = [(1, 2), (3, 4), (2, 3), (5, 6), (1, 5)]

flat_list = [item for pair in pairs_list for item in pair]

count = Counter(flat_list)


unique_numbers = [num for num, freq in count.items() if freq == 1]


print("Unique numbers:", unique_numbers)

#inverted right angle triangle
n = int(input("enter the rows"))
for i in range (n,0,-1):
    print(""* (n-i)+ "*"* i )
    
 #hollow square
n = int(input("enter size of the square: "))
for i in range(n):
    if i == 0 or i == n - 1 :
        print("*" * n)
    else:
        print("*" + "" * (n-2) + "*")
       
    
          






  
