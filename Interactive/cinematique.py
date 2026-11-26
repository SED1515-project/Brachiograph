import math

A_x = -50       #position de l'epaule
A_y = 139.5

L1 = 155       #longueur des deux maillons
L2 = 155

OFFSET_A = 75      
OFFSET_B = 150     

def borne(x):
    """Responsable: Lisa

    Limite une valeur numérique à l'intervalle [-1, 1] afin de protéger
    les appels aux fonctions trigonométriques inverses.

    Entrées : x (float), valeur à limiter.
    Sorties : float compris entre -1 et 1.
    Appels : aucun."""
    return max(-1.0, min(1.0, x))   

def cinematique_inverse(C_x, C_y):

    """ Responsable: Lisa

    Calcule les angles des servos épaule et coude nécessaires pour placer
    le stylo aux coordonnées cibles. Vérifie l'atteignabilité du point et
    la plage admissible de chaque servo.

    Entrées : C_x (float, mm), C_y (float, mm).
    Sorties : tuple (servoA, servoB) en degrés, ou None si le point est
              inaccessible ou si un angle est hors de [0, 180].
    Appels : borne().
    """
    d = math.sqrt((A_x - C_x) ** 2 + (A_y - C_y) ** 2)

  # verification de la distance entre l'epaule et le stylo : point atteignable par le bras ?

    if d == 0 or d < abs(L1 - L2) or d > L1 + L2:     # L1=La ; L2=Lb ; AC=d 
                return None
    
    A_base_C = math.sqrt((A_x-C_x)**2+C_y**2)    
    angle_BAC = math.acos(borne((L1**2+d**2-L2**2)/(2*L1*d)))    
    angle_ACB = math.asin(borne((L1*math.sin(angle_BAC))/L2))
    angle_YAC = math.acos(borne((A_y**2+d**2-(A_base_C)**2) / (2*A_y*d)))

    alpha = math.degrees(angle_BAC + angle_YAC)
    beta = math.degrees(angle_BAC + angle_ACB)

    servoA = alpha - OFFSET_A
    servoB = OFFSET_B - beta

    if 0 <= servoA <= 180 and 0 <= servoB <= 180:
        return servoA, servoB
    else:
        return None  
