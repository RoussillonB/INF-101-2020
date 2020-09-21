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

    # First question of the quzz
    rep_1 = input('a < b < c ?')
    # Translates user answer into boolean
    bool_rep_1 = rep_1 == 'V'
    """
    Attention, la solution donnee en TD if(bool_rep_1 == a < b < c) ne marche pas!
    En effet, en python tous les operateurs de comparaison ont la meme priorité.
    L'expression bool_rep_1 == a < b < c est donc interpretee comme (bool_rep_1 == a) < b < c.
    """
    true_answer = a < b < c
    # The user is correct if and only if their answer is the same as the true answer
    if(bool_rep_1 == true_answer):
        print('reponse correcte, Bravo')
        good_answers += 1
    else:
        print('reponse incorrecte')

    # Second question of the quizz
    rep_2 = input('Un seul nombre impair parmi a, b, c ?')
    bool_rep_2 = rep_2 == 'V'
    true_answer_2 = (a % 2 + b % 2 + c % 2) == 1
    if(bool_rep_2 == true_answer_2):
        print('reponse correcte, Bravo')
        good_answers += 1
    else:
        print('reponse incorrecte')

    # Third question of the quizz
    rep_3 = input('a, b, c disctincts deux à deux ?')
    bool_rep_3 = rep_3 == 'V'
    true_answer_3 = a != b and a != c and b != c
    if(bool_rep_3 == true_answer_3):
        print('reponse correcte, Bravo')
        good_answers += 1
    else:
        print('reponse incorrecte')
    print(good_answers, 'bonnes reponses sur 3')

    play = input('Voulez-vous rejouer?')