#program by himala
#date 8/26/2016


print "******* Welcome to Number Game *********"
print "How to paly:  Enter your number if computer guess same as your number then you will win "
print ""

#game levels
print "Please Enter Game Level you like to paly"
game_level = int(raw_input("Level 1 (Easy) enter 1, Level 2 (Intermediate) enter 2, Level 3 (Difficult) enter 3 : "))
print ""
print "Good Luck"
print ""
#Level 1
if game_level == 1:
    player_number = raw_input("enter number between 1 to 5 : ")
    import random
    random_number = random.randint(1, 5)
    import time
    print "Wait.. Computer Thinking"
    time.sleep(1.5)
    print "Computer says: " + str(random_number)
    if (random_number == player_number):
        print "****** you win ******"
    else:
        print " sorry you lost :( "
#Level 2
elif game_level == 2:
    player_number = raw_input("enter number between 1 to 25 : ")
    import random
    random_number = random.randint(1, 25)
    import time
    print "Wait.. Computer Thinking"
    time.sleep(1.5)
    print "Computer says: " + str(random_number)
    if (random_number == player_number):
        print "****** you win ******"
    else:
        print " sorry you lost :( "
#Level 3
elif game_level == 3:
    player_number = raw_input("enter number between 1 to 50 : ")
    import random
    import time
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
