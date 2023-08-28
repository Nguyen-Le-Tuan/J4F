print('Hello')
options = input("Do you want to play quiz game? ")
if options.lower() == 'yes':
    print("Okay, let's go :)")
    score = 0
    answer1 = input("What does CPU stands for? ") # Câu hỏi 1
    if answer1.lower() == 'central processing unit':
        print('Correct')
        score += 1
    else:
        print('Incorrect :(')
    answer2 = input('What does GPU stands for? ') # Câu hỏi 2
    if answer2.lower() == 'graphics processing unit':
        print('Correct')
        score += 1
    elif score <=1:
        print('Oops, incorrect')
    else:
        print('Incorrect :(')
    answer3 = input('What does RAM stands for? ') # Câu hỏi 3
    if answer3.lower() == 'random access memory':
        print('Correct')
        score += 1
    elif score <= 1:
        print('Arghhhh, incorrect again??')
    else:
        print('Incorrect :(')
    answer4 = input('Easier: 1+1 = ?') # Câu hỏi 3
    if answer4 == '2'and score <= 3:
        print('Hah, Correct :)')
        score += 1
    elif score <= 4:
        print("I don't have anything to say -.-")
    else:
        print('Incorrect :(')
        print("Your final point is: " + str(score) + ' points')  # Điểm cuối cùng
elif options.lower() == 'no':
    print('I hope you will play :(')
    quit()
else:
    print("Do you type correctly?")

