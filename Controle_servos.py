from Traducteur_servo import traduit
from Interactive.Lecture_potentiometres import reinitialiser_lectures
from machine import PWM, Pin
from time import sleep

# Angles du stylo
ANGLE_STYLO_HAUT = 0
ANGLE_STYLO_BAS = 30

# Décalages de calibration
OFFSET_EPAULE = 0.0
OFFSET_COUDE = 0.0

PAUSE_DEPLACEMENT_S = 0.2  # temps laissé aux servos après un G1 A MODIFIER
PAUSE_STYLO_S = 0.3         # temps laissé au poignet après M3 / M5 A MODIFIER

def creer_servo(pin):
    """ Responsable: TheKingyveL

    Crée un objet PWM associé à la broche indiquée et configure sa
    fréquence à 50 Hz.

    Entrées : pin (int), numéro de broche.
    Sorties : objet PWM configuré.
    Appels : constructeur Pin(), constructeur PWM(), PWM.freq()."""
    servo = PWM(Pin(pin))
    servo.freq(50)
    return servo

def positionner (servo, angle):
     """ Responsable: TheKingyveL

    Convertit l'angle demandé en rapport cyclique PWM et commande
    directement le servomoteur.

    Entrées : servo (objet PWM), angle (float, degrés).
    Sorties : aucune (None).
    Appels : traduit(), servo.duty_u16()."""
     servo.duty_u16(traduit(angle))


def deplacer(servos, S_valeur = None, E_valeur = None):
    """Responsable: TheKingyveL

    Déplace l'épaule et/ou le coude selon les angles fournis, applique
    les décalages locaux configurés, puis attend la fin du mouvement.

    Entrées : servos (dict contenant 'epaule' et 'coude'); S_valeur et
              E_valeur (float ou None, degrés).
    Sorties : aucune (None).
    Appels : positionner() et sleep()."""
    
    if S_valeur is not None:
        positionner(servos["epaule"],S_valeur + OFFSET_EPAULE)
    if E_valeur is not None:
        positionner(servos["coude"],E_valeur + OFFSET_COUDE)
    sleep(PAUSE_DEPLACEMENT_S)


def desactiver(servos):
    """ Responsable: TheKingyveL

    Désactive les signaux PWM de tous les servomoteurs du dictionnaire.

    Entrées : servos (dict de noms vers objets PWM).
    Sorties : aucune (None).
    Appels : servo.deinit() pour chaque servo."""
    
    for servo in servos.values():
        servo.deinit()
    

def relever_stylo(servo):
    """ Responsable: ScNova

    Place le servo du poignet à l'angle prédéfini correspondant au stylo
    relevé, puis attend le temps de stabilisation.

    Entrées : servo (objet PWM du poignet).
    Sorties : aucune (None).
    Appels : traduit(), servo.duty_u16(), sleep()."""
    
    servo.duty_u16(traduit(ANGLE_STYLO_HAUT))
    sleep(PAUSE_STYLO_S)
    

def abaisser_stylo(servo):
    """Responsable: ScNova

    Place le servo du poignet à l'angle prédéfini correspondant au stylo
    abaissé, puis attend le temps de stabilisation.

    Entrées : servo (objet PWM du poignet).
    Sorties : aucune (None).
    Appels : traduit(), servo.duty_u16(), sleep()."""
    servo.duty_u16(traduit(ANGLE_STYLO_BAS))
    sleep(PAUSE_STYLO_S)

def retour_position_initial(servos, angle_epaule, angle_coude):
    """ Responsable: TheKingyveL

    Relève le stylo, ramène l'épaule et le coude aux angles initiaux,
    puis réinitialise les références des potentiomètres.

    Entrées : servos (dict des servos); angle_epaule et angle_coude
              (float, degrés).
    Sorties : aucune (None).
    Appels : relever_stylo(), deplacer(), reinitialiser_lectures()."""

    relever_stylo(servos["poignet"])
    deplacer(servos, angle_epaule, angle_coude)
    reinitialiser_lectures()
