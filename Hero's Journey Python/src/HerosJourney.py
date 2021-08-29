"""
----------------------------------------------------
Code: https://www.codeavengers.com/python/7#1.1     
----------------------------------------------------
English: Interactive Hero's Journey Presentation 
Nov 26, 2018
Phoebe S.
#Current Version
Note: Exit this world with "0" at any time
----------------------------------------------------
"""
import random


































lose = int(0) #start at 0. if = 1 -- death sequence
parent_happy = 0 #starts unhappy

start_choice = int(input("Start the adventure (1). Listen to the true story (2)."))

if start_choice == 1: # run the adventure
  print("The Beginning:")
  
  gender = int(input("Are you male (1) or female(2)?"))
  
  while gender == 1 or gender == 2: #exit any var with 0 (except name)
      
      print("Unfortunately, you do not get to choose who you are born as in this world.\n\nYou are a 15 year old daughter, and the youngest of the 3.\nYou have a loving mother and father, as well as a few brothers.\nThe youngest one being no older than 6 years old.")
      
      #"""SKIP--TESTER
      print("But the world is on the verge of war...")
        
      name = input("While you cannot choose who you are born as, you may choose who you become.\n\n What is your nickname?")
      print(name + "? Excellent. Now we can truly begin.")
        
      wake_up = int(input("\"" + name + "! Wake up\" said your father.\nHow do you respond? 1 = \"5 more minutes...\" or 2 = \"I don't want to...\""))
        
      if wake_up == 0: # exit
          break
        
      if wake_up == 1 or wake_up == 2: # refusal
          
          print("\"He gave a short laugh. Aren't you excited for your big trip?\" he asked.")
      # end if . wake up
      
      

      print("Before you can reply you hear shouting down the street.\nYour father's face turns pale. \"Pack your things. Now.\" He said as he hurried out the room.\nYou pack your few belongings as quickly as possible.\nBefore you finish you see armed men enter your house.\n\nThey force you and your family outside into the street.")
      
      print("You see your mother, already with tears in her eyes.\nYou make eye contact with your father, seeing the fear in his eyes.\n\nYou are the last thing he sees before the armed man shoots him at point blank. ")
      
      print("Tears form in your eyes and you hear your youngest brother start to cry.\n\nHis weeping is quickly silenced.")

      print("Within seconds the rest of your brothers are shot.\nThen without a word, the soldiers leave and move on to the next house.")
      

      print("You, your mother, and sisters head back inside.\nYour mother, shaking, tells you to finish packing and leave now before they return.\nYou rush to grab your personal belongings. But will need something else for the trip.")
        
      #SKIP--END TESTER """ 
      item = int(input("""What will you take with you?
      1 = Food supplies (food, water, a knife, matches, a pan). 
      2 = Camping supplies (first aid kit, map, sleeping gear, a flashlight)."""))
        
      if item == 0: # exit
        break
        
      if item == 1: #food
          print("You rush in to grab the food supplies before leaving.\n\nFOOD SUPPLIES WAS ADDED TO YOUR INVENTORY.")
      elif item == 2:  #camp gear
          print("You rush in to grab the camping supplies before leaving.\n\nCAMPING GEAR WAS ADDED TO YOUR INVENTORY.")
      # end if. item
    
      print("On your way out, your mother gives you all the money she and your father have been saving up for you to leave the country and seek safety.\nShe gives you your ID papers and tells you how to get to the boats heading to a country across the ocean.\nYou give your mother and sisters a brief and tearful farewell.\nYou wonder if you will see them again one day...\n\nYOU GAINED + 1 MONEY.\nTHE ID PAPERS WERE ADDED TO YOUR QUEST ITEMS.")
      #------------------------------------------------------------
      solider_choice = int(input("On your way to the boat you see some armed soldiers in the street, looting a house. They are coming your way.\n\nWill you:\n(1) Run past them, and risk being spotted.\n(2) Hide in an alley till they pass by. You don't know how long they will be around and may miss the boat.\n(3) Try to take a different route. But you might get lost."))
        
      if solider_choice == 0: # exit
        break
      
      if solider_choice == 1: #run
        print("You run as hard and silently as you can while they aren't looking. As one of them turns around they spot you and shoot.")
        
        shot = random.randint(1,3) #hit or miss. 1 in 3 chance
        #print(shot)#console
        
        #shot = 2 #TESTER --auto miss
        
        if shot == 1: #hit
          print("They aimed well and hit you twice.\n\nTHE ENEMY DEALT 100 DMG. \nAlmost immediately you bleed out to death.")
          lose = 1 #game over
          break
        else: #miss
          print("You hear a few bullets clash into a window next to you but don't stop running. You run for the boat and somehow make it to safety.\n\nYOU GAINED +1 SPEED POINT.")
        #end if. run. hit or miss
      
      elif solider_choice == 2: #hide
        print("You wait in a nearby ally, staying well hidden and wait for them to pass by.")
        
        hide = random.randint(1,4) #hide. 1 in 3 chance
        #print(hide)#console
        
        if hide == 1: #miss the boat
          print("They took a while looting before they moved on. As you make it to the port you see the last boat has already taken off. You remain trapped on this land, and sooner than later...")
          lose = 1 #game over
          break
        
        else: #made it
          print("After a short time, you see them pass by. Without being noticed you run back onto your route and make it just in time, as the boat is preparing to head off. \n\nYOU GAINED +1 STEALTH POINT.")
        # end if. hide
        
      elif solider_choice == 3: #another route
        print("You turn around and try to find another path to the port.")
        
        if item == 1: #food. no map
          print("Without a map or compass you become completely lost. You ask a few people where the port is but end up at the wrong one. You try to find your way home, but remain trapped on the land until you run out of food.")
          lose = 1 #game over
          break
          
        elif item == 2: #camp gear. map
          print("Thankfully you have your map and travelling gear and manage to find a safer path to get to the boat in time.")
        #end if. route
      # end if. solider_choice
          
      #-----------------------------------------------------------------  
      print("You board onto the boat that is over crowded with people. You know this is going to be a long ride.\nBy nightfall, you are starving.\nYou see a boy even younger than you with their mother. He looks starving.")
      
      if item == 1: #food. no kit
        food_share = int(input("""Will you share some food with him?
        1 = Yes. Risk starving to help another.
        2 = No. There is barely enough food for myself."""))
          
        if food_share == 0: # exit
          break
      
        if food_share == 1: #give food
          print("Despite your tummy growling, you give up the last of your food. The mother looks grateful to you.\nYou don't know how long it will be until you come across more food. But hope you can make it through the night.")
          parent_happy = 1 #is happy

        elif food_share == 2: #dont give food
          print("You feel a bit guilty but know that your parents risked everything to get you this far. You can't risk starving to death now.")
        #end if. food share
          
      elif item == 2: # med kit. no food
        print("You don't have any food for yourself, much less some to share. You hope the two of you will survive.")
      #end if. item.
      
      if item == 2 or food_share == 1: # shared food or did not bring food
        starved_to_death = random.randint(1,3)
        #print(starved_to_death)#console
          
        if starved_to_death == 1: #starved
          print("The boat had to take a detour, adding extra days to the journey. Without any food, you die of starvation.")
          lose = 1
          break
        
        else: #not starved
          print("You remained hungry the rest of the ride there but make do.")
        #end if. starved to death
      
            
      if item == 2 or food_share == 2: # did not share food
        print("The next day the boy looks sick.")
          
        if item == 2: #med kit
          med_kit = int(input("""Will you use the med kit to help him?
          1 = Yes, I will do what I can.
          2 = No, I might need it later."""))
            
          if med_kit == 0: # exit
            break
      
          if med_kit == 1:
            print("You offer your med kit and do what you can for the child. He looks a little better and the mother is thankful to you.")
            parent_happy = 1 #is happy
            
            injured_to_death = random.randint(1,3)
            #print(injured_to_death)#console
          
            if injured_to_death == 1: #injured 
              print("The next day the weather took a turn for the worse. The boat sailed across violent waves. \nYou were thrown across a room with enough force to shatter a large glass mirror and became injured in the process. Without proper medical supplies, you slowly bleed out to death.")
              lose = 1
              break
            else: #not injured 
              print("You manage to make do without the medical supplies.")
            #end if. injured
            
          elif med_kit == 2:
            print("You feel a bit guilty but know that your parents risked everything to get you this far. You can't risk giving away a med kit now.")
          #end if. use med kit
        #end if. had med kit
      #end if. did not share food
      
      #------------------------------------------------------------
      #player survives and goes to new land
        
      print("After a long journey, you arrive from your homeland and end up in the new country.\nSomeone greets you: \"Хто ти?\"\nYou have no idea what they said.\nYou tell them your name is " + name + ".\nThey have no idea what you said.\nYou show them your ID papers.\nYou still don't know what's happening but they lead you and the others from the boat into a tiny village.\nSomehow this becomes your new home and your name is now \"Селія\".\n\nTHE ID PAPERS WERE REMOVED FROM YOUR QUEST ITEMS.")
        
      if parent_happy == 1: #helped child -- good ending
        print("You see the boy you helped and his mother. You ask if you can stay with them for a while. The three of you share a shelter until you find a job and are able to support yourself.")
      
      else: # parent = 0 
        print("You wander around the new village. You see the boy's mother, but not the boy.")
        
        if item == 1: #food
          print("Eventually you come across an odd man who is interested in buying your food supplies from you for a high price.")
        elif item == 2: #med kit
          print("Eventually you come across an odd man who is interested in buying your med kit from you for a high price.")
        #end if. item
        
        sell = int(input("He insists that he will give you the money later, if you let him take your supplies with him for now. You don't think you've seen this man before and can't remember if he was on the boat with you. He is offering enough money to help you on your feet in this new world. But it will cost you dearly if he's lying. \n\nWill you give your items to this man? \n1 = Yes. Sell to the man. \n2 = No. I don't trust him."))
        
        if sell == 0: # exit
          break
        
        if sell == 1: #yes 
          print("You agreed to let him take the supplies for now.")
          
          truth = random.randint(1,2)
          #print(truth)#console
          
          if truth == 1:
            print("The next day, you still haven't seen him and wonder if he will ever come back.")
            print("By night fall, he returns with lots of money! He thanks you for trusting him, and tells you that his family needed your supplies instantly and that there wasn't enough time for him to grab the money the other day.") #good ending. 
          elif truth == 2:
            print("You never see the man again or his money.\nPerhaps he couldn't find you or never intended to pay you back. \nEither way, without any money, survival items, friends or family, you find it very difficult to survive in the new world. \nAfter a few days, maybe weeks...") 
            lose = 1
            break #lose
          #end if. truth
        
        elif sell == 2: #no
          print("You did not trust the man and took your items back from him.\nHowever, with no money, friends or family, you find it difficult to survive in the new world. \nAfter a few weeks, maybe months...")
          lose = 1
          break # lose
        #end if. sell
      #end if. parent happy or not
        
      #-----------------------------------------------------------------  
      #THE GOOD ENDING
      print("You grow up in the new country. \nYears later you have a job as a seamstress, a home, and even met a romantic partner.\nBetween the 2 of you, you gain enough money to bring one of your sisters over from your homeland.")
        
      family_saved = int(input("Who will you bring over? \n1 = The younger sister. \n2 = The older sister."))
        
      if family_saved == 0: # exit
          break
        
      if family_saved == 1:
          print("You send over enough money for your younger sister to come over.\n\nYOUR YOUNGER SISTER HAS JOINED THE PARTY.")
      elif family_saved == 2:
          print("You send over enough money for your older sister to come over.\n\nYOUR OLDER SISTER HAS JOINED THE PARTY.")
      # end if. family 1
            
            
      print("The company of your sister fills you with joy. It has been many years since you've seen anyone from your old life.\nBetween the 3 of you, you save up enough money to bring over one more person. But will you?")
            
      family_saved2 = int(input("""Who will you bring over next? 
      1 = Your other sister. 
      2 = Your ma.
      3 = Save the money. They will be fine..."""))
    
      if family_saved2 == 0: # exit
          break
          
      if family_saved2 == 1 or family_saved2 == 2: #saved a 2nd person
          if family_saved2 == 1:
              print("You send over enough money for your other sister to come over.")
          elif family_saved2 == 2:
              print("You send over enough money for your ma to come over.")
          #end if. ma or sis
            
          print("Unfortunately, the world is still in a time of conflict.\nThe new land rejected their boat. As did many other countries.\nShe ends up in Argentina, and you never see her again. But at least she's alive.")   
       
      elif family_saved2 == 3: # did not save a 2nd person
          print("You decided to save your money, continue your new life here, and hope the best for them.")
        # end if. family 2
        
      print("You and your partner grow old in the new land, and end up raising 2 kids. Your adventure is coming to an end. But for them this is just\n\nThe Beginning.")
      break
  #end while
  
  
  #bad out comes 
  if lose == 1: # lost/died
    print("Y O U  D I E D.")
    try_again = int(input("Want to try again? \n1 = Ya. \n2 = Rage quit."))
    
    if try_again == 1: #yes
      print("Your story will begin anew...") #reload program
    elif try_again == 2: # no
      print("You remain dead and now cease to exist. Have a nice day.")
    #end if. try again  
  #end if. lose  
    

