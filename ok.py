
print("""The train ride home is long, but at this hour is peaceful. You have just return from a year in Fort Benning for basic training.You are tired, but proud of yourself. You are not the same person who left.
    The sound of wailing babies has ceased and the noisy people on their phones are no more.
    Besides you and an older couple. The train is quite bare . You are about to doze off to sleep when "Club" by Dej Loaf breaks the silence of the train.
    The couple looks over at you in disapproval.
    """)




reaction = input("> ")

if reaction == "1":
    print("You turn around and ")
    print("What do you do?")
    print("1. Glare.")
    print("2. Apologize.")

    choice= input("> ")

    if  choice == "1":
        print("You glare at the couple.")
        print("Who cares? This is your phone. You pay the bill.")
        print(" The old woman gasps and mumbles something under her breath that you can not hear.")
                
    if choice == "2":
        print("You apologize and their expression softens.")
    else:
        print("You stare into space not doing anything for a long time. The couple look concerned but,  frightened.")
        print("They move into the back of the train.")
        print("You stay staring for so long that when the train stops. You are escorted off by some friendly people in white jackets.")
        
print(""" You decide to check who called you. You have two missed calls and two messages from your childhood friend and your mother.
By the way, is your childhood friend a male or a female?( 1 for male or 2 for female)
""")

def gender_choice():
    gender= ''
    while gender != "1" and gender !="2":
        print("I did not catch that. Please type choose: 1 for male or 2 for female")
        gender = input("Which will you choose?") 
        print()

gender_choice()