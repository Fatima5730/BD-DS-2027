# ==========================================================
# Script : Importer les données du chômage au Maroc
#          et générer un graphique d'évolution
# Source des données : Haut-Commissariat au Plan (HCP)
# ==========================================================

# --- 1. Importer les bibliothèques ---
import pandas as pd
import matplotlib.pyplot as plt

# --- 2. Importer (charger) les données depuis le fichier CSV ---
# Le fichier doit être dans le même dossier que ce script,
# ou indique le chemin complet vers le fichier.
# sep=";" car le fichier a été enregistré depuis Excel avec un séparateur point-virgule
# decimal="," car Excel (en français) utilise la virgule comme séparateur décimal (ex: 9,9)
df = pd.read_csv("donnees_chomage_maroc.csv", sep=";", decimal=",")

# Afficher les premières lignes pour vérifier que l'import a bien fonctionné
print("Aperçu des données :")
print(df.head())

# Vérifier s'il y a des valeurs manquantes
print("\nValeurs manquantes par colonne :")
print(df.isna().sum())

# --- 3. Générer le graphique d'évolution du taux de chômage national ---
plt.figure(figsize=(9, 5))

plt.plot(
    df["annee"],
    df["taux_national"],
    marker="o",          # un point sur chaque année
    linewidth=2,
    color="#1f5c8b",
    label="Taux de chômage national"
)

# Ajouter le titre et les légendes des axes
plt.title("Évolution du taux de chômage au Maroc (2014-2025)", fontsize=13, fontweight="bold")
plt.xlabel("Année")
plt.ylabel("Taux de chômage (%)")
plt.legend()
plt.grid(axis="y", alpha=0.3)

# Afficher la valeur au-dessus de chaque point
for x, y in zip(df["annee"], df["taux_national"]):
    plt.annotate(f"{y}%", (x, y), textcoords="offset points", xytext=(0, 8), ha="center", fontsize=8)

plt.tight_layout()

# --- 4. Sauvegarder le graphique en image ---
plt.savefig("evolution_chomage_maroc.png", dpi=150)

# --- 5. Afficher le graphique à l'écran ---
plt.show()

print("\nGraphique généré et sauvegardé sous 'evolution_chomage_maroc.png'")