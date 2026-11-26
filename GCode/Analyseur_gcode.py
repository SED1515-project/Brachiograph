def lire_fichier(nom_fichier):
    """Responsable: Lilia

    Lit le fichier ligne par ligne, ignore les lignes vides, sépare la
    commande de ses paramètres, convertit les valeurs en nombres et
    construit la liste ordonnée des instructions.

    Entrées : nom_fichier (str, chemin du fichier G-code).
    Sorties : liste de tuples (commande, parametres), où parametres est
              un dictionnaire associant une lettre à une valeur float.
    Appels : méthodes de lecture de fichier et opérations sur chaînes."""
    
    instructions = []
    with open(nom_fichier,"r") as file:
        for line in file:
            elements = line.strip().split() # separe une ligne de fichier en une liste 

            if not elements: # si c'est une ligne vide on passe a la ligne suivante 
                continue

            commande = elements[0] # on conserve la commande dans une variable donc commande = M3

            parametres = {}

            for element in elements[1:]: # loop tout les elements apres l'element de commande retourne un format dictionnaire 
                nom_parametre = element[0]
                valeur = float(element[1:])
                parametres[nom_parametre] = valeur

            instruction = (commande, parametres)
            instructions.append(instruction) # on aura un format (commande,{nom_parametre: valeur_parametre, ...})

    return instructions # [(commande,{nom_parametre: valeur_parametre,...}),...]




