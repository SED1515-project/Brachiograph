from machine import ADC, Pin


# les Pins
POTENTIOMETRE_X_PIN = 26
POTENTIOMETRE_Y_PIN = 27
STYLO_PIN = 10

# Configuration des lecteurs analogue ADC et du button pour le stylo
potentiometre_X = ADC(Pin (POTENTIOMETRE_X_PIN))
potentiometre_Y = ADC(Pin (POTENTIOMETRE_Y_PIN))
stylo = Pin(STYLO_PIN, Pin.IN, Pin.PULL_DOWN)


def lecture():
    "lire les entrees de l'utilisateur x et y ainsi que l'etat du stylo"
  
    x_adc = potentiometre_X.read_u16()
    y_adc = potentiometre_Y.read_u16()
    stylo_state = stylo.value()

    return x_adc, y_adc, stylo_state
