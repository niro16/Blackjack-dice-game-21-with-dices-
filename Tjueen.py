import random

class Terning:
    def __init__(self, antall_sider=6):
        self.__verdi = 1
        self.__sider = antall_sider

    def kast(self):
        self.__verdi = random.randint(1, self.__sider)

    def get_verdi(self):
        return self.__verdi

class Spiller():
    def __init__(self, id, name, poengsum=0):
        self.id = id
        self.name = name
        self.poengsum = poengsum

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_poengsum(self):
        return self.poengsum

    def set_poengsum(self, ny_poengsum):
        if ny_poengsum > 0:
            self.poengsum = ny_poengsum
        else:
            raise ValueError("Poengsum kan ikke være negativt")

    def set_name(self, new_name):
        if new_name:
            self.name = new_name
        else:
            raise ValueError("Navn kan ikke være tomt")

class Tjueet:
    def __init__(self, spillere):
        self.spillere = spillere
        self.terning = Terning()
        self.aktivespillere = []

        for i in range(self.spillere):
            en_spiller = lag_spiller(self.terning)
            self.aktivespillere.append(en_spiller)


    def flere_omganger(self):
        vinnere = []
        poeng = []
        for spiller in self.aktivespillere:
            while True:
                print("{} har {} poeng".format(spiller.get_name(), spiller.get_poengsum()))
                print("Vil {} kaste terningen en gang til?".format(spiller.get_name()))
                answer = input("(y/n)")
                if answer == "y":
                    self.terning.kast()
                    ny_poengsum = spiller.get_poengsum() + self.terning.get_verdi()
                    if ny_poengsum > 21:
                        print("{} tapte, du fikk {}".format(spiller.get_name(), ny_poengsum))
                        break
                    spiller.set_poengsum(ny_poengsum)
                elif answer == "n":
                    print("Du fikk så mange poeng {}".format(spiller.get_poengsum()))
                    vinnere.append(spiller)
                    break
                else:
                    print("Tast enten 'y' eller 'n'")

        for i in vinnere:
            poeng.append(i.get_poengsum())
        max_value = max(poeng)
        info = poeng.index(max_value)

        print("\nVinneren av spillet er: \n{} ".format(vinnere[info]))

def lag_spiller(terning):
    id = int(input("Skriv inn ID på spiller: "))
    navn = input("Skriv navn på spiller: ")
    poeng = 0
    for i in range(3):
        terning.kast()
        poeng += terning.get_verdi()
    spiller = Spiller(id, navn, poeng)
    return spiller



if __name__ == "__main__":
    while True:
        try:
            nr_spillere = int(input("Skriv inn antall spillere: "))
            Tjueet(nr_spillere).flere_omganger()
            break
        except ValueError:
            print("Skriv inn et heltall!!")
