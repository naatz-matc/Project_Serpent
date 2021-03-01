#!/usr/bin/env python3

print ("Please enter your name: ")

YourName = input(" ")
print ()
print (f"Hello {YourName}, pick two of your very \n" \
        "best friends and enter there names:")
print ()
Friend_1 = input("Friend 1-> ")
print ()
Friend_2 = input("Friend 2-> ")
print ()
print (f"""You have just escaped your holding cell after your
failed attempt to storm Area 51 with your friends {Friend_1}
and {Friend_2}. You reach the end of a dark, dimley lit hallway
with three doors. You must choose a door to go through. Which door
do you choose? door #1, door #2, or door #3?""")
print ()
door = input("-> ")
print ()

#========= Door #1 Logic ============

if door == "1":
    print ("You have stubmled into an alien autopsy room with \n" \
           "a real live alien waiting to be disected.")
    print ("What do you do?\n")

    print ("1. Find the key and set it free")
    print ()
    print ("2. Reach for the bonesaw, its time \n" \
           "to see whats inside these creatures!")
    print ()
    #========== Alien Logic ===========
    alien = input("-> ")

    if alien == "1":
        print ("The alien seems grateful after you set it free. It \n" \
               "reveals itself to speak English and offers to take \n" \
               "you on a trip to explore the universe and relocate to \n" \
               "its home planet and highly advanced society. What will you do?")
        print ()
        print ("1. Peace out Earth!")
        print ()
        print ("2. No thanks, I would miss my family and friends too much")
        print ()
        vacay = input("-> ")
        print ()
        if vacay == "1":
            print (f"Live long and prosper {YourName}, nanu nanu!")
            print ()
        elif vacay == "2":
            print ("The alien understands and as a token of appreciation it \n" \
                   "rewards you with the glove of Thanos with the complete set \n" \
                   "of infinity stones!!!")
            print ()
    elif alien == "2":
         print ()
         print ("As you begin the disection the alien emits a supersonic \n" \
                "scream that alerts both the soldiers on the base and the \n" \
                "waiting alien armada orbiting the earth. As you are being \n" \
                "detained by the soldiers the alien invasion force descends \n" \
                "upon Area 51, vaporizing everyone with their high tech weaponry \n" \
                "and begin the process of conquering the world and enslaving the \n" \
               f"human race. But why should you care {YourName}, YOUR ALREADY DEAD!!!")
         print ()
#========== Door #2 Logic ===============

elif door == "2":
    print (f"You discover that your friend {Friend_2} has also escaped and you both \n" \
            "find yourselves in the top secret aircraft hanger with dozens of experimental \n" \
           f"aircraft just waiting for you. Fortunately for {Friend_2} and you everyone is \n" \
            "at lunch so you both decide to hop in one of the aircraft. You notice two \n" \
            "unique buttons in the cockpit, one colored red and the other colored yellow. \n" \
            "Which button do you press?")
    print ()
    print ("1. Red")
    print ()
    print ("2. Yellow")
    print ()
    button = input("-> ")

    if button.lower() == "1" or button.lower() == "red":
        print ()
        print ("The aircraft powers on and starts to operate on its own. The cockpit \n" \
               "closes and you are strapped into your seat. You are scared beyond belief \n" \
               "as the hanger door opens and the jet engines begin to spool. You begin to \n" \
               "zone out and are oblivious to the world around you. You hear a noise coming \n" \
              f"from behind you and realize it is {Friend_2} telling you that this is not \n" \
               "any aircraft, it is a TIME MACHINE! As the aircraft takes off you ponder where \n" \
               "and WHEN you will end up as you end up passing out from G forces you encounter \n" \
               "before you travel through time.")
        print ()
        print (f"When you come to you realize that you and {Friend_2} have traveled back in time \n" \
                "to the Jurassic Period of prehistory. The aircraft was severly damaged during the \n" \
               f"journey and is unrepairable. You and {Friend_2} realize that you are now stuck here \n" \
                "forever. In an attempt to lighten the mood you say 'at least now I dont have to pay \n" \
               f"the rent'. {Friend_2} slaps you in the face and walks away looking for something to eat.")
        print ()
    else:
        print ()
        print (f"You have just enabled stealth mode on the aircraft. You and {Friend_2} are completely \n" \
                "invisible to everyone else around. In your excitement you begin to press other buttons and \n" \
               f"accidentally hit one that ejects you and {Friend_2} from the cockpit. This alerts the \n" \
                "soldiers and you both are reaprehended and transported to Area 666, where you are never \n" \
               f"heard from again. I hope it was all worth it {YourName}!")
        print ()

#=========== Door #3 Logic ===============

elif door == "3":
    print (f"You discover your friend {Friend_1} in an experimental bio-chamber, where it appears the \n" \
           f"government has begun horrifying gene editing experiments on them. {Friend_1} is barely \n" \
            "recognizable anymore and you are overcome with heartbreak. You walk over to the control \n" \
           f"panel for {Friend_1}'s pod. You contemplate on whether to release and rescue them or turn \n" \
           f"off the life support and ending the experiments, and at the same time, {Friend_1}'s life. \n" \
            "Which option do you choose?")
    print ()
    print (f"1. Release {Friend_1} and begin the reanimation process")
    print ()
    print ("2. Turn off the pod and end the experiment")
    print ()
    heartbrk = input("-> ")
    if heartbrk == "1":
        print ()
        print (f"As you rescue {Friend_1} from their pod and begin to revive them, they suddenly \n" \
               f"awake from their slumber. {Friend_1} opens up their three eyes and spins their head \n" \
               f"nearly 360 degrees to observe the surroundings. {Friend_1} looks at you and for a \n" \
                "brief moment there is a smile on their face. This is short lived, however, as a few \n" \
               f"seconds later all three of {Friend_1}'s eyes turn blood red and as they open their \n" \
               f"mouth to reveal razor sharp teeth! {Friend_1} has completely transition into a monster! \n" \
                "They pin you down with their Wolverene-like claws and impale you with it's scorpion-like \n" \
                "tail. You slowly fade to black as you see your former friend escape from the laboratory.")
        print ()
    elif heartbrk == "2":
        print ()
        print (f"After coming to terms with what you must do, you shut down power to your friend {Friend_1}'s \n" \
                "pod. As you watch the remaining life drain from what is left of their body, you are overcome \n" \
               f"with grief and sorrow. You begin to cry uncontrollably as the monitor broadcasts {Friend_1}'s \n" \
                "final heartbeat. You sit on the floor for a while reminiscing all of the good times that you \n" \
               f"and {Friend_1} had together.")
        print ()
        print (f"Cheer up {YourName}, because after grieving for some time you manage to escape from Area 51 \n" \
                "and expose to the world the horrors of what goes on there. You rally enough public support to \n" \
                "have the facility shut down and the perpetrators charged with crimes against humanity in \n" \
                "international court. There convictions and life sentences are a victory for all mankind. \n" \
               f"You are now at peace knowing that {Friend_1}'s death was not in vein.")
        print ()
