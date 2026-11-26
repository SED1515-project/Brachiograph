def traduit(angle: float) -> int:
	 """
    Responsable: -

    Limite l'angle à [0, 180] degrés, puis le convertit en valeur entière
    de rapport cyclique PWM utilisée par la méthode duty_u16().

    Entrées : angle (float, degrés).
    Sorties : int, valeur PWM.
    Appels : aucun.
    """

	MIN = 1638 # 0 degrés
	MAX = 8192 # 180 degrés
	DEG = (MAX - MIN) / 180 # valeur par degré

	# Limite l'angle à une valeur comprise entre 0 et 180 degrés
	angle = max(0, min(180, angle))

	return int(angle * DEG + MIN)