elif start_choice == 2: #tell the story
  #story
  print("""INTRO

This interactive hero’s journey was based on some true events that my great grandma, Celia, had faced.

I never knew my great grandma so I only know what my mum remembers. We don't know much about her before the age of 15 or any exact years of these events. However, they all would have taken place throughout her life time which was before, during, and after WW2.

The interactive story was about the protagonist fleeing from their homeland to a country across the ocean. I wanted to mimic the feelings of not understanding what the people in the new country were saying and receiving a name you don't understand. So I used Google Translate to say “who are you” in Ukrainian, when you were greeted. Then I translated “Celia" for the new name. (But it may not be accurate).

This journey took you into the Ukraine, but the real journey started from Ukraine and ended in the United States.""")

  print("""THE ORDINARY WORLD

Celia was part of a jewish family. She had 2 older sisters, a mother and father, and a few brothers. 

At the time, there were soldiers in the Ukraine called the “Pogroms” who were against jews. So they came into their houses, shot the males, and took away women, to be raped.

Celia was the youngest sister so she was the most likely be taken away. So her parents had raised enough money to help her leave the country to go to the US, where it would be safer for her. """)

  print("""THE ORDEAL/THE CALL/THE REFUSAL

Her story starts with the traumatic experience acting as a call. 
However, there wasn't any way for her to refuse this call because she had to get to safety.

At the age of 15, the Pogroms came and took her father and brothers out of the house and made her watch as they got shot. She had to leave before they could come back. She only took with her the few things she had and a bit of money. She joined many others who were escaping on a large boat to the States.""")

  print("""THE MENTOR

I would consider Celia's mother as her mentor since she provided the money and told her where to go and how. """)

  print("""CROSSING THE THRESHOLD/BELLY OF THE BEAST

In this case, crossing the threshold was her crossing the ocean/border into the USA. When they got to the United States, they were in some jewish area called the “Ellis islands”. 

Once she landed, she was in the belly of the beast, since she was in a new world with ideals and a language unknown to her, which lead to some issues. """)

  print("""TESTS/ALLIES/ENEMIES/APPROACH
  
The first challenge, was her journey by boat into a new country. She was likely completely alone, and had no allies at this time.

The next challenge was once she landed, none of the Americans understood their language. So the US citizens became both a friend and foe.

The Americans were an ally by allowing the Ukrainian boat into safety, where people could start a new life. But the Americans were also a new enemy because they had the Ukrainians live in a small village area, and gave them new names that only the Americans could understand.

Celia's next test was surviving/adapting in the new world, and getting a job to support herself. She did this by growing up in the US, and started working as a seamstress, where she meet her first husband (who was a tailor). He became like an ally to her. 

Finally, she tasked herself to make enough money to bring family over to the US.""")

  print("""REWARD

Together, her and her husband had saved up enough money to bring over the second youngest sister (who was the next most likely to be taken away).

Her sister also became a seamstress and they all worked on getting their final sister over into the States. """)

  print("""THE ROADBACK/THE REFUSAL

Celia did not want to return to the Ukraine for obvious reasons. But she also stayed in the US for the rest of her life because she was afraid that if she left, they wouldn’t let her back in. 

While she did not physically return back to where she came, she was on the road back to familiarity and having a family.""") 

  print("""RETURN WITH THE ELIXIR
  
The three of them had managed to save up enough money to bring the third sister to the States.

However, it was very difficult for the 3rd sister to leave the country. This was after WW2 and no country was accepting jews including USA, Canada, Europe, and England. The only place that accepted them was Argentina (who was also letting in Nazis).

So Celia never saw her oldest sister, but she did live. """)

  print("""RESURRECTION
  
At some time, Celia's first husband had died and she eventually found another one. """)

  print("""EPILOGUE 
  
Celia never got her mother into the States either, but she faced no further threat from the Pogroms because she was too old for them.

Celia got to build a new life and had 2 kids with her first husband.""")

  print("""SOURCES:
  
My mom.
""")

else: # exit
  print("Goodbye.")
#end if. start choice
#END PROGRAM

"""
TRANSFORMATION--From what I hear she wasn't the nicest person, which is likely an after effect from her traumatic childhood of watching her family shot, and crossing into a new country, alone at the age of 15.

On the boat, there may have been some people who were could be considered allies nice to her since she was young, and they were all escaping for similar reasons, but we don't know for sure. """



