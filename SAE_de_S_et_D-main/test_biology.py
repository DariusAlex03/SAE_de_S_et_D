import biology as by

def test_est_base():
    assert by.est_base('A')
    assert not by.est_base('z')
    assert not by.est_base('0')
    print("La fonction est_base est ok !")

def test_est_adn():
    assert not by.est_adn('AABBTR')
    assert by.est_adn('AACGTC')
    assert not by.est_adn('AA00TR')
    print("La fonction est_adn est ok !")


def test_arn():
    assert by.arn('ATGCATGC')
    assert not by.arn('AUJHUIBHJ')
    assert by.arn('A')
    print("La fonction arn est ok !")

def test_arn_to_codons():
    assert by.arn_to_codons('ARGCATGCA') == (["ARG", "CAT", "GCA"])
    assert by.arn_to_codons('ARGCATGCATC') == (["ARG", "CAT", "GCA"])
    print("La fonction arn_to_codons est ok !")


def test_load_dico_codons_aa():
    assert by.load_dico_codons_aa("codons_aa.json") != None
    print("La fonction load_dico_codons_aa est ok !")

def test_codons_stop():
    codons = by.load_dico_codons_aa("codons_aa.json")
    assert by.codons_stop(codons) == ["AGA", "AGG", "UAA", "UAG"]
    print("La fonction codons_stop est ok ! ")



def test_codons_to_aa():
    codons = by.load_dico_codons_aa("codons_aa.json")
    assert by.codons_to_aa(["CGU", "AAU", "UAA", "GGG", "CGU"], codons) == ["Arginine", "Asparagine"]
    print("La fonction codons_to_aa est ok !")

def test_nextIndice():
    assert by.nextIndice()
    print("La fonction est ok !")


def test_decoupe_sequence():
    assert by.decoupe_sequence()
    print("La fonction est ok !")


def test_codons_to_seq_codantes():
    assert by.codons_to_seq_codantes()
    print("La fonction est ok !")

def test_seq_codantes_to_seq_aas():
    assert by.seq_codantes_to_seq_aas()
    print("La fonction est ok !")

def test_adn_encode_molecule():
    assert by.adn_encode_molecule()
    print("La fonction est ok !")


if __name__ == "__main__":
    test_est_base()
    test_est_adn()
    test_arn()
    test_arn_to_codons()
    test_load_dico_codons_aa()
    test_codons_stop()
    test_codons_to_aa()