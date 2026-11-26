from GCode.Analyseur_gcode import lire_fichier
from GCode.Interpreteur_gcode import executeur
from Interactive.Lecture_potentiometres import lecture
from Controle_servos import creer_servo, desactiver, retour_position_initial, deplacer, abaisser_stylo, relever_stylo
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

# used AI to make this function
def interactive(servos):
    """Responsable: ScNova

    Initialise la position, lit continuellement les potentiomètres et le
    bouton, convertit les coordonnées en angles, applique les corrections
    de calibration puis commande les servos et le stylo.

    Entrées : servos (dict des servos); table_calibration (dict).
    Sorties : aucune (boucle interactive).
    Appels : retour_position_initial(), lecture(), cinematique_inverse(),
             appliquer_corrections(), deplacer(), abaisser_stylo(),
             relever_stylo()."""
    
    # Return to initial position
    retour_position_initial(servos, x_init, y_init)

    dernier_state = False
    dernier_x = x_init
    dernier_y = y_init

    while True:

        # Read potentiometers and button
        dx, dy, state = lecture()

        # Calculate actual pen position
        x = x_init + dx
        y = y_init + dy

        # Calculate servo angles when position changes
        if x != dernier_x or y != dernier_y:

            angles = cinematique_inverse(x, y)

            if angles is not None:
                deplacer(servos, angles[0], angles[1])

            dernier_x = x
            dernier_y = y

        # Control the pen
        if state != dernier_state:

            if state:
                abaisser_stylo(servos["poignet"])
            else:
                relever_stylo(servos["poignet"])

            dernier_state = state

            

def gcode(servos,nom_fichier):
    """
    Responsable: ScNova

    Lit le fichier G-code, puis transmet chaque commande et ses paramètres
    à l'interpréteur jusqu'à la fin du fichier ou jusqu'à une commande M18.

    Entrées : servos (dict); nom_fichier (str); table_calibration (dict).
    Sorties : booléen - True si l'exécution a été arrêtée par M18,
              False si toutes les commandes ont été traitées.
    Appels : lire_fichier(), executeur().
    """
    
    # Lit le fichier G-Code et récupère la liste des instructions 
    instructions = lire_fichier(nom_fichier)
    
    # Exécute les instructions dans l'ordre du fichier
    for commande, parametres in instructions:
        if executeur(servos, commande, parametres):
            return True
        
    return False

def main():
    
     """
    Responsable: ScNova
    
    Crée les trois servos, charge la table de calibration, affiche le menu,
    lance le mode choisi et permet de démarrer la calibration. Si un G-code
    retourne le signal d'arrêt M18, termine le programme sans désactiver
    deux fois les servos.
    Le corps de main() est fourni au niveau de détail demandé pour le
    point d'entrée du programme; les fonctions spécialisées restent à
    compléter dans leurs modules respectifs.

    Entrées : aucune (configuration locale du programme).
    Sorties : aucune (None).
    Appels : creer_servo(), calibrer(), calibration_configuration(), interactive(),
             gcode(), desactiver().
    """

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


if __name__ == "__main__":
    main()
