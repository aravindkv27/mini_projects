import random
from typing import final
#from typing import final


print("Lets Play Rock Paper and Scissors. ")




rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# rocks=int(rock)
# papers=int(paper)
# scissorss=int(scissors)

rps=input("Choose Rock for 0 Paper for 1 and Scissors for 2 : ")

if rps=="0":
    print(rock)
elif rps=="1":
    print(paper)
elif rps=="2":
    print(scissors)
else:
    print("Enter correct Number.")


print("Computer Choice : ")
computer=[rock,paper,scissors]
com=len(computer)

final=random.randint(0,com-1)
com_ans=computer[final]

print(com_ans)

if rps=="0" and com_ans==scissors:
    print("you win")
elif rps=="0" and com_ans==paper:
    print("You Lose")
elif rps=="0" and com_ans==rock:
    print("Draw")
if rps=="1" and com_ans==scissors:
    print("you win")
elif rps=="1" and com_ans==rock:
    print("You Lose")
elif rps=="1" and com_ans==paper:
    print("Draw")
if rps=="2" and com_ans==scissors:
    print("Draw")
elif rps=="2" and com_ans==paper:
    print("You Win")
elif rps=="2" and com_ans==rock:
    print("You Win")
