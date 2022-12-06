print("Welcome to KBC")
a=input("enter your name:")
questions_list=["1.longest river in the world",
                "2.A country without snakes in the world",
                "3.what is the capital of UK",
                "4.Reliance opened a hospital dedicated to covid-19 in which city"]
options_list=[["godavari","nailu","krishna","brahmaputra"],
             ["island","hawaidweepam","lakshadweep","kavaratthi"],
             ["london","sanfrancio","england","delhi"],
            ["hyderabad","chennai","mumbai","gujarat"]]
solutions=[2,2,1,3]
fifty_options=[["nailu","krishna"],["island","hawaidweep"],["london","delhi"],["chennai","gujarat"]]
fifty_solutions=[1,2,1,2]
i=0
fifty=0
while i<1:
    print(questions_list[0])
    print("1.",options_list[0][0])
    print("2.",options_list[0][1])
    print("3.",options_list[0][2])
    print("4.",options_list[0][3])
    print("1.with lifeline, 2.without lifeline")
    choice=int(input("enter ur option"))
    if choice==1:
        fifty+=1
        print("1.",fifty_options[0][0])
        print("2.",fifty_options[0][1])
        answer=int(input("enter your answer:"))
        if answer==fifty_solutions[0]:
            print("congratslations your answer is correct")
            print("you won 5000 rupees")
        else:
            print("your answer is wrong")
            print("better luck for next time")
            break
    if choice==2:
        answer=int(input("enter your answer:"))
        if answer==solutions[0]:
            print("congraslations you won 10,000 rupees")
        else:
            print("oops wrong answer")
            break
    i=i+1







