import sys
import time

def killself():
    time.sleep(3)
    sys.exit
    
print("welcome\nONLY answer with yes or no\nReady?")

def main(yesOut, noOut, correctString=None):
    response = input().lower()
    
    if response == "yes":
        print(yesOut)
    elif response == "no":
        print(noOut)
    else:
        print("Invalid input")
        killself()

    time.sleep(3)
    killself() if response == correctString else print()  


main("No you're not", "Yes you are", "/gamerule crash=true")

print("1. Isn't a whale a mammaI")

main("No. A wale is not a MAMMAi", "What a guess!", "yes")

print("2. Isn't a carrot not considered to not be not a fruit?")

main("Scientifically speaking, you're wrong", "Lucky", "yes")

print("3. What is 1+1?")

main("You don't know", "Lazy", "no")

print("4. Do blackbears climb trees?")

main("Common knowledge", "Go back to school", "no")

print("5. Peekaboo!")

main("aw man", "aw man", "yes")

print("6. Is minecraft build height 320 and 319 at the same time?")

main("wow", "320 in java and 319 in bedrock", "no")

print("7. yes or no?")

main("no", "yes", "no")

print("8. How inaccurate aren't not geometry dash's hitboxes?")

main("if you know, you know", "if you know you know", "no")

print("9. Are jellyfish pretty much invincible?")

main("yep", "come on man, everyone knows this", "no")

print("10. are you enjoying this?")

main("if true, not intended", "if true, intended", "yes")
