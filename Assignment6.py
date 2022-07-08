#Q1
n = int(input("Enter a number: "))
sum = 0
for i in range(1, n):
  if(n % i == 0):
    sum = sum + i
if (sum == n):
  print(" %d is a Perfect Number" %n)
else:
  print(" %d is not a Perfect Number" %n)

#Q2
def isPalindrome(x):
    return x == x[::-1]
x = input("enter a word: ")
y = isPalindrome(x)
if y:
    print("Yes")
else:
    print("No")
    
#Q3
from math import factorial
n = 6
for i in range(n):
    for j in range(n-i+1):
        print(end=" ")
    for j in range(i+1):
        print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
    print()

#Q4
def pangram(x):
    check=""
    small=x.lower()
    combine=small.replace(" ","")
    for i in combine:
        if i in check:
            return False
        else:
            check+=i
    return True
print(pangram("The quick brown fox jumps over the lazy dog"))

#Q5
n=input("enter the string: ") 
l=n.split('-') 
l.sort() 
print('-'.join(l))

#Q6
def student_data(student_id, **kwargs):
    print(f'\nStudent ID: {student_id}')
    if 'student_name' in kwargs:
        print(f"Student Name: {kwargs['student_name']}")
    if 'student_name' and 'student_class' in kwargs:
        print(f"\nStudent Name: {kwargs['student_name']}")
        print(f"Student Class: {kwargs['student_class']}")
student_data(student_id='21107078', student_name='Shorya Aggarwal')
student_data(student_id='21107078', student_name='Shorya Aggarwal', student_class ='B.Tech Mechanical')

#Q7
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

#Q8
def findTriplets(arr, n):
    for i in range(0, n-2):
        found = False
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if (arr[i] + arr[j] + arr[k] == 0):
                    print(arr[i], arr[j], arr[k])
                    found = True
    if (found == False):
        print("does not exist")
arr = [-25, -10, -7, -3, 2, 4, 8, 10]
n = len(arr)
findTriplets(arr, n)

#Q9
class validity:
    def f(str):
        a= ['()', '{}', '[]']
        while any(i in str for i in a):
            for j in a:
                str = str.replace(j, '')
        return not str
s = input("enter : ")
print(s, "-", "is balanced"
    if validity.f(s) else "is Unbalanced")

