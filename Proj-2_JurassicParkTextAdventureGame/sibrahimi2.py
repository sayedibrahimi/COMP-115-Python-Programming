# Assignment: (#2):
# Author(s): Sayed Abdul Ahad Ibrahimi
# Due Date: (10/18/2021)
#
# Description: The goal of this project is about Selections/Conditionals which includes Boolean Values and Boolean Expressions, Logical Operaters, Boolean Functions. 
#              The programmer delivers the story through python using functions and selections. 
#              The programmer can call a function from another function which in turn call another function! So, the programmer may avoid using global variables. 

# Comments: (In this story, Nico and Chris are my actual friends. They and some of my other friends too have played with this story. 
#            The locations are actual part of the map based on the Jurassic Park/world movies. I wrote down the story in pages of notebook, 
#            I mind mapped the entire story at white board, I started typing the down the structure and finally the dialogues and some dramatic scenes. I spent a full week. 
#            At first, I was afraid that I may not be able to implement (code) the mind map but it took me around 4-6 hours to finish the entire code without the dialogues and debugging.  
# Honor Pledge: I have abided by the Wheaton Honor Code and
# all work below was performed by (Ahad Ibrahimi).

import random
   
# You land on the island and welcomed by the officials!

def Welcome():
    
    print("\nWelcome to Jurrasic Park!\n")
    name = input("Please confirm your name on the tickets: ")
    print(f"\nWelcome {name}! Please make sure you have read the emergency instruction below: \n".format(0)) 
    print("Incase of Emergency, always ask/follow the authorized personel. Thank you and Enjoy your visit!\n")
    option = int(input("Please select from one of the available tourist areas in the map to begin your tour.\n\n"
                       "1) Jeep tour through grass lands.\n"
                       "2) Sorkin's Lab (breading zone).\n"
                       "3) Tour through Jungle Oasis.\n"))
            
    if option == 1:
        Scene1(name)
           
    elif option == 2:
        print("Welcome to Sorkin's Lab! Please take your assinged seats!\n"
              "\nAhem! Hey! I am Nico and I am here with my brother Chris, he is in the Jungle Oasis tour!\n"
              f"Nico: ohk! Nice to meet you {name}!\n".format(0))
        PanicMode()        
        Scene2(name)
            
    elif option == 3:
        print("Welcome to Jungle Oasis!\n" "Please take your assinged seats!\n"
              "\nAhem! Hey! I am Chris and I am here with my brother Nico, he is in the Grass Lands tour!\n"
              f"Chris: Nice to meet you {name}!\n".format(0))
        PanicMode()
        print("*Everyone Starts Desperatly Running and Scattering Out*\n" "\nChris: we need to run to one of those buildings and take shelter right now!\n")
        Scene3(name)

#----------------------------End of Welcome Function----------------------------

# things go south real quick!

def PanicMode():
    
    print("*EEEEEEEEEOOOOEEEEEEEOOOOO* *A LOUD Siren goes off!*\n"
          "Security Personnel: Everyone! Stop Panicking! Do NOT Leave Your Seats!\n"
          "\n*SCREAMS* *CRY* *AHHHHHHHH!* *whats happening?!* *WE ARE All GONNA DIE!*\n")

#------------------------End of PanicMode Function------------------------------

# You are introduced with Chris and Nico!

def Scene1 (name):
    
    print("Welcome to grass lands! Please take your assinged seats!\n"
          "\nAhem! Hey! I am Chris and this is my brother, Nico!\n"
          f"Nico: Nice to meet you {name}!\n".format(0))
    PanicMode()
    option = int(input("1) Sit tight in the Jeep?\n"
                       "2) Leave the Jeep?\n"))
    
    if option == 1:
        print("*After a 20 min drive*  " "*At the Sorkin's Lab*\n"
              "\nNico: ARGHHH! I think my shoulder is displaced!\n"
              "My brother was pushed away by the crowd out of the Jeep!\n")       
        Scene2(name)
    
    elif option == 2:
        print("*People running everywhere*   *SCREAMS*\n" "\nChris: Hey! Did you see my brother?" "I need to get back to where ever those Jeep were headed!\n" 
              "We need to run to one of those buildings and take shelter right now!\n")
        Scene3(name)
        
#--------------------------End of Scene1 Function-----------------------------

# You are with Nico. You need to survive while finding Chris and getting out of the island.
    
