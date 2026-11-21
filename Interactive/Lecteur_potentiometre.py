from machine import ADC, Pin



# les Pins
POTENTIOMETRE_X_PIN = 26
POTENTIOMETRE_Y_PIN = 27
STYLO_PIN = 10

# Configuration des lecteurs analogue ADC et du button pour le stylo
potentiometre_X = ADC(Pin (POTENTIOMETRE_X_PIN))
potentiometre_Y = ADC(Pin (POTENTIOMETRE_Y_PIN))
stylo = Pin(STYLO_PIN, Pin.IN, Pin.PULL_DOWN)

ADC_MAX = 65535
DISTANCE = 100 #millimetres

# position presente et precedente 
x = 0.0
y = 0.0
ancien_x = None
ancien_y = None


def lecture():
    "lire les entrees de l'utilisateur x et y ainsi que le stylo abaiser ou lever"
    global x, y, ancien_x, ancien_y

    #lecture des deux potentiometre et du button pour le stylo
    x_adc = potentiometre_X.read_u16()
    y_adc = potentiometre_Y.read_u16()
    state = stylo.value()

    # 
    if ancien_x is not None and ancien_y is not None:
       x += (x_adc - ancien_x) * DISTANCE / ADC_MAX
       y += (y_adc - ancien_y) * DISTANCE / ADC_MAX

    ancien_x = x_adc
    ancien_y = y_adc

    return x, y, state # x, y est en millimetre et state est en True or False

def reinitialiser_lectures():
    global x, y, ancien_x, ancien_y

    x = 0
    y = 0

    ancien_x = potentiometre_X.read_u16()
    ancien_y = potentiometre_Y.read_u16()

