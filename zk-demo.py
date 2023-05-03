import hashlib


def hashify(secret):
    return hashlib.sha256(secret.encode()).hexdigest()


def verifyKnowledge(info1, info2):
    info1_hash = hashify(info1)
    info2_hash = hashify(info2)

    if (info1_hash == info2_hash):
        print("Match kr gya")
    else:
        print("Match nhi krra")


knldg1 = "Treasure location is XYfcZ"
knldg2 = "Treasure location is XYZ"

#! Trynna match knowledge of one source to another
verifyKnowledge(knldg1, knldg2) #!This way we matched the knowledge without even sharing the actuall info
