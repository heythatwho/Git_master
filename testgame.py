print("welcome to the hell, good luck ;)")
# whatever...
name =input("type your name here ")

while True:
    try:
        age=int(input(f"hello {name} ;)  type your age here " ))
    except ValueError:
        print("input number, please")
        continue
    else:
         #age was successfully parsed, and we're happy with its value.
        #we're ready to exit the loop.
        break
print("Hello ", name, "you are ", age, "years old. ")
health =10

print(f"you are starting with {health} health.")
        
if int(age) <12:
    print("huh,too young too simple... ghost inside, go away ")
elif age == 12:
    print("be careful ;) ")
else:
    print("very well, go ahead, dont die")
    
    wants_to_play = input("Do you want to play?").lower()
    if wants_to_play == "yes":
        print("have fun :)")
        
        left_or_right=input("frist choice... left or right (left/right)? ").lower()
        if left_or_right == "left":
            ans = input("nice, you follow the path and reach a lake... Do you swim across or go around? (across and around) ")
            
            if ans == "around":
                print("you went around and reached the other side of the lake")
            
            elif ans == "across":
                print("you managed to get across, but were bit by a fish and lost 5 health. ")
                
                health -=5
            ans=input("you notice a house and a river. which do you go to river or house? (river/house)")
            if ans=="house":
                print("you go to the house and are greted by the owner.. he is a ghost..you lose 5 health")
                health -=5

                if health <=0:
                    print("you now have 0 health and you lost the game")
                else:
                    print("you are lucky, you have survived...")
                    
            # else:
                # print("you fell in the rvier and lost.. ")

            
                if health <= 0:
                    print("you now have 0 health and you lost the game...")

                else:
                    print("you fell in the river and lost.. ")
            
            else:
                print("you die. gg")
            
        else:
            print("you fell down and die...")
        
        
        
    else:
        print("Bye bye")



