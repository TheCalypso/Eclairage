# Paramètre pour l'arrondi
decimales_arrondi = 3                       # A CHANGER

a_longueur = 14                             # A CHANGER
b_largeur = 7                               # A CHANGER
hauteur_plafond = 3                         # A CHANGER
hauteur_plan_utile = 0.80                   # A CHANGER
flux_lumineux = 2800  # en lumens           # A CHANGER
puissance_luminaire = 21  # en watts        # A CHANGER
E = 500  # en lux                           # A CHANGER
M = 0.9  # facteur de maintenance  D        # A CHANGER

print("#################### START ####################")
# Calcul de la hauteur utile
hauteur_utile = round(hauteur_plafond - hauteur_plan_utile, decimales_arrondi)

# Calcul de l'efficacité lumineuse
Fe = round(flux_lumineux / puissance_luminaire, decimales_arrondi)

print("Hauteur utile:", hauteur_utile)
print("Efficacité lumineuse:", Fe)

# Calcul de K pour l'interpolation
K = round(((a_longueur * b_largeur) /
          ((a_longueur + b_largeur) * hauteur_utile)), decimales_arrondi)
print("K:", K)

# Valeurs pour l'interpolation
# REGARDER LES POURCENTAGES PLAFOND - MURS - SOL
# REGARDER LES POURCENTAGES PLAFOND - MURS - SOL
# REGARDER LES POURCENTAGES PLAFOND - MURS - SOL
# REGARDER LES POURCENTAGES PLAFOND - MURS - SOL
# REGARDER LES POURCENTAGES PLAFOND - MURS - SOL
# Les K sont à trouver dans le tableau dans la colonne de gauche
# Les U sont les valeurs EN FONCTION DE LA COLONNE !!!!!!
print("##################### ETAPE TABLEAU #######################")
U1 = 1.03                                   # A CHANGER
U2 = 1.08                                   # A CHANGER
K1 = 2                                    # A CHANGER
K2 = 2.5                                      # A CHANGER

# Calcul du delta U pour l'interpolation
Delatu = round(((K - K1) * (U2 - U1)) / (K2 - K1), decimales_arrondi)
print("Delta U:", Delatu)

# Calcul du facteur d'utilisation U
U = round(U1 + Delatu, decimales_arrondi)
print("Facteur d'utilisation U:", U)

P = round(1/(Fe*U*M), 7)
print("Efficience lumineuse en W/m²/lx:", P)

intensite_lumineuse = round(
    (E * a_longueur * b_largeur) / (M * U), decimales_arrondi)
print("Intensité lumineuse I:", intensite_lumineuse, "lm")

N = round(intensite_lumineuse / flux_lumineux, decimales_arrondi)
print("Nombre de luminaire à installer:", N)

# Séparation maximale recommandée
# Facteur S/H
print("##################### ETAPE PLACEMENT #####################")
facteur_s_h = 1.5                           # A CHANGER
a_nbr_luminaire = 5                         # A CHANGER
b_nbr_luminaire = 4                         # A CHANGER

s_max = round(facteur_s_h * hauteur_utile, decimales_arrondi)
print("Distance maximale recommandée:", s_max, "m")

# Placement des luminaires
s_a = round(a_longueur / a_nbr_luminaire, decimales_arrondi)
s_b = round(b_largeur / b_nbr_luminaire, decimales_arrondi)

print(s_a, s_b)

if s_a and s_b:
    print("Il faut mettre", a_nbr_luminaire, "en longueur a.")
    print("Il faut mettre", b_nbr_luminaire, "en longueur b.")
else:
    print("Il faut trouver une autre combinaison.")
    print("s_a", s_a)
    print("s_b", s_b)

E_corrigee = round(((a_nbr_luminaire * b_nbr_luminaire *
                   flux_lumineux) / intensite_lumineuse) * E, decimales_arrondi)
test = (a_nbr_luminaire * b_nbr_luminaire *
        flux_lumineux) / intensite_lumineuse
print("Eclairage corrgié est:", E_corrigee, "lux")
