#Q1 Checking if the number is perfect or not?

def perfect_number(n):
    sum = 0
    for x in range(1,n):
        if (n % x == 0):
            sum = sum + x
    return sum

n = int(input("Enter a number:"))

if(n == perfect_number(n)):
    print(n, "is a perfect number")
else:
    print(n, "is not a perfect number")
print("")

print("The other method is including digit")
def perfect_number(n):
    sum = 0
    for i in range(1,n+1):
        if (n%1 == 0):
            sum = sum+i
    return sum/2

n = int(input("Enter a number:"))
if (n == perfect_number(n)):
    print(n, "The number is a perfect number")
else:
    print(n,"The number is not a perfect number")

print("")

# Q2 Is the passed string a palindrome or not?
def isPalindrome(s):
            return s == s[::-1]

a = input("Enter a string:")

reverse = isPalindrome(a)
if reverse:
    print(a, 'is a Palindrome')
else:
    print(a,'is not a Palindrome')

print("")


#Q3 Pascal's Triangle
def factorial(a):
    i = 1
    for m in range (1, a+1):
        i = i*m

    return i

n = int(input("Enter the number of rows:"))

for p in range (0,n):
    for q in range(1,n-1):
        print("")

    for r in range(0, p+1):
        coefficient = int(factorial(p)/(factorial(r)*factorial(p-r)))
        print("", coefficient, end ="")

print("")

n = int(input("Enter the number of rows:"))

print("")


#Q4 Pangram

import string

def is_pangram(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in s.lower():
            return False

    return True

# Driver code
string = input("Enter the string:")
if (is_pangram(string)== True):
    print("Yes, the given string is a pangram")
else:
    print("No, the given string is not a pangram")

print("")

#Q5 Given the hyphen separated string as user input using the input() function.

s = input("Enter the string =")
# print the string before alteration
print("the string before alteration =",s)
#split the hyphen separated strings into a list of strings using the split()
# function and store it in a variable.
w = s.split("-")
# sort the given list using the sort()
w.sort()
# print the sorted sequence by joining the words in the list with a hyphen
result = '-'.join(w)
#print the resultwords
print("The string after alteration =", result)
print("")



# Question 6
# Student Data


def student_data(student_id, **kwargs):
    print("Student ID=", student_id)
    if "student_name" in kwargs:
        print("Student Name=", kwargs["student_name"])
    if "student_class" in kwargs:
        print("Student Class=", kwargs["student_class"])


        student_data(student_id="21102025")
        student_data(student_id="21102025", student_name="Hitanshi Sharma")
        student_data(student_id="21102025", student_name="Hitanshi Sharma", student_class="1st Year")
        print()


# Question 7

class Student:
    pass


class Marks:
    pass


student1 = Student()
marks1 = Marks()
print(isinstance(student1, Student))
print(isinstance(marks1, Student))
print(isinstance(marks1, Marks))
print(isinstance(student1, Marks))
print("\nCheck whether the said classes are subclasses of the built-in object class or not.")
print(issubclass(Student, object))
print(issubclass(Marks, object))
print()




# Question 8
# Print all triplets within an array whose sum is zero

def findTriplets(arr, n):
    found = False
    for i in range(0, n - 2):

        for j in range(i + 1, n - 1):

            for k in range(j + 1, n):

                if (arr[i] + arr[j] + arr[k] == 0):
                    print(arr[i], arr[j], arr[k])
                    found = True

    # If no triplet with 0 sum found in array
    if (found == False):
        print("not exist")


#  Driver code
arr = [-25, -10, -7, -3, 2, 4, 8, 10]
n = len(arr)
findTriplets(arr,n)

print("")


# Question 9
# Parantheses

class parantheses:
    def find(str):
        a = ['()', '{}', '[]']
        while any(i in str for i in a):
            for j in a:
                str = str.replace(j, '')
        return not str


s = input("Enter the sequence of parantheses : ")
if parantheses.find(s):
    print(s, "-", "is balanced")
else:
    print(s, "-", "is unbalanced")






