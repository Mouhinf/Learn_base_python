import random

secret = random.randint(0, 5)

t = int (input('Donner le nombre que vous avez devine : '))

if secret == t :
    print("C'est juste vous avez devinez le nombre")
else:
    print("Vous avez perdu")


