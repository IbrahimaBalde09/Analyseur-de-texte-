import re
from collections import Counter

def charger_texte():
    """Charge un texte depuis un fichier ou l'entrée utilisateur."""
    choix = input("Voulez-vous analyser un fichier texte ? (o/n) : ")
    if choix.lower() == 'o':
        chemin = input("Entrez le chemin du fichier : ")
        try:
            with open(chemin, 'r', encoding='utf-8') as fichier:
                return fichier.read()
        except FileNotFoundError:
            print("Fichier introuvable. Veuillez réessayer.")
            return charger_texte()
    else:
        return input("Entrez votre texte : ")

def compter_caracteres(texte):
    """Compte le nombre total de caractères."""
    return len(texte)

def compter_mots(texte):
    """Compte le nombre de mots dans le texte."""
    mots = re.findall(r'\b\w+\b', texte.lower())
    return len(mots)

def compter_phrases(texte):
    """Compte le nombre de phrases en considérant les signes de ponctuation."""
    phrases = re.split(r'[.!?]+', texte)
    return len([p for p in phrases if p.strip()])

def mots_frequents(texte, n=5):
    """Retourne les N mots les plus fréquents."""
    mots = re.findall(r'\b\w+\b', texte.lower())
    compteur = Counter(mots)
    return compteur.most_common(n)

def rechercher_mot(texte, mot):
    """Cherche combien de fois un mot apparaît dans le texte."""
    mots = re.findall(r'\b\w+\b', texte.lower())
    return mots.count(mot.lower())

if __name__ == "__main__":
    texte = charger_texte()
    print("\n--- Analyse du texte ---")
    print(f"Nombre de caractères : {compter_caracteres(texte)}")
    print(f"Nombre de mots : {compter_mots(texte)}")
    print(f"Nombre de phrases : {compter_phrases(texte)}")
    
    print("\nMots les plus fréquents :")
    for mot, freq in mots_frequents(texte):
        print(f"{mot}: {freq}")
    
    mot_recherche = input("\nEntrez un mot à rechercher : ")
    print(f"Le mot '{mot_recherche}' apparaît {rechercher_mot(texte, mot_recherche)} fois.")
