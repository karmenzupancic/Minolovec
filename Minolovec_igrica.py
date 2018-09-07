import tkinter as tk
import model

class Minolovec:
    def __init__(self, okno):
        self.plosca = model.Plosca(10, 10)

        self.obvestilo = tk.Label(okno, text='Pozdravljen v Minolovcu!')
        self.obvestilo.grid(row=0, column=0)


        self.stevec_potez = tk.Label(okno, text='0')
        self.stevec_potez.grid(row=0, column=1)

        prikaz_plosce = tk.Frame(okno)
        self.gumbi = []
        for vrstica in range(self.plosca.visina):
            vrstica_gumbov = []
            for stolpec in range(self.plosca.sirina):
                def pritisni_gumb(vrstica=vrstica, stolpec=stolpec):
                    self.klik(vrstica, stolpec)
                gumb = tk.Button(prikaz_plosce, text='', height=1, width=1, command=pritisni_gumb)
                gumb.grid(row=vrstica, column=stolpec)
                vrstica_gumbov.append(gumb)
            self.gumbi.append(vrstica_gumbov)
        prikaz_plosce.grid(row=1, column=0, columnspan=2)


    def klik(self, vrstica, stolpec):
        rezultat = self.plosca.klik_polja(vrstica, stolpec)

        if rezultat == model.VARNO:
            self.gumbi[vrstica][stolpec].config(text=str(self.plosca.mreza[vrstica][stolpec]), state='disabled')
            self.obvestilo.config(text='Varno polje :)')

            for i in range(3):
                for j in range(3):
                    if (0 <= (vrstica - 1 + i) < self.plosca.visina and 0 <= (stolpec - 1 + j) < self.plosca.sirina and (vrstica - 1 + i, stolpec - 1 + j) not in self.plosca.mine):
                        self.gumbi[vrstica - 1 + i][stolpec - 1 + j].config(text=str(self.plosca.mreza[vrstica - 1 + i][stolpec - 1 + j]), state='disabled')
    
                        
        elif rezultat == model.KONEC_IGRE:
            for vrstica_gumbov in self.gumbi:
                for gumb in vrstica_gumbov:
                    gumb.config(state='disabled')
            self.obvestilo.config(text='ZMAGA!')
            
            
        elif rezultat == model.PORAZ:
            self.gumbi[vrstica][stolpec].config(text="X", state='disabled')
            for vrstica_gumbov in self.gumbi:
                for gumb in vrstica_gumbov:
                    gumb.config(state='disabled')
            self.obvestilo.config(text='O ne! Zadel si mino!')

        self.stevec_potez.config(text=str(self.plosca.poteze))

okno = tk.Tk()
moj_stevec = Minolovec(okno)
okno.mainloop()
