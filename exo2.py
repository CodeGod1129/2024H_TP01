# TODO : Calculer les quantités de matériaux nécessaires pour fabriquer un nombre donné de baguettes magiques.

nombre_baguettes =input("Nombre de baguettes a fabriquer :")
bois=int(nombre_baguettes)* 3
ml=int(nombre_baguettes)* 10
print(f" Voici les materiaux requis pour la fabrication de {nombre_baguettes} baguettes magiques:")
print(f"- {bois} piece(s) de bois")
print(f"- {nombre_baguettes} coeur(s) de creatures magiques")
print(f"- {ml} ml de vernis")