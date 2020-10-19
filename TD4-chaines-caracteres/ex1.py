# Dans ce fichier, des input ont été ajoutés. Ils ne sont pas du tout demandés dans l'exercice 1 et il serait faux de les mettre en partiel.
# Ils sont présent juste pour obtenir un programme python que vous pouvez tester.
# De même, les print ne sont pas demandés et sont la juste pour des tests.

# Correction de ce qui était attendu:
"""
1) len(x) == 1 and 'A' <= x <= 'Z'
2) len(y) == 1 and y in 'AEIOUY'
3) len(y) == len(x) == 1 and 'a' <= x <= 'z' and 'a' <= y <= 'z'
4) x < y
5) 3 <= len(x) <= 7
6) len(x) == 1 and x.islower() and x.upper() == y
7) ord('a') <= n <= ord('z')
"""

# Correction en programme python
# Question 1
x = input('x1')
print(len(x) == 1 and 'A' <= x <= 'Z')

# Question 2
y = input('y2')
print(len(y) == 1 and y in 'AEIOUY')

# Question 3
x = input('x3')
y = input('y3')
print(len(y) == len(x) == 1 and 'a' <= x <= 'z' and 'a' <= y <= 'z')

# Question 4
x = input('x4')
y = input('y4')
print(x < y)

# Question 5
x = input('x5')
print(3 <= len(x) <= 7)

# Question 6
x = input('x6')
y = input('y6')
print(len(x) == 1 and x.islower() and x.upper() == y)

# Question 7
n = int(input('n7'))
print(ord('a') <= n <= ord('z'))
