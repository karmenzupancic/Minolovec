import random

NEVELJAVNA_POTEZA = '?'
PORAZ = 'X'
VARNO = 'V'
KONEC_IGRE = 'K'

class Plosca:
    def __init__(self, visina=20, sirina=20, stevilo_min=15):
        self.visina = visina
        self.sirina = sirina
        self.stevilo_min = stevilo_min
        self.mine = []
        self.seznam_min(stevilo_min)
        self.mreza = [[0 for i in range(self.visina)] for j in range(self.sirina)]
        self.spreminjanje_mreze(self.mreza)
        self.poskusi = set()
        self.poteze = 0
        self.varna = set()
        self.varna_polja()
        
    def __repr__(self):
        return 'Plosca(visina={}, sirina={}, mine={})'.format(
            self.visina, self.sirina, self.mine
        )

    def __str__(self):
        polja = []
        for _ in range(self.visina):
            polja.append(self.sirina * [' '])

        for vrstica, stolpec in self.poskusi:
            polja[vrstica][stolpec] = str(self.mreza[vrstica][stolpec])


        niz = ''
        rob = '+' + self.sirina * '-' + '+\n'
        for vrstica in polja:
            niz += '|' + ''.join(vrstica) + '|\n'
        return rob + niz + rob
    

    def seznam_min(self, stevilo_min):                
        while self.stevilo_min > 0:
            i = random.randint(0, self.visina - 1)
            j = random.randint(0, self.sirina - 1)
            if (i, j) not in self.mine:
                self.mine.append((i, j))
                self.stevilo_min -= 1
        return self.mine


    def spreminjanje_mreze(self, mreza):
        '''Spremeni matriko ničel, tako, da za vsako polje pove, koliko min ima v bližini.
        '''
        for vrstica, stolpec in self.mine:
            self.mreza[vrstica][stolpec] = -1

            okolica_vrstice = range(vrstica - 1, vrstica + 2)
            okolica_stolpca = range(stolpec - 1, stolpec + 2)

            for i in okolica_vrstice:
                for j in okolica_stolpca:
                    if (0 <= i < self.visina and 0 <= j < self.sirina and self.mreza[i][j] != -1):
                        self.mreza[i][j] += 1



    def klik_polja(self, vrstica, stolpec):
        '''Preveri, kaj je v mrezi v ozadju na koordinati (vrstica, stolpec).
        Če tam je mina, vrne PORAZ, če poteza ni veljavna, nam vrne NEVELJAVNA POTEZA.
        Če pa tam ni mine, pa VARNO, oziroma KONEC_IGE, ko smo že kliknili vsa varna polja.
        '''
        if 0 <= vrstica < self.visina and 0 <= stolpec < self.sirina and (vrstica, stolpec) not in self.poskusi:
            self.poteze += 1
            self.poskusi.add((vrstica, stolpec))
            if (vrstica, stolpec) not in self.mine:
                    if self.konec_igre():
                        return KONEC_IGRE
                    else:
                        return VARNO
            return PORAZ
        else:
            return NEVELJAVNA_POTEZA




    def varna_polja(self):
        '''Vrne množico vseh polj, ki so varna (niso mine).'''
        for i in range(self.visina):
            for j in range(self.sirina):
                if (i, j) not in self.mine:
                    self.varna.update((i, j))
        return self.varna
    
    def konec_igre(self):
        for polje in self.varna:
            if polje not in self.poskusi:
                return False
        return True
        



    
