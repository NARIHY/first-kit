class CompteurAlphabet:
    def __init__(self, lettre_debut: str, lettre_fin: str):
        self.lettre_debut = lettre_debut.upper()
        self.lettre_fin = lettre_fin.upper()

    def valider_lettres(self) -> bool:
        """
        Vérifie que les deux lettres sont valides (une seule lettre, alphabétique).
        """
        return (
            self.lettre_debut.isalpha() and len(self.lettre_debut) == 1 and
            self.lettre_fin.isalpha() and len(self.lettre_fin) == 1
        )

    def position_dans_alphabet(self, lettre: str) -> int:
        """
        Retourne la position de la lettre dans l'alphabet (A = 1, B = 2, ..., Z = 26).
        """
        return ord(lettre) - ord('A') + 1

    def compter_lettres(self) -> int:
        """
        Compte le nombre de lettres entre les deux lettres inclusivement.
        """
        position_debut = self.position_dans_alphabet(self.lettre_debut)
        position_fin = self.position_dans_alphabet(self.lettre_fin)
        return abs(position_fin - position_debut) + 1

    def afficher_resultat(self):
        """
        Affiche le nombre de lettres entre les deux lettres.
        """
        if not self.valider_lettres():
            print("X Veuillez entrer deux lettres valides (une seule lettre de A à Z).")
            return

        nombre = self.compter_lettres()
        print(f"Il y a {nombre} lettres entre {self.lettre_debut} et {self.lettre_fin} (inclusivement).")


# --- Exemple d'utilisation ---
if __name__ == "__main__":
    lettre1 = input("Entrez la première lettre : ")
    lettre2 = input("Entrez la deuxième lettre : ")

    compteur = CompteurAlphabet(lettre1, lettre2)
    compteur.afficher_resultat()
