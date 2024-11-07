import random


def random_number_generator(min, max):
    """
    Generates random integer between the range of two integers

    Args:
        min: The lower-boundary integer value
        max: The upper-boundary integer value
    
    Returns:
        random.randint: random number(int type) between min and max values

    
    Examples:
    >>>random_number_generator(1,7)
    4
    >>>random_number_generator(500,800)
    756

    """
    return random.randint(min, max) #generates random integer in the range of min and max


def random_operation_selector():
    """
    
    Selects random operator from the options which are +(addition), -(subtraction),*(multiplication)

    Returns:
        random.choice= random operator ( +,-,*)
    
    """
    
    return random.choice(['+', '-', '*']) #choosed the operation that will be applied


def question_generator(num_1, num_2, op):
    """
    Creates the question with decided numbers and operation. 

    Args:
        num_1= the first number in the question
        numb_2= the second number in the question
        op= the selected operation (could be + - *)
    
    Returns:
        problem: the question that is asked to the user
        ans= the answer as a result of the logic/operation

    """

    problem = f"{num_1} {op} {num_2}" # question definition
    if op == '+': 
        ans = num_1 + num_2 # addition logic
    elif op == '-': 
        ans = num_1 - num_2 # subtraction logic
    else: ans = num_1 * num_2 # multiplication logic

    return problem, ans

def math_quiz():
    """
    Prints the greeting statements and explanations about the game. Uses different functions to generate random number, to select the operation and creates the questionaries.

    Raises:
        ValueError: If the user's input is not a valid integer.
    
    Example: 
        In order to execute this function, it can be called in the main block at the end of the function
        >>>if __name__ == "__main__":
          math_quiz()
    """
    correct_answer = 0  #score counter
    question_number = 3 #number of questions that will be asked

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(question_number):
        num_1 = random_number_generator(1, 10); #generates a number between 1 and 10
        num_2 = random_number_generator(1, 5);  # generates a number between 1 and 5
        op = random_operation_selector() # select a random operation 

        PROBLEM, ANSWER = question_generator(num_1, num_2, op) # this line creates the question based on numbers and operation
        print(f"\nQuestion: {PROBLEM}")

        while True:
            try:
                user_answer = int(input("Your answer: "))

                break  # Exit the loop if input is valid
            except ValueError:
                print("Invalid input. Please enter a valid integer.") #if the inpu is invalid, it askes continuously until getting an valid input

        if user_answer == ANSWER:
            print("Correct! You earned a point.")
            correct_answer += 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {correct_answer}/{question_number}")

if __name__ == "__main__":
    math_quiz()
