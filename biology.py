def est_base(c):    #code bon
    """
    :param c: correspond à un seul caractère
    :return: renvoie une valeur boolene, soit True soit False
    Cette fonction vérifie si le caractère introduit en paramètre est bien un des caractères 'A','T','G','C'
    """
    if c == 'A' or c == 'T' or c == 'G' or c == 'C':
        return True 
    else:
        return False

def est_adn(s):    #code bon
    """
    :param s: correspond à une chaine de caractères
    :return: retourne une valeur booléne
    Cette fonction vérifie sii dans la chaîne introduite il y a que les caractères 'A','T','G','C'
    """
    #je modifie ce comm
    i = 0
    while i < len(s):
        if est_base(s[i]) == True:
            a = True
        else:
            return False
        i = i + 1
    return True


def arn(adn):    #code bon
    """
    :param adn: une chaine de caractère qui correspondent à un adn
    :return: si la nouvelle chaine de caractère avec les 'T' qui sont changée par de "U"
    Cette fonction en prend une chaine de caractères (un adn) introduite en paramètres, vérifie si cela correspond bien à
    un adn ensuite elle elle transforme les caractères 'T' par des 'U'
    """
    nvx = ''
    i = 0
    if est_adn(adn) == True:
        while i < len(adn):
            if adn[i] == 'T':
                nvx = nvx + 'U'
            else:
                nvx = nvx + adn[i]
            i = i + 1
        print(nvx)
        return nvx
    else:
        print("Ce n'est pas un adn !!!")
        return None


def arn_to_codons(arn):
    """
    :param arn:
    :return:
    """
    t = []
    codons = ""
    i = 0
    compt = 0
    if codons[compt] <= 2:
        while i < len(arn):
            codons = condons + arn[i] #####################################################
            print(i)                  ############# A TERMINERRRRRR #######################
            i = i + 1                 #####################################################
            print(codons)             # bonne nuit frero 
    if codons[]  
        t.append(codons)
    codons =


def load_dico_codons_aa(filename):
    pass

def codons_stop(dico):
    pass


def codons_to_aa(codons, dico):
    pass




def nextIndice(tab, ind, elements):
    pass


def decoupe_sequence(seq, start, stop):
    pass


def codons_to_seq_codantes(codons, dico):
    pass


def seq_codantes_to_seq_aas(seq_codantes, dico):
    pass


def adn_encode_molecule(adn, dico, molecule):
    pass
