#number_line = input('Type here: ')
first_number = float(input('What is the biggest number? '))
second_number = float(input("What is the smallest number? "))
distane = float(input('How far is it from each of the number in the range? '))
numbers_of_number = (first_number - second_number) / distane + 1
answer = ((first_number + second_number) * numbers_of_number) / 2
print(float(answer))