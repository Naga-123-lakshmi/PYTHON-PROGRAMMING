#list Comprehension PRINT EVENS 
even=[x for x in range(5) if x%2==0]
print(even)

#list Comprehension using if - else
result=["even" if x%2==0 else "odd" for x in range(10)]
print(result)

#list Comprehension create a list of squares
squares=[x**2 for x in range(5)]
print(squares)
#convert strings to uppercase
strings=["naga","lakshmi","varshini","hema"]
upper=[strings.upper() for strings in strings]
print(upper)