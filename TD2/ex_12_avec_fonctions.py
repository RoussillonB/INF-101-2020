def question_1():
    # First question of the quzz
    rep = input('a < b < c ?')
    # Translates user answer into boolean
    bool_rep = rep == 'V'
    true_answer = a < b < c
    # The user is correct if and only if their answer is the same as the true answer
    return true_answer == bool_rep

def question_2():
    # First question of the quzz
    rep = input('Un seul nombre impair parmi a, b, c ?')
    # Translates user answer into boolean
    bool_rep = rep == 'V'
    true_answer = (a % 2 + b % 2 + c % 2) == 1
    # The user is correct if and only if their answer is the same as the true answer
    return true_answer == bool_rep

def question_3():
    # First question of the quzz
    rep = input('a, b, c disctincts deux à deux ?')
    # Translates user answer into boolean
    bool_rep = rep == 'V'
    true_answer = a != b and a != c and b != c
    # The user is correct if and only if their answer is the same as the true answer
    return true_answer == bool_rep

# If you have never seen it, the following is a multiline comment
"""
Variable used to determined if the game should be replayed.
Initialized at 'oui' to enter the game at least once
"""
play = 'oui'

# Main game loop
while play == 'oui':
    # Counts the number of correct answers to the quizz
    good_answers = 0
    print('Entrez trois entiers a, b et c')
    a = int(input('a = ?'))
    b = int(input('b = ?'))
    c = int(input('c = ?'))

    """ 
    Note that the usage of functions makes the main loop shorter and easier to read.
    In general, we try to keep each piece of code as short as possible.
    """
    is_correct_1 = question_1()
    if(is_correct_1):
        print('reponse correcte, Bravo')
        good_answers += 1
    else:
        print('reponse incorrecte')

    is_correct_2 = question_2()
    if(is_correct_2):
        print('reponse correcte, Bravo')
        good_answers += 1
    else:
        print('reponse incorrecte')

    is_correct_3 = question_3()
    if(is_correct_3):
        print('reponse correcte, Bravo')
        good_answers += 1
    else:
        print('reponse incorrecte')
    print(good_answers, 'bonnes reponses sur 3')

    play = input('Voulez-vous rejouer?')
