import random

list_of_words=["aardvark","baboon","camel"]

chosen_word = random.choice(list_of_words)  #choosing the word randomly

lenght_of_chosen_word=len(chosen_word)
#testing
#print(f"the solution is {chosen_word}.")
display=[]
for letter in chosen_word:
    display+="_"
# print(display)
#chosen_word=list(chosen)  #converting the chosen word into list

lenght_of_word=len(display)
while_i= False



while not while_i :
    guess=input("Guess the Letter : ").lower()
    
    for position in range(lenght_of_chosen_word):
        letter = chosen_word[position]
        if letter==guess:
            display[position]=letter
    print(display)
    #while_i=while_i+1

    if "_" not in display:
        while_i=True
        print("You win.")



    # index=0
    # for i in chosen_word:
    #     if guess == i:
    #         display.insert(index,guess)
    #     index+=1
    # print(display)
    # while_i=while_i+1

### Other method to insert a letter

