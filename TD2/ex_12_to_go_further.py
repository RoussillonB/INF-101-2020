"""
This implementation goes beyond what is asked by the exercise and tries to give an elegant
implementation of the quizz.
Note that it can always be improved (for example by adding input filtration).
"""

def question(message, answer):
    """
    Asks a quizz question to the user given:
    - message the question to ask the user.
    - answer the correct answer to the question.
    Returns True if the user answered correctly, False otherwise
    """
    rep = input(message)
    # Translates the user response to a boolean for comparison to the answer
    rep_bool = rep == 'V'
    return rep_bool == answer


def correct_message():
    """
    Prints the message in case of correct answer.
    This might seem overkill but it is way easier if we want to modify the message
    after having written the full program. In general, we avoid code duplication.
    """
    print('reponse correcte, Bravo')


def incorrect_message():
    """
    Prints the message in case of incorrect answer
    """
    print('reponse incorrecte')


def play():
    """
    Plays the quizz defined in exercise 12
    """

    # Counts the number of correct answer
    number_correct = 0

    # Retrieves parameters of the quizz
    print('Entrez trois entiers a, b et c')
    a = int(input('a = ?'))
    b = int(input('b = ?'))
    c = int(input('c = ?'))

    # Question 1
    message_1 = 'a < b < c ?'
    answer_1 = a < b < c
    is_correct_1 = question(message_1, answer_1)
    if(is_correct_1):
        correct_message()
        number_correct += 1
    else:
        incorrect_message()

    # Question_2
    message_2 = 'un seul nombre impair parmi a, b, c ?'
    answer_2 = (a % 2 + b % 2 + c % 2) == 1
    is_correct_2 = question(message_2, answer_2)
    if(is_correct_2):
        correct_message()
        number_correct += 1
    else:
        incorrect_message()

    # Question 3
    message_3 = 'a, b, c disctincts deux à deux?'
    answer_3 = a != b and a != c and b != c
    is_correct_3 = question(message_3, answer_3)
    if(is_correct_3):
        correct_message()
        number_correct += 1
    else:
        incorrect_message()

    # The quizz ends, printing the number of correct answers
    print(number_correct, 'reponses correctes sur 3')
    """
    Note that there is no return statement in this function.
    By default, it returns None.
    """


# Main loop, ideally a main program should be as short as this
# We want to play at least once
replay = 'oui'
while replay == 'oui':
    play()
    replay = input('Voulez vous rejouer?')
