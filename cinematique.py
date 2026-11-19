import math

def cinématique_inverse (C_x, C_y):

    A_x = −50       #position de l'epaule
    A_y = 139.5

    L_a = 155       #longueur des deux maillons
    L_b = 155

    AC = math.sqrt((A_x - C_x) ** 2 + (A_y - C_y) ** 2)
    if 
    A_base_C = math.sqrt((A_x - C_x) ** 2 + C_y ** 2) 
    
    angle_BAC = math.acos((L_a ** 2 + (AC) ** 2 - L_b**2) / (2 * L_a * AC))
    
    angle_ACB = math.asin((L_a * math.sin(angle_BAC)) / L_b)
                          
    angle_YAC = math.acos((A_y ** 2 + AC ** 2 - (A_base_C) ** 2) / (2 * A_y * AC))

    alpha = math.degrees(angle_BAC + angle_YAC)
    
    beta = math.degrees(angle_BAC + angle_ACB)

    servoA = alpha - 75
           
    servoB = 150 - beta

    return servoA, servoB 
