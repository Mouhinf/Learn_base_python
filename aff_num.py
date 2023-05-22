"""
Ecrivez un code qui lit un nombre entier strictement positif n et affiche sur n lignes une table de multiplication de taille  n x n, avec, pour i entre 1 et n,  les n premieres valeurs multiples de i strictement positives sur la ieme ligne.
Ainsi, les n premiers multiples de 1 strictement positifs (0 non compris) sont affiches sur la premiere ligne, les n premiers multiples de 2 sur la deuxieme, et caetera
Exemple 1

Avec la valeur lue suivante :

3

le resultat a afficher sera :

1   2   3
2   4   6
3   6   9

"""
n = int(input())
for i in range(1,n+1) :
  for j in range (1, n+1) :
    print(i*j, end = "\t")
  print() 
