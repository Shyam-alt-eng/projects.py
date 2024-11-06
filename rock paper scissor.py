import random
you = {"rock": 1,"paper": 0,"scissor": -1}
revyou = {1:"rock",0:"paper",-1:"scissor"}
sum = 0
while True :
    user_input = input("Enter your choice ('rock','paper','scissor') :").lower()
    you = {"rock": 1,"paper": 0,"scissor": -1}
    revyou = {1:"rock",0:"paper",-1:"scissor"}
    opponent = random.choice([1,0,-1])
    if user_input not in{"rock","paper","scissor"} :
        print("please Enter valid command"+"\U0001F604")
    else:
        user_input = you[user_input] 
        opponent = random.choice([1,0,-1])

        if (opponent ==  user_input ):
            print("it's a draw"+"\U0001F929")
            
            
            
        elif(opponent == 1 and user_input == -1) or (opponent == 0 and user_input == 1) or (opponent == -1 and user_input == 0) :
            print("you lose"+"\U0001F61E")
            print(f"your score is {sum}")
            print(f"opponent entered {revyou[opponent]} and you entered {revyou[user_input]}")
            break
        elif (opponent == 1 and user_input== 0) or (opponent == 0 and user_input == -1) or (opponent == -1 and user_input == 1): 
            print("you win"+"\U0001F389"+"\U0001F601")
            sum+=5
            print(f"your score is {sum}")

        
