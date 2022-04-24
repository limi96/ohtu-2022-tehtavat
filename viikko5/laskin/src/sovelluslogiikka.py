class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos
        self.edellinen_luku_lista = []
        self.edellinen_luku_lista.append(tulos)

    def muista_edellinen_luku(self): 
        self.edellinen_luku_lista.append(self.tulos)

    def get_edellinen_luku(self):
        listan_pituus = len(self.edellinen_luku_lista)
        return self.edellinen_luku_lista[listan_pituus-1]

    def miinus(self, arvo):
        self.muista_edellinen_luku()
        self.tulos = self.tulos - arvo

    def plus(self, arvo):
        self.muista_edellinen_luku()
        self.tulos = self.tulos + arvo

    def nollaa(self):
        self.tulos = 0

    def kumoa(self):
        self.aseta_arvo(self.get_edellinen_luku())

    def aseta_arvo(self, arvo):
        self.tulos = arvo

