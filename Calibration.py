def calibrer(nom, servo, autre, fichier, debut=0, pas=10):
    """
    Responsable: TheKingyveL

    Effectue une séquence de calibration pour un servo à la fois. L'autre
    servo est maintenu à une position de référence. Pour chaque angle
    demandé, l'équipe mesure l'angle physique et ajoute la mesure au
    fichier de calibration.

    Entrées : nom (str, 'epaule' ou 'coude'); servo (objet PWM à calibrer);
              autre (objet PWM maintenu à 90 degrés); fichier (str, chemin
              du fichier); debut (int, angle initial); pas (int, intervalle,
              normalement 10 degrés).
    Sorties : aucune (None); les mesures sont ajoutées au fichier.
    Appels : commande d'angle servo, temporisation, saisie utilisateur,
             écriture de fichier (à préciser lors de l'implémentation).
    """
    pass


def calibration_configuration(fichier):
    """
    Responsable: TheKingyveL

    Lit les mesures stockées dans le fichier et construit une table de
    corrections distincte pour l'épaule et le coude. Chaque mesure associe
    l'angle demandé à l'erreur (angle demandé - angle mesuré). Trie les
    points pour permettre l'interpolation.

    Entrées : fichier (str, chemin du fichier de calibration).
    Sorties : dict de la forme {'epaule': [(angle, correction), ...],
              'coude': [(angle, correction), ...]}.
    Appels : ouverture/lecture de fichier, conversion numérique, tri.
    """
    pass


def correction(points, angle):
    """
    Responsable: TheKingyveL

    Calcule une correction pour l'angle demandé par interpolation linéaire
    entre deux mesures voisines. Si aucune paire ne couvre l'angle, la
    correction prévue est 0.0, conformément au principe du Lab 8.

    Entrées : points (liste de tuples (angle_mesure, correction));
              angle (float, angle désiré en degrés).
    Sorties : float, correction en degrés.
    Appels : parcours des points et calcul d'interpolation.
    """
    pass


def appliquer_corrections(epaule, coude, table_calibration):
    """
    Responsable: TheKingyveL

    Applique séparément la correction de l'épaule et du coude aux angles
    calculés. Un angle égal à None reste None, afin de permettre les
    déplacements partiels déjà acceptés par deplacer().

    Entrées : epaule et coude (float ou None, degrés); table_calibration
              (dict produit par calibration_configuration()).
    Sorties : tuple (epaule_corrigee, coude_corrige), valeurs en degrés.
    Appels : correction() pour chaque angle présent.
    """
    pass
