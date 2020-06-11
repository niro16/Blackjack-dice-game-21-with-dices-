import random

class Terning:
    def __init__(self, antall_sider=6):
        self.__verdi = 1
        self.__sider = antall_sider

    def kast(self):
        self.__verdi = random.randint(1, self.__sider)

    def get_verdi(self):
        return self.__verdi

class Spiller:
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
        
        id=0
        for i in range(self.spillere):
            navn = input("Skriv navn på spiller: ")
            poeng = 0
            id += 1
            spiller = Spiller(id, navn, poeng)
            self.aktivespillere.append(spiller)


    def flere_omganger(self):
        vinnere = []
        poeng = []
        for spiller in self.aktivespillere:
            while True:
                print("{} har {} poeng".format(spiller.get_name(), spiller.get_poengsum()))
                print("Vil {} kaste terningen?".format(spiller.get_name()))
                answer = input("(y/n)")
                if answer == "y":
                    self.terning.kast()
                    ny_poengsum = spiller.get_poengsum() + self.terning.get_verdi()
                    spiller.set_poengsum(ny_poengsum)
                    if ny_poengsum > 21:
                        print("{} er ute av spillet, du fikk {}".format(spiller.get_name(), ny_poengsum))
                        print("\n\n\n")
                        break
                    elif ny_poengsum == 21:
                        print("{} har oppnådd 21".format(spiller.get_name()))
                        vinnere.append(spiller)
                        print("\n\n\n")
                        break
                elif answer == "n":
                    print("Du fikk så mange poeng {}".format(spiller.get_poengsum()))
                    vinnere.append(spiller)
                    print("\n\n\n")
                    break
                else:
                    print("Tast enten 'y' eller 'n'")
        
        uavgjort = []
        if len(vinnere) > 1: ########## Sjekk denne 
            for i in vinnere:
                poeng.append(i.get_poengsum())
            max_value = max(poeng)
            for j in range(len(vinnere)):
                if vinnere[j].get_poengsum() == max_value:
                    uavgjort.append(vinnere[j].get_name())
            if uavgjort and len(uavgjort) > 1:
                print("Uavgjort mellom spillerne: {}".format(uavgjort))
            else:
                info = poeng.index(max_value)
                print("\nVinneren av spillet er: \n{} med {} poeng".format(vinnere[info].get_name(), vinnere[info].get_poengsum()))
        elif len(vinnere) < 1:
            print("Ingen vant! :(")
        else:
            for i in vinnere:
                poeng.append(i.get_poengsum())
            max_value = max(poeng)
            info = poeng.index(max_value)
            print("\nVinneren av spillet er: \n{} med {} poeng".format(vinnere[info].get_name(), vinnere[info].get_poengsum()))


if __name__ == "__main__":
    while True:
        try:
            nr_spillere = int(input("Skriv inn antall spillere: "))
            Tjueet(nr_spillere).flere_omganger()
            print("Vil du/dere spille igjen?")
            ans = input("(y/n)")
            if ans == "y":
                pass
            elif ans == "n":
                break
        except ValueError:
            print("Skriv inn et heltall!!")