def Scene2(name):
    
    print("*Power goes off!*\n"
          "*Nearby Velociraptor*  GRRRRAAAWR!*\n"
          "\nNico: *Shaking* What was that sound?!\n"
          "We need to restart the power to get out of this building!\n")
    option = int(input("1) Find the switch to the power?\n"
                       "2) Run to the roof using the emergency stairs?\n"))
    if option == 1:
        
        odds = random.random()
        
        if (odds > 0.5):
            print("Nico: You found the switch to emergency power!"
                  "Now lets get the hell outta here!\n" "\n*Outside of the budiling*\n")
            DriveTo(name)
            
        else:
            print("Nico: How were you not able to find the switch for emergency power?\n" "\n*GRRRRAAAWR!* RUN!\n\n"
                  "Oh no! the doors are closed cuase of power cut!\n"
                  "Look! there are two grenades! Those might come in handy!\n"
                  "I found this key and we can use it to manually open the door!\n")
            option = int(input("1) Use the key?\n"
                               "2) Yolo! Use the Grenade?\n"))
            if option == 1:
                
                n = random.randint(1,2)
            
                if n == 1:
                    print("There we go! lets get out of this building now!\n" "\n*Outside of the budiling*\n")
                    DriveTo(name)
            
                else:
                    print("oh no! The key is not working!\n"
                          "Velociraptor can smell us from far distance, Run!\n"
                          "\n*At the greenhouse*\n")
                    option = int(input("1) Break the window using the emergency axe?\n"
                                       "2) Hide behind the boxes!\n"))
                    
                    if option == 1:
                        print("\n*Glass Shatters!*\n" "\nNico: lets go before we are eaten alive by the fricken Velociraptors!!\n" "\n*Outside of the budiling*\n")
                        DriveTo(name)
                    
                    elif option == 2: 
                        print("\nNico: AHHHHH!!! *SCREAM* *Vlociraptors found both of you and ripped your flesh while you were alive!*")
                    
            elif option == 2:
                print("Nico: NO! NO!   *Loud Explosion*  *BOOOOM*   *DUST & SMOKE*   *Coughs*   Nico: help me get outta here\n" "\n*Outside of the budiling*\n")
                DriveTo(name) 
                
    elif option == 2:
        print("*At the Roof*\n" 
              "\nNico: Look! There are two areial lifts at two different directions, one is towards East and the other one is to west.\n" 
              "We can use them to get out of this building!\n")
        option = int(input("1) Use the 1st Areial lift and head towards East?\n"
                           "2) Use the 2nd Areial lift and head towards West?\n"))
        if option == 1:
            
            odds = random.random()
             
            if (odds > 0.5):
                print("Nico: oh no! The lift is not moving! We are stuck above around 100ft from the ground!\n")
                option = int(input("1) Jump off of the lift?\n"
                                   "2) Wait for help to arrive?\n"))
                if option == 1:
                    print("Nico: Noooo!\n" "\n*You Suicided!*\n")
                
                elif option == 2:
                    print("\nYou Starved to Death!\n")
                
            else:
                print("*Beezzzzzed*  " "*Reached the ground level*\n" "Nico: help me remove this clif.\n" "\n*Outside of the budiling*\n")
                DriveTo(name)
                
        elif option == 2:
            print("Nico: *Above 50ft from the ground*  " "*SCREAMS* Look out!\n" "\n*You were stabbed by a Pteranodon! (a flying pterosaur)*\n")
            
#-------------------------End of Scene2 Function-------------------------------

# You need to find Chris while trying to survive!

def DriveTo(name):
    
    print("Nico: Look! There is a Jeep!  " "Lets check it out!\n" "It has the key!\n" 
          "\nDid you hear that!\n" "My brother sent me a radio message, he is waiting for me on a bridge close to Jungle Oasis!\n" "We need to save him now!\n")
    option = int(input("1) Drive the Jeep to Jungle Oasis?\n"
                       "2) Leave Nico and drive to Airport?\n"))
            
    if option == 1:
        print("*Engine turning on*  " "*Bugghghghg-VooooRRR*\n" "Nico: Hold up brother! I will be there soon\n" "\n*after 30 min drive*  " "*Jeep Stops*\n" 
              "\nNico: What the hell happened here! The bridge looks damaged!\n")
        option = int(input("1) pass through damaged bridge?\n"
                           "2) Take a different route through safari lodge?\n"
                           "3) Go to the Helicopter pad?\n"))
            
        if option == 1:
            print("Nico: Oh here we go!\n")
            MeetUp(name)                  
            
        elif option == 2:
            print("*You spot A HUGE Spinosaurus*\n" "\nNico: AHHHHHH!  Drive faster!!  Speed-up!\n"
                  "Nico: *SHOUTS* Should I use the other Grenade?\n")
            option = int(input("1) Yes!\n"
                               "2) No!\n"))
            if option == 1:
                print("*Loud Explosion*  *BOOOOM*  *Heavy Breathing*\n")
                MeetUp(name)
                        
            elif option == 2:
                print("Nico: *SCREAMS* *Aurghahaha* *You are torn apart inside Jeep by the Spinosaurus\n")
                        
        elif option == 3:
            JungleOasis(name)
        
    elif option == 2: 
        print("Nico: *SHOUTS*  " "You coward!  " "Dont leave me alone!\n" "\n*At the Airport*\n" "\n*AHHHHHHHH!!!*\n" "\n*You are swallowed by a T-Rex!*\n")
        
#---------------------------End of DriveTo Function----------------------------    

# You have made it with Nico and Chris alive!

