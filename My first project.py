#My first project
#comments help other programmers understand ur code quickly, and is useful for debugging

print("Hello world!")

#python uses indentation to organise and structure code, wrong indentation causes a bug
#capitalisation also matters in Python

#variable: stores data to be used later, use equal sign to assign value, printed wihtout quotes
#variable naming: only _ symbol accepted, cannot start with a number, no reserved keywords(and, assert, break, class, continue, def)

myGreeting = "Welcome to Coding Lab!"
print(myGreeting)

#update variable to hold a different data
myGreeting = "You will be an expert Python coder!"
print(myGreeting)

#strings: from variables, can be any symbol number letters, enclosed in quotation marks
userName = input("What is your name?: ")
myGreeting = "Dear " + userName + ", welcome to Coding Lab!"
print(myGreeting)

#print special chracters with \ as escape char
print(userName + " said: \"Great!\"")
print("1\n2\n3\n")

#print multiple inputs
print("abc", "def", "ghi")

#multiplying strings
print("string" *3)
