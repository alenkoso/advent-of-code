with open("input.txt") as input:
    koncna_povrsina = 0
    koncna_dolzina = 0
    for dimenzije in input:
        sirina, visina, dolzina = sorted(int(i) for i in dimenzije.split("x"))
        koncna_povrsina = koncna_povrsina + 2 * (
                    dolzina * sirina + sirina * visina + visina * dolzina) + sirina * visina  # part 1
        koncna_dolzina = koncna_dolzina + dolzina * sirina * visina + 2 * (sirina + visina)  # part 2

    print("Total square feet of wrapping paper to order: ", koncna_povrsina)
    print("Total feet of ribbon to order: ", koncna_dolzina)
