
#Developer's name: Angelina
#Date: 11/20/20
#Adventure Game: The Evil Bruh
#Background information: This is basically just a continuation to an ongoing story I've been doing for these types of assignments
 
#imports
import time
import random
 
 
#variables
done = False
note = 0
injury = 0
strength = 0
wit = 0
sword = False
 
 
room0 = ("You're back at the start again.")
room1 = ("Ohh a painting. Very nice. That must be Lady Moment. \nIs that a note behind the frame? Go get it.")
room2 = ("This is one long, dusty hall full of nothing. Sounds like \nthis is where the noise is coming from though. BANG. There it is \nagain. Go farther. BANG. 'I HEAR YOU, COME HERE!' Do you \nwanna go farther or turn back? ")
 
room4 = ("Looks like this door needs a code to open it.")
#intro
 
 
 
while done == False:
 print("After a failed attempt to escape the Evil Bruh's maze, \nyou end up in a dark pit. All you can remember is that \nyou must escape and finally put a stop to him.")
 time.sleep(2)
 
 print()
 
 #beginning --- narrator
 print("So you're in a dark pit, eh? Shame. \nHave you tried feeling around?")
 time.sleep(1)
 
 print()
 
 #first decision
 choice1 = input("Well? \n[1] yes \n[2] no \n \n")
 #user input that gives player a flashlight
 
 if choice1.lower() == "yes" or choice1.lower() == "1":
   print()
   print("Liar. Go on, feel around.")
   time.sleep(1)
   print()
   print("Oh, look! You found a flashlight while feeling around. Fantastic.\nNow you can see all the dust down here.")
   time.sleep(1)
 
 else:
   print()
   print("Oh, look! You found a flashlight while feeling around. Fantastic. \nNow you can see all the dust down here.")
 
   print()
 
   #finding the right room choice
 print("So, you can finally see all these cells... and all of em' empty, huh. \nI wonder if there's anyone else down here.")
 
 print()
 print("BANG!")
 print()
 
 choice2 = input("What was that!? Will you go look? \n[1] yes \n[2] no\n \n")
 #user input to search for noise
 
 if choice2.lower() == "no" or choice2.lower() == "2":
   print("You don't want to continue? Some hero you are...")
   done = True
 else:
   print("Alright, alright... go check out that old painting")
   time.sleep(1)
   print(room1)
   time.sleep(2)
   print()
   note = 1
   print("As soon as the note touches your fingers, a trap door that must \nhave been hiden from all the dirt and dust opens up underneath you. \n\nAfter falling for a few seconds, you grab onto a ledge.")
   time.sleep(3)
   note = 0
   print()
   print("You grab onto the rock, but the note slips out of your grasp and into the dark abyss. \nTo add to that misfortune, your hands are injured too. \nNice going.")
   time.sleep(2)
   injury += random.randrange (1,100)
   print()
   choice5 = input("You can't bring yourself to let go. You keep holding on as if something magical would happen.\nWell, welcome to reality- you're not just going to be saved. Figure it out yourself.\n Are you strong?\n[1] yes\n[2] no\n")
   time.sleep(3)
   if choice5.lower() == "2" or choice5.lower() == "no":
     print("At least you can admit it. Do some pushups to gain strength.")
     choiceA = int(input("How many will you do? "))
     strength = choiceA
     if strength <= 40:
       print("You're still not strong enough, you slip and fall")
       done = True
     else:
       print("Would you look at that, you're strong enough to keep hanging on.")
       print()
       print("1 hour later...")
       print()
       choice6 = input("'BANG!' Oh boy. 'BANG!' There's that sound aganin. It's closer \nnow. 'HEY YOU!' How will you respond? \n[1] help me \n[2] get away from me\n")
       print()
       if choice6.lower() == "1" or choice6.lower() == "help me":
         print("'You got it,' the raspy, mysterious voice responds. A rope is thrown down and you climb up.")
         print()
         choice7 = input("'Hey there, hero. Is this your sword? I found it in the entrance.'\n[1]Yes! I've been looking for that\n[2]No, I have literally never seen that thing in my life\n")
        
         print()
         if choice7.lower() == "1" or choice7.lower() == "yes":
           sword = True
           print("'Here you go, hero. Now follow me.' \nYou throw everything you've ever been taught about strangers, and follow the strange man.\n\nHe leads you down the hall that you previously ignored. You can hear the banging louder than ever.\n'In you go, hero,' the man pushes into a room, 'we've been expecting you.'")
           time.sleep(3)
           print()
           choice8 = input("[1]look to where he pushed you \n[2]turn and ask the man what he was thinking when he pushed you\n")
           if choice8.lower() == "1" or choice8.lower() == "look to where he pushed you":
            
               #import random is working here to generate a random number to add to die_rnd (die_random)
             die_rnd = random.randrange(0,11)
             if die_rnd == 5 or die_rnd == 1 or die_rnd == 8:
               print("You stumble in the direction the man pushed you with your hand on the sword.\nSomeone sprints towards you screaming, but you're not quick enough. \nThe person already has their sword through you. \nHow sad, it seems like it's all over now.")
               done = True
             else:
               print("You stumble in the direction the man pushed you with your hand on the sword.\nSomeone sprints towards you screaming, but you think fast.\nYour sword is already out and through the person.\n'Very good, hero,' the Evil Bruh's voice calls out before you're once again met with nothing but darkness.")
               done = True
           else:
             print("As you turn around to give the man a piece of your mind, you feel a sharp pain enter your back.\nHow lovely. Now you can't finish your mission or give that weird, pushy dude trouble. Some hero you are.")
             done = True
         else:
           print("'Oh, hm... now that I think about it, I probably grabbed it off of one of those dead bodies.\nOh well, mistakes happen. Come along now'")
           time.sleep(1)
           print()
           print("You throw everything you've ever learned about strangers out of the window and followed the man.\n'Let's see what you're made of, hero,' he says while pushing you into the same room you heard the noises coming from earlier.")
           time.sleep(2)
           print()
           if injury <= 30:
             print("You're met with a fierce-looking... what is that thing? A person, obviously... a very strong person...\ngood luck with that, hero, but your hands are so injured, there's no hope. Maybe you should've taken that sword.\nThe person who was clad in ebony armour and carrying an ancient-looking sword notices how you helpless you are.\nThe last thing you hear is, 'pathetic,' as the sharp sword pierces you.")
             done = True
           else:
             print("You're met with a fierce-looking... what is that thing? A person, obviously... a very strong person...\ngood luck with that, hero. Luckily your hand isn't too injured.\nDespite the person's armour and sword, you use your strength to your advantage. Before they can move, you chuck your flashlight that you've managed to keep at their head,\nknocking them out. Very nice.\nYou hear clapping and turn to see it's the Evil Bruh, 'good job, hero,' he says before putting a finger on your temple causing you to faint.")
           done = True
       else:
         print("'Oh...uh... alright then,' the raspy, mysterious voice yells back, the echoes of his feet in the distance, 'The Evil Bruh will not be pleased.'")
         print()
         if injury <= 25:
           print("You may be strong, but your injured hands can't hold up much longer. You pass out and fall, hitting your head.")
           done = True
         else:
           print("You decide to put your flashlight to use and smash them against \nthe stone to create hand holes to go down and get the note you dropped.")
           print()
           note = 1
           choice9 = input("You finally reach the bottom of the pit. The note is down here. Go pick it up.\nDo you want to read it?\n[1]yes \n[2]no?\n")
           if choice9.lower() == "1" or choice9.lower() == "yes":
             print("1442")
             time.sleep(2)
             print("After a few seconds of looking at the note, it vanishes.")
             note = 0
           else:
             print("You decide that reading the note that you risked your life for isn't important")
        
           print("You continue walking.")
           print("....")
           print("The Evil Bruh sure does like neverending halls. There's no turning back, so you walk for at least 30 minutes until you're met with a door.\nIt looks like you need to enter a code. Maybe that note will be useful.")
           if note == 1:
             print("The note reads: 1442")
             time.sleep(1)
             choiceC = input("Enter the code: ")
             if choiceC == "1442":
               print("The door opens and you're met with the Evil Bruh. He puts a finger to your temple and you're met with darkness.")
               done = True
             else:
               print("A loud beep sounds through the rocky hall. You look around to see where it's coming from, but are met with a dart shot into your chest. Suddenly, you faint.")
               done = True
           else:
             print("You no longer have the note.")
             choice10 = input("Enter the code: ")
             if choice10 == "1442":
               print("The door opens and you're met with the Evil Bruh. He puts a finger to your temple and you're met with darkness.")
               done = True
             else:
               print("A loud beep sounds through the rocky hall. You look around to see where it's coming from, but are met with a dart shot into your chest. Suddenly, you faint.")
               done = True
  
 
   else:
     print()
     print("Would you look at that, you're strong enough to keep hanging on.")
     print()
     print("1 hour later...")
     print()
     choice6 = input("'BANG!' Oh boy. 'BANG!' There's that sound aganin. It's closer \nnow. 'HEY YOU!' How will you respond? \n[1] help me \n[2] get away from me\n")
     print()
     if choice6.lower() == "1" or choice6.lower() == "help me":
       print("'You got it,' the raspy, mysterious voice responds. A rope is thrown down and you climb up.")
       print()
       choice7 = input("'Hey there, hero. Is this your sword? I found it in the entrance.'\n[1]Yes! I've been looking for that\n[2]No, I have literally never seen that thing in my life\n")
      
       print()
       if choice7.lower() == "1" or choice7.lower() == "yes":
         sword = True
         print("'Here you go, hero. Now follow me.' \nYou throw everything you've ever been taught about strangers, and follow the strange man.\n\nHe leads you down the hall that you previously ignored. You can hear the banging louder than ever.\n'In you go, hero,' the man pushes into a room, 'we've been expecting you.'")
         time.sleep(3)
         print()
         choice8 = input("[1]look to where he pushed you \n[2]turn and ask the man what he was thinking when he pushed you\n")
         if choice8.lower() == "1" or choice8.lower() == "look to where he pushed you":
          
             #import random is working here to generate a random number to add to die_rnd (die_random)
           die_rnd = random.randrange(0,11)
           if die_rnd == 5 or die_rnd == 1 or die_rnd == 8:
             print("You stumble in the direction the man pushed you with your hand on the sword.\nSomeone sprints towards you screaming, but you're not quick enough. \nThe person already has their sword through you. \nHow sad, it seems like it's all over now.")
             done = True
           else:
             print("You stumble in the direction the man pushed you with your hand on the sword.\nSomeone sprints towards you screaming, but you think fast.\nYour sword is already out and through the person.\n'Very good, hero,' the Evil Bruh's voice calls out before you're once again met with nothing but darkness.")
             done = True
         else:
           print("As you turn around to give the man a piece of your mind, you feel a sharp pain enter your back.\nHow lovely. Now you can't finish your mission or give that weird, pushy dude trouble. Some hero you are.")
           done = True
       else:
         print("'Oh, hm... now that I think about it, I probably grabbed it off of one of those dead bodies.\nOh well, mistakes happen. Come along now'")
         time.sleep(1)
         print()
         print("You throw everything you've ever learned about strangers out of the window and followed the man.\n'Let's see what you're made of, hero,' he says while pushing you into the same room you heard the noises coming from earlier.")
         time.sleep(2)
         print()
         if injury <= 30:
           print("You're met with a fierce-looking... what is that thing? A person, obviously... a very strong person...\ngood luck with that, hero, but your hands are so injured, there's no hope. Maybe you should've taken that sword.\nThe person who was clad in ebony armour and carrying an ancient-looking sword notices how you helpless you are.\nThe last thing you hear is, 'pathetic,' as the sharp sword pierces you.")
           done = True
         else:
           print("You're met with a fierce-looking... what is that thing? A person, obviously... a very strong person...\ngood luck with that, hero. Luckily your hand isn't too injured.\nDespite the person's armour and sword, you use your strength to your advantage. Before they can move, you chuck your flashlight that you've managed to keep at their head,\nknocking them out. Very nice.\nYou hear clapping and turn to see it's the Evil Bruh, 'good job, hero,' he says before putting a finger on your temple causing you to faint.")
         done = True
     else:
       print("'Oh...uh... alright then,' the raspy, mysterious voice yells back, the echoes of his feet in the distance, 'The Evil Bruh will not be pleased.'")
       print()
       if injury <= 25:
         print("You may be strong, but your injured hands can't hold up much longer. You pass out and fall, hitting your head.")
         done = True
       else:
         print("You decide to put your flashlight to use and smash them against \nthe stone to create hand holes to go down and get the note you dropped.")
         print()
         note = 1
         choice9 = input("You finally reach the bottom of the pit. The note is down here. Go pick it up.\nDo you want to read it?\n[1]yes \n[2]no?\n")
         if choice9.lower() == "1" or choice9.lower() == "yes":
           print("1442")
           time.sleep(2)
           print("After a few seconds of looking at the note, it vanishes.")
           note = 0
         else:
           print("You decide that reading the note that you risked your life for isn't important")
      
         print("You continue walking.")
         print("....")
         print("The Evil Bruh sure does like neverending halls. There's no turning back, so you walk for at least 30 minutes until you're met with a door.\nIt looks like you need to enter a code. Maybe that note will be useful.")
         if note == 1:
           print("The note reads: 1442")
           time.sleep(1)
           choiceD = input("Enter the Code: ")
           if choiceD == "1442":
             print("The door opens and you're met with the Evil Bruh. He puts a finger to your temple and you're met with darkness.")
             done = True
           else:
             print("A loud beep sounds through the rocky hall. You look around to see where it's coming from, but are met with a dart shot into your chest. Suddenly, you faint.")
             done = True
         else:
           print("You no longer have the note.")
           choice10 = input("Enter the code: ")
           if choice10 == "1442":
             print("The door opens and you're met with the Evil Bruh. He puts a finger to your temple and you're met with darkness.")
             done = True
           else:
             print("A loud beep sounds through the rocky hall. You look around to see where it's coming from, but are met with a dart shot into your chest. Suddenly, you faint.")
             done = True
