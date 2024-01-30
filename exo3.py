# TODO : Calculer la distance que chaque rocher lancé par les catapultes peut atteindre en utilisant la formule de la portée d'un projectile.
import math
vitesse_initiale = input("Entrez la vitesse initiale (en m/s) : ")
angle_lancement = input("Entrez l'angle de lancement (en degres) : ")
angle_lancement=int(angle_lancement)
angle_radian=math.radians(angle_lancement)
g= 9.81
portee = (float(vitesse_initiale) ** 2 * math.sin(2 * float(angle_radian))) / g
portee=float(portee)
portee="{:.2f}".format(portee)
print (f"La distance parcourue par le projectile est de {portee} metres.")
