"""
Ecrire une fonction bat(joueur_1, joueur_2) où joueur_1 et joueur_2 ont chacun une valeur entière 0, 1 ou 2, qui encode ce que le joueur a fait comme coup (0 : PIERRE, 1 : FEUILLE, 2 : CISEAUX) qui renvoie un résultat booléen :

    vrai si joueur_1 bat le joueur_2 :

    faux si joueur_2 bat joueur_1 ou fait match nul contre lui.
"""
def bat(joueur_1, joueur_2) :
  if (joueur_1 == 0 and joueur_2 == 0) :
    return False
  if (joueur_1 == 1 and joueur_2  == 1) or (joueur_1 == 0 and joueur_2 == 1) :
    return False
  if joueur_1 == 2 and (joueur_2 == 1) :
    return True
  if (joueur_1 == 0 and joueur_2 == 2) :
    return True
  if (joueur_1 == 0 and joueur_2 == 2) or (joueur_1 == 1 and joueur_2 == 0):
    return True
  if joueur_1 == 1 and joueur_2 == 2 :
    return False
  if joueur_1 == joueur_2 :
    return False
  if joueur_1 == 2 and joueur_2 == 0 :
    return False
