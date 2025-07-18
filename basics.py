#Basic List Problems"""list=[1,2,3,4,5]
print(list)
print(len(list))
print(list[0])
print([len(list)//2])
print(list[-1])
list[2]=9
print(list)
list.append(10)
print(list)
list.insert(1,6)
print(list)
list.pop()
print(list)
#Number-Based List Problems
#sum of lists
list=[2,3,4,5,6,7]
print(sum(list))
#max-min numbers
max=max(list)
min=min(list)
print("max_number:",max)
print("min_number:",min)
#Even-Odd count
list=[1,2,3,4,5,6,7,8,9,10]
even=0
odd=0
for list in list:
        if list%2==0:
            even+=1
        else:
            odd+=1
print("even_count:",even)
print("count:",odd)
#1-20 numbers using range
numbers=list(range(0,21))
print(numbers)
#using for loop
list=[]
for i in range(0,21):
    list.append(i)
print(list)
#remove all evens giving user input
numbers=input("enter numbers:")
nums=list(map(int,numbers.split()))
odd=[num for num in nums if num % 2 !=0]
print(odd)
#using list comprehension remove even numbers
numbers=[10,22,33,43,58,96]
odd_numbers=[number for number in numbers if number%2 !=0]
print(odd_numbers)
#remove even numbers
numbers=[2,3,24,54,63]
odd_numbers=[]
for number in numbers:
    if number%2!=0:
        odd_numbers.append(number)
print("remaining numbers:",odd_numbers)
#second largest number
nums=[89,38,1,74,93,34]
numbers=list(set(nums))
print(numbers)
print(numbers[-2])

