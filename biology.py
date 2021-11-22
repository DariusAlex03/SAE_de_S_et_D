def est_base(c):
    if c == 'A' or c == 'T' or c == 'G' or c == 'C':
        return True 
    else:
        return False
#ce code est bon je lai tester
def est_adn(s):
    i = 0
    while i < len(s):
        if est_base(s[i]) == True:
            a = True
        else:
            return False
        i = i + 1
    return True
# Ce code est bon je lai tester

def arn(adn):
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
    #ce code est bon. je lai tester
    #oublie pas de faire les teste pour les nouvelles fonctions !!!!!!!!!
    #jai fini tu peut push stv


def arn_to_codons(arn):
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
