#program by himala
#date 8/26/2016

import random
import time

print "******* Welcome to Number Game *********"
print "How to paly:  Enter your number if computer guess same as your number then you will win "
print ""

#game levels
print "Please Enter Game Level you like to paly"
game_level = raw_input("Level 1 (Easy) enter 1, Level 2 (Intermediate) enter 2, Level 3 (Difficult) enter 3 : ")
print ""
print "Good Luck"
print ""
#Level 1
if game_level == "1":
    player_number = raw_input("enter number between 1 to 5 : ")
    random_number = random.randint(1, 5)
    print "Wait.. Computer Thinking"
    time.sleep(1.5)
    print "Computer says: " + str(random_number)
    if (random_number == int(player_number)): # player number and computer number matching same
        print "****** you win ******"
    elif (random_number < int(player_number)): # computer number smaller than player number
        print " Too Hi"
        print " sorry you lost :( "
    elif (random_number > int(player_number)): ## computer number larger than player number
        print " Too Low"
        print " sorry you lost :( "
    else:
       print " sorry you lost :( "
#Level 2
elif game_level == "2":
    player_number = raw_input("enter number between 1 to 25 : ")
    random_number = random.randint(1, 25)
    print "Wait.. Computer Thinking"
    time.sleep(1.5)
    print "Computer says: " + str(random_number)
    if (random_number == player_number):
        print "****** you win ******"
    else:
        print " sorry you lost :( "
#Level 3
elif game_level == "3":
    player_number = raw_input("enter number between 1 to 50 : ")
    print "Wait.. Computer Thinking"
    time.sleep(1.5)
    random_number = random.randint(1, 50)
    print "Computer says: " + str(random_number)
    if (random_number == player_number):
        print "****** you win ******"
    else:
        print " sorry you lost :( "
#Wrong level select
else:
    print "Please Select Correct Game level"