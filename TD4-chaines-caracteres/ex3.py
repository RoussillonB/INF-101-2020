def dans_alphabet(lettre):
    # Les parenthèses après le and sont nécessaires ici.
    return (len(lettre) == 1 and ('A' <= lettre <= 'Z' or 'a' <= lettre <= 'z'))

print(dans_alphabet('-'))
print(dans_alphabet('b'))
print(dans_alphabet('ab'))
print(dans_alphabet('F'))
