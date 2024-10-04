#alone reeborg's world
def turn_around():
    turn_left()
    turn_left()
def turn_right():
    turn_left()
    turn_left()
    turn_left()
turn_left()
move()
turn_right()
move()
turn_right()
move()
turn_right()
move()
#hurdle 1
#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
for movement in range(0,6):
    jump()
# hurdle 1 alternate version with while loop
numb_hurdles=6
while numb_hurdles>0:
    jump()
    numb_hurdles-=1

#hurdle 2
#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
while at_goal()==False:
    jump()
#hurdle 3
#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
while not at_goal():
    if front_is_clear():
        move()
    else:
        jump()
#hurdle 4
#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
#maze (the code works in almost all cases)
#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
def turn_right():
    turn_left()
    turn_left()
    turn_left()
while not at_goal():

    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
#debugging exercise for problem_worlds 1,2 and 3 from angela's zip file(this is the maze definitive code that must works in all cases)
        
#debug version 1 (works in almost all cases)
def turn_right():
    turn_left()
    turn_left()
    turn_left()
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
        if right_is_clear():
            turn_right()
        while front_is_clear():
            move()
    elif front_is_clear():
        move()
    else:
        turn_left()
#debug version 2 (works in almost all cases)
while not at_goal():
    if right_is_clear():
        turn_right()
        while front_is_clear():
            move()
            if right_is_clear():
                turn_right()
                move()
    elif front_is_clear():
        move()
    else:
        turn_left()
#Angela debugging version: (works in every known outcome i've tested so far) The key to debug this is that we need to get our robot to a starting position where it has a wall in the right side. This is because of the order of the if, elif, else conditionals first checking if the right side is clear, creating the infinite loop
def turn_right():
    turn_left()
    turn_left()
    turn_left()
while front_is_clear():
    move()
turn_left()
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
