n = 18
Total_guess = 5
guesses_left = Total_guess
name = str(input("Enter a Gamer tag/ name:"))
print("Welcome to a Number guessing game.")
print("Are you ready to start?")
while guesses_left>0:
    input_number = int(input("Enter a number:"))
    if input_number<18:
        print("Your number is smaller. think of bigger digit under 20.")
    elif input_number>18:
        print("Your number is greater. think of digit under 20.")
    elif input_number == n:
        break
        print("You Finally gussed it right,")
        print("You won the game.")
    guesses_left -= 1
    print("Guesses left:", guesses_left)
if guesses_left == 0:
    print("Guesses limit over, Try Again next time.")

print("Thank you for playing the Game", name)
print("Do not forget to reveiw in playstore.")