import biology as by

def test_est_base():
    assert by.est_base('A') == True
    assert by.est_base('z') == False
    assert by.est_base( 0 ) == False
ok
ok juste att je te disquand tu peux refaire des modif
j'ai fini je fais juste un push la sur le git'
def test_est_adn():
    assert by.est_adn('AABBTR') == False
    assert by.est_adn('AACBTC') == True
    assert by.est_adn('AA00TR') == False

def test_arn(adn):
    assert by.arn()
    #rien

def test_arn_to_codons(arn):
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