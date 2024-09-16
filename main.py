"""Ce fichier va permettre de vérifier si un nombre est premier ou pas
"""

#### Fonction secondaire


def isprime(n):
    """
    Permet de vérifier si un nombre est premier c'est ou non.
    
    >>>isprime(2)
    True
    
    >>>isprime(6679)
    True
    """
    if n==1:
        return False
    for i in range (2,n):
        if n%i == 0:

            return False
    return True


    # votre code ici


#### Fonction principale


def main():
    """
    Permet de faire appel a des fonctions
    """
    print(isprime(10))
    print(isprime(19))
    print(isprime(6679))
    print(isprime(1))
    # vos appels à la fonction secondaire ici

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
