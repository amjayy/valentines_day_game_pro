from ringtone import club
from textwrap import dedent
def gender_choice():
    gender= ''
    while gender != "male" and gender !="female":
        gender = input("Which will you choose?") 
        print()

    return gender

def your_gender():
    you = ''
    while you != "male" and you !="female":
        you = input("Which will you choose?") 
        print()

    return you

def choose_now():
    choose = ''
    while choose != "glare" and  choose !="apologize":
        print("You stare into space not doing anything for a long time. The couple look concerned but,  frightened.")
        print("They move into the back of the train.")
        print("You stay staring for so long that when the train stops. You are escorted off by some friendly people in white jackets.")
    return choose
def your_ride_home():
    ride = ''
    while ride != "mom" or ride !="friend":
        print("Well, I guess you're going to walk home.")
    return ride





print("""The train ride home is long, but at this hour it is peaceful. You have just return from a year in Fort Benning for basic training.You are tired, but proud of yourself. You are not the same person who left.
    The sound of wailing babies has ceased and the noisy people on their phones are no more.
    Besides you and an older couple. The train is quite bare . You are about to doze off to sleep when...""")

club.phone_ringing()

print("You quickly shut off your phone. You silently curse yourself for being still stuck in 2010 still using songs as ringtones.")
print("You give the couple on the train an awkward smile.")
print("""But, the still couple looks over at you in disapproval.What do you do? Do you  glare back or apologize?""")

choice= input("> ")

if  choice == "glare":
    print("You glare at the couple.")
    print("Who cares? This is your phone. You pay the bill.")
    print(" The old woman gasps and mumbles something under her breath that you can not hear.")

    print(""" You decide to check who called you. You have two missed calls and two messages from your childhood friend and your mother.
By the way, is your childhood friend a male or a female?
""")
                
if choice == "Apologize":
    print("You apologize and their expression softens. They leave you alone after accepting your apology")

    
        
    
print(" You decide to check who called you. You have two missed calls and two messages from your childhood friend and your mother.")

print("By the way, is your childhood friend a male or a female?")

gender = gender_choice()

print("By the way, what is your gender ?")
you = your_gender()

print("Who do you want to pick you up from the station?")
ride = your_ride_home()

person = input("> ")

if ride == "mom":
    print(dedent("""
    About 15 minutes later, your train ride comes to a stop. You grab all your items and slip your phone into your pocket.
    You bound off the terminal to see your mom standing there with a large teddy bear that's holding a red heart. 
    You grin and run to you mother. She asks you where you want to eat at before going to the neighborhood. What do you choose?
    """))

elif ride == "friend":
    print(dedent(""" About 15 minutes later, your train ride comes to a stop. You grab all your tiems and slip your phone into your pocket. You are
    about to bound off the terminal when you hear some a familiar loud country voice shout out. "What's good biscuit head?" You whip around in
    excitement. Your shoulders sag in slight disappointment. It isn't them, but it's only their sibling. A great friend as well, but you thought..
    Wait a second, what was the person you were expecting's name?
    """))

else:
    print("You fail to text back anyone, so they assume")