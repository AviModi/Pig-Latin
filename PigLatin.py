continue_game = "yes"
while(continue_game=="yes"):
    user_input=input("Enter a word to convert to pig latin ")
    vowels=("a,e,i,o,u")
    first_letter=user_input[0]
    if first_letter in vowels:
        user_input=user_input+"yay"
    else:
        user_input=user_input[1:]
        user_input=user_input+first_letter+"ay"
    print(user_input)
    continue_game=input("Do you want to play again ")
    if continue_game=="no":
        print("Thanks For Playing")
