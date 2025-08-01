#quiz game 

#--------------------------------------------------
def new_game():
    guesses=[] # this will store all user answers 
    correct_guesses=0
    question_num=1
    for key in questions:
        print("-------------------------------")
        print(key) # print the questions 

        for i in options[ question_num-1]:
            print(i) # prints the option of that questions 

    user_guess= input(" enter (A,B,C,or D):")
    user_guess= user_guess.upper()    # converts input to uppercase
    guesses.append(user_guess)    # append to the list ( corrected)

    correct_guesses += check_answer(questions.get(key),user_guess)
    question_num += 1    
    display_score (correct_guesses,guesses)
#-----------------------------------------------
def check_answer(answer, user_guess):
    if answer== user_guess:
        print('correct')
        return 1
    else:
        print(" WRONG!")
        return 0

#------------------------------------------------
def display_score(correct_guesses, guesses):
    print("----------------------------------------------------")
    print("RESULT")
    print("-------------------------------------------------------")
    print("answers:", end="")
    for i in questions :
        print(questions.get(i), end="")
    print()

    print("guesses:", end="")
    for i in guesses: 
        print(i, end="")
    print()

    score= int((correct_guesses/len(questions))*100)
    print(" your score is :" + str(score) + "%")


#-----------------------------------------------
def play_again():
   
    response= input(" Do you want to play again (yes/no):")
    response= response.upper()
    if response== " YES":
        return True
    else:
        return False
#---------------------------------------------------

questions= { " who created python" : " A",
            " what year as python created?:" : " C",
            " is the earth round ?:": " B", 
            " python is tributed to which comedy group ?: " :" A"}
options = [[" A. guido van rossum ","B. elon musk", "C. Tiago", "D. herry blues"],
           [" A.1894","B.1894", "C.1659","D.1985"],
        ["A. nhjikmo", "B.JINKMO",'C. MONTY PYTHON ', "D. GHDKF"],
        [ "A. TRUE", "B. FALSE", " C. NEITHER ", "D. EITHER"]]
# start the game 
new_game()

while play_again():
     new_game()
     break
print(" byeeeeeeeeeeeee!")





