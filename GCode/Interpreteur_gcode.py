from Controle_servos import deplacer, desactiver, abaisser_stylo, relever_stylo



def executeur (servos, commande, parametres):
    """Responsable: TheKingyveL

    Interprète une commande. Pour G1, récupère les angles S (épaule) et
    E (coude), applique les corrections de calibration puis déplace le
    bras. Pour M3/M5, abaisse/relève le stylo. Pour M18, désactive les
    servos et signale l'arrêt de l'exécution du fichier.

    Entrées : servos (dict des servos); commande (str); parametres (dict
              de paramètres numériques); table_calibration (dict).
    Sorties : booléen - True lorsque la commande demande l'arrêt (M18),
              False autrement.
    Appels : appliquer_corrections(), deplacer(), abaisser_stylo(),
             relever_stylo(), desactiver()."""
    
    if commande == "G1":
        deplacer(servos, parametres.get("S"), parametres.get("E"))
                          
    elif commande == "M3":
        abaisser_stylo(servos["poignet"])
      
    elif commande == "M5":
        relever_stylo(servos["poignet"])
      
    elif commande == "M18":
        desactiver(servos)
        return True

    else:
        print("commande non reconnue: ", commande)

    return False