def MeetUp(name):
    
    print("*After a while!*  " "Stop!" "  Look! there is my brother!!\n" "\n*Military Helicopters approching and landing for the rescue*\n" 
          f"\nChris & Nico: Lets go home {name}!\n" "\n*chakk-chackk-chak-chak, chak-a-chak-akk-chk-chk-chk*\n".format(0))    

#-----------------------------End of MeetUp Function----------------------------

# You are with Chris. You need to survive while finding Nico and getting out of the island.

def Scene3(name):
    
    option = int(input("1) Go to Insectorium lab to get help?\n"
                       "2) Go to infirmary?\n"))
    if option == 1:
        print("*At the Insectorium lab*\n" "\nChris: Can you explain what the hell is going on?\n" 
              "Security Personnel: Someone shutdown the power that runs the island and freed all the Dinosaurs.\n" 
              "Chris: *Shocked* Is that even possible?!\n"
              "Security Personnel: For now we are taking few people to emergency bunker, it is safe there.\n"
              "Chris: Where are you taking those people in the chopper?\n"
              "SP: Those are taken to the northern dock.\n"
              "Chris: WHAT! why are we not taken there!\n"
              "SP: Those are scienist and VIPs.\n"
              "Chris: Go to hell with your VIPS!\n"
              f"Chris: Hey {name}! I contacted my brother and he is waiting for me on Staff Apartments's roof, near grass land\n".format(0))
        option = int(input("1) Trust the personnel and go to Emergency bunker?\n"
                           "2) Sneak around and steal a Jeep!\n"))
        
        if option == 1:
            print("*At the Emrgency Bunker*\n"
                  "\nGeneral: Alright! Listen Up! We are taking all of you to the airport to get you out of this island.\n" "Now everybody get into the Jeeps right now!\n"
                  "\n*At the Airport*\n" "SP: Fire!" "\n*AHHHHHHHH!!!*  " "*people SCREAMING*\n" "\n*You are swallowed by a T-Rex!*\n")
            
        elif option == 2:
            print("Chris: Here! the map shows if we head East, there is a chopper there.\n")
            
            n = random.randint(1,2)
            
            if  n == 1:
                print("*After a While*\n" "\nThere is the chopper!  " "Lets go save my brother!\n" "*\nchakk-chackk-chak-chak, chak-a-chak-akk-chk-chk-chk*\n")
                MeetUp(name)
                
            else:
                print("*After a While*\n" "\nChris: The engine is dead!\n")
                option = int(input("1) Drive to another chopper showen on the map?\n"
                                   "2) Leave Chris and drive to aiport?\n")) 
                if option == 1:
                    print("*After a while*\n" "\nThere is the chopper!  " "Lets go save my brother!\n" "*\nchakk-chackk-chak-chak, chak-a-chak-akk-chk-chk-chk*\n")

                elif option == 2:
                    print("Chirs: *SHOUTS*  " "NO!!  Why are you leaving me behind!" "\n*At the Airport*\n" "\n*AHHHHHHHH!!!\n*" "\n*You are swallowed by a T-Rex!*\n")             
                    
    
    elif option == 2:
        print("*Pitch Black*\n" "\nChris: oh NO! we shouldnt have come here!\n"
              "\n*Nearby Velociraptor*  GRRRRAAAWR!*\n"
              "Chris: Run to basement!\n")
        option = int(input("1) Run to Basement?\n"
                           "2) Stay put!\n"))
        if option == 1:
            print("Chris: The doors of basement locked up!  We can't get out now!\n")
            
            n = random.randint(1,3)
            
            if n == 1:
                print("*You Starved to Death!*")
                
            elif n == 2:
                print("*You suffocated to death due to leaked pisonuse gas!*")
            
            else:
                print("*The basement ran out of air and you suffocated to death!*")
        
        elif option == 2:
            print("\nChris: AHHHHH!!! *SCREAM* *Vlociraptors found both of you and ripped your flesh while you were alive!*")
                

#-----------------------End of Scene3 Function----------------------------------                

# You need to find Chris while trying to survive!

def JungleOasis(name):
    
    print(" Nico: We need to to go get my brother before we leave the island!\n" "I am not getting into that chopper without him!\n")
    option = int(input("1) Save Chris?\n"
                       "2) Ditch Nico?\n"))
    if option == 1:
        MeetUp(name)
                
    elif option == 2:
        print("*chakk-chackk-chak-chak, chak-a-chak-akk-chk-chk-chk*\n" "\nNico: *SHOUTS*  " "Where are you going, you coward!  " "Come Back!\n")
        option = int(input("1) Land the Chopper?\n"
                           "2) Move On?\n"))
        if option == 1:
            print("Nico: I knew you were gonna return!  " "Thank you! " "I owe you my life!\n")
            MeetUp(name)
                    
        elif option == 2:
            print("Nico: NOOOOOO!!\n" "\n*YOU GOT OUT!*\n")
                   
#------------------------End of JungleOasis Function---------------------------       

def main():
    
    Welcome()
    
if __name__ == "__main__":
    main()
        

            
    