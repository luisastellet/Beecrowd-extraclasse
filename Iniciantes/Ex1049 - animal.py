a = input()
b = input()
c = input()
if a == "vertebrado":
    if b == "ave":
        if c == "carnivoro":
            print("aguia")
        else: #onivoro
                print("pomba")
    else: #mamifero
        if c == "onivoro":
            print("homem")
        else: #herbivoro
            print("vaca")


else: #invertebrado
    if b == "inseto":
        if c == "hematofago":
            print("pulga")
        else: #hervivoro
            print("lagarta")
    else: #anelideo
        if c == "hematofago":
            print("sanguessuga")
        else: #onivoro
            print("minhoca")