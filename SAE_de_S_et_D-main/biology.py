import json
import itertools


def est_base(c):
    """
    :param c: correspond à un seul caractère
    :return: renvoie une valeur boolene, soit True soit False
    Cette fonction vérifie si le caractère introduit en paramètre est bien un des
    caractères
    'A','T','G','C'
    """
    t = ["A", "T", "G", "C"]
    return c in t    # Retourne True si c est dans t


def est_adn(s):
    """
    :param s: correspond à une chaine de caractères
    :return: retourne une valeur booléne
    Cette fonction vérifie si dans la chaîne
    introduite il y a que les caractères 'A','T','G','C'
    """
    i = 0
    a = True
    while i < len(s) and a == True:
        if est_base(s[i]) == True:
            a = True
        else:
            a = False
        i = i + 1
    return a


def arn(adn):
    """
    :param adn: une chaine de caractère qui correspondent à un adn
    :return: La nouvelle chaine de caractère avec les 'T' qui sont changée
    par des "U"
    Cette fonction en prend une chaine de caractères (un adn) introduite en
    paramètres, vérifie si cela correspond bien à
    un adn ensuite elle elle transforme les caractères 'T' par des 'U'
    """
    nvx = ''
    if est_adn(adn) == True:
        for i in adn:
            if 'T' == i:
                nvx = nvx + 'U'
            else:
                nvx = nvx + i
        return nvx
    else:
        return None


def arn_to_codons(arn):
    """
    Cette fonction permet de decouper des ARN en codons (groupe de 3)
    :param arn:
    :return: t qui est le tableau final
    """
    a = arn
    r = len(arn)%3
    if 0 != r: # Si len(arn) n'est pas un multiple de 3, ca retourne le tableau final
               # moins le nombre de caractere restants
        a = arn[0: len(arn) - r]
    return [a[i: i+3] for i in range(0, len(a), 3)]

def load_dico_codons_aa(filename):
    """
    :param filename: ici codons_aa.json
    :return: le dico json
    """
    path = ('data/' + filename)
    file = open(path, 'r')
    return json.load(file)

def codons_stop(dico):
    """
    :param dico: ici le dico que renvoie la derniere fonction
    :return: le tabeleau avec les codons stop
    """
    tab = []
    a = [b + c + d for b, c, d in itertools.product(["A", "U", "G", "C"], repeat=3)] #fonction tirée d'internet qui fait un produit cartesien
    for i in a:
        if i not in dico:
            tab.append(i)
    return tab





def codons_to_aa(codons, dico):
    """
    :param codons:
    :param dico: ici le dico que renvoie la derniere fonction
    :return: le tableau avec comme valeurs les acides aminés
    """
    tab = []
    codon_stop = codons_stop(dico)
    for codon in codons:
        if codon in codon_stop:
            return tab
        else:
            tab.append(dico[codon])
    return tab

def nextIndice(




        tab, ind, elements):
    pass


def decoupe_sequence(seq, start, stop):
    pass


def codons_to_seq_codantes(codons, dico):
    pass


def seq_codantes_to_seq_aas(seq_codantes, dico):
    pass


def adn_encode_molecule(adn, dico, molecule):
    pass