def est_base(c):
    if c =='A' or c == 'T' or c == 'G' or c == 'C':
        return True 
    else:
        return False

def est_adn(s):
    for a in s :
        if est_base(a) == False:
            return False
        else:
            return True
print(est_adn('AABBTR'))
j'ai fini pour l'instant
je fait un push




def arn(adn):
    pass
vsy
cest bon ?
j'essaye de push ca pour voir'

def arn_to_codons(arn):
    pass


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
