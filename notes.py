#defining our own function, by using the keyword "def" and the name of our function with parenthesis and colon ":" followed by an indented code block with the actions we need it to perform
def chimulco():
  print("hello there")
  print("nice to see you")
#after creating the function we have to call it to get executed by the console. We can't call functions before declaring them
print("it's time to call the function")
chimulco()
# we can assign a function to another variable
def spam():
    print("Spam, spam, spam, spam")
spam()

spam_on_eggs = spam
spam_on_eggs()
#to indent whole blocks of code we use "ctrl + ]" or "ctrl + tab" and "ctrl + [" to get it back to the start
# 4 spaces are the preferred indentation method over the tab method
#most code editors have settings that allows to indent using spaces or tabs and establish the size of the indentation to 2, 4 or whichever spaces we want. So when we hit the tab key the editor automaticly adds 4 spaces

#while loop: if the condition is true it keeps doing the actions inside the indented code block until the condition becomes false
# to stop an infinite loop press Ctrl+C
countdown = 10
while countdown > 0:
    countdown -= 1
    print(countdown)
# break: we use this keyword to force a stop in a loop
countdown2 = 10
while countdown2 > 0:
    countdown2 -= 1
    if countdown2 == 4:
        break
    print(countdown2)
# continue: with this keyword we continue to the next iteration of the loop and all the code that comes after the "continue" keyword is ignored
countdown3 = 10
while countdown3 > 0:
    countdown3 -= 1
    if countdown3 > 7:
        continue
    print(countdown3)

for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found an odd number", num)
# same functionality as doing it with the "else" clause
for chop in range(2, 10):
    if chop % 2 == 0:
        print("even", chop)
    else:
        print("odd", chop)
# A for or while loop can include an "else" clause. With the "else" statement we can run a block of code once when the condition of the loop no longer is true. In a for loop, the else clause is executed after the loop reaches its final iteration. In a while loop, it’s executed after the loop’s condition becomes false. In either kind of loop, the else clause is not executed if the loop was terminated by a break
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

for x in range(6):
  print(x)
else:
  print("Finally finished!")

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number')
#the while loop gives you control over the index numbers. Here's a while loop which accesses every 3rd element in a list
names=["jose","juan","pedro","martha","ramon","ulises","katia","diana","esmeralda","ruby"]
var=0
while var<len(names):
    print(names[var])
    var+=3
# same functionality using a for loop with the range function
for x in range(0, len(names), 3):
    print(names[x])


#https://docs.python.org/3/library/functions.html
# (PEP, Python Enhancement Proposals) https://peps.python.org/pep-0008/
# https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops
# https://www.w3schools.com/python/python_while_loops.asp
