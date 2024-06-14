import random

# Step 2: Generate a random number between 1 and 10
random_number = random.randint(1, 10)

# Step 3: Start the guessing loop
while True:
    try:
        # Step 4: Get user input and handle errors
        user_guess = int(input("Please guess a number between 1 to 10: "))
        
        # Step 5: Check the user's guess
        if user_guess == random_number:
            break
    except ValueError:
        print("Please provide an integer.")
        
# Step 6: End the game and display the result
print("Game over! Congrats, you win! The number was:", random_number)
