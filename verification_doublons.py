class VerificateurDoublons:
    def __init__(self, numeros):
        self.numeros = numeros

    def obtenir_doublons(self):
        compteur = {}
        for numero in self.numeros:
            compteur[numero] = compteur.get(numero, 0) + 1
        doublons = [numero for numero, nb in compteur.items() if nb > 1]
        return doublons

# Exemple de test
if __name__ == "__main__":
    numeros = input("Entrez les numéros séparés par des espaces : ")
    liste_numeros = [int(x) for x in numeros.split()]
    v = VerificateurDoublons(liste_numeros)
    print(v.obtenir_doublons())  # Affichera [1, 2]
