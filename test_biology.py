import biology as by

def test_est_base():
    assert by.est_base('A')
    assert not by.est_base('z')
    assert not by.est_base('0')

def test_est_adn():
    assert not by.est_adn('AABBTR')
    assert by.est_adn('AACGTC')
    assert not by.est_adn('AA00TR')

def test_arn(adn):
    assert by.arn('ATGCATGC')
    assert not by.arn('AUJHUIBHJ')
    assert by.arn('A')

def test_arn_to_codons(arn):
    assert by.arn_to_codons('ARGCATGCATCG') == (["ARG", "CAT", "GCA", "TCG"])
    assert by.arn_to_codons()

def test_load_dico_codons_aa(filename):
    assert by.load_dico_codons_aa()

def test_codons_stop(dico):
    assert by.codons_stop()


def test_codons_to_aa(codons, dico):
    assert by.codons_to_aa()

def test_nextIndice(tab, ind, elements):
    assert by.nextIndice()


def test_decoupe_sequence(seq, start, stop):
    assert by.decoupe_sequence()


def test_codons_to_seq_codantes(codons, dico):
    assert by.codons_to_seq_codantes()


def test_seq_codantes_to_seq_aas(seq_codantes, dico):
    assert by.seq_codantes_to_seq_aas()


def test_adn_encode_molecule(adn, dico, molecule):
    assert by.adn_encode_molecule()