from GCode.Analyseur_gcode import lire_fichier
from GCode.Interpreteur_gcode import executeur
from Interactive.Lecture_potentiometres import lecture
from Controle_servos import creer_servo, desactiver, retour_position_initial
from Interactive.Cinematique_inverse import cinematique_inverse


# Configuration des broches
PIN_EPAULE = 0
PIN_COUDE = 1
PIN_POIGNET = 2


#position initial
x_init = 0
y_init = 0

FICHIERS_GCODE = {
    1: "line.gcode",
    2: "circle.gcode",
    3: "square.gcode",
    4: "circle_and_square.gcode"
}


def interactive(servos):
    """Gere le mode de dessin interactif"""
    retour_position_initial(servos, x_init, y_init)

    while True:
        x, y, state = lecture()
        angles = cinematique_inverse(x,y)


    return None

def gcode(servos,nom_fichier):
    # Lit le fichier G-Code et récupère la liste des instructions 
    instructions = lire_fichier(nom_fichier)
    
    # Exécute les instructions dans l'ordre du fichier
    for commande, parametres in instructions:
        if executeur(servos, commande, parametres):
            return True
        
    return False



servos = {
        "epaule": creer_servo(PIN_EPAULE),
        "coude": creer_servo(PIN_COUDE),
        "poignet": creer_servo(PIN_POIGNET)

        }


while True:

    choix = input("\nChoisissez un mode:\n" 
                  "1. Interactif\n"
                  "2. Fichier G-Code\n"
                  "0. Quitter\n"
                  "Votre choix: ")

    if choix == "1":
        
        interactive(servos)

    elif choix == "2":

        while True:

            print("---FICHIERS DISPONIBLES---")
            for num, fichier in FICHIERS_GCODE.items():
                print(num,".",fichier)
            print("0. Retour au menu principal")
            
            try: 
                choix_dessin = int(input("choisissez un dessin: "))

                if choix_dessin in FICHIERS_GCODE:
                    gcode(servos,FICHIERS_GCODE[choix_dessin])

                elif choix_dessin == 0:
                    print ("Fin du programme")
                    break

                else:
                    print("Choix invalide")
                    
            except ValueError:
                print("Erreur: Veuillez entrer un nombre valide")
        
        

    elif choix == "0":
        print("Fin du programme")
        desactiver(servos)
        break

    else:
        print("Mode non reconnu")
