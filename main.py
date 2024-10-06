import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

class BudgetApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Kalkulator kućnog budžeta")
        
        # Promjenjive za prihode i rashode
        self.prihod = tk.DoubleVar()
        self.rashod = tk.DoubleVar()
        self.kategorija = tk.StringVar(value="Stanovanje")

        # GUI elementi
        tk.Label(root, text="Unesite prihod:").grid(row=0, column=0)
        tk.Entry(root, textvariable=self.prihod).grid(row=0, column=1)
        
        tk.Label(root, text="Unesite rashod:").grid(row=1, column=0)
        tk.Entry(root, textvariable=self.rashod).grid(row=1, column=1)
        
        tk.Label(root, text="Kategorija:").grid(row=2, column=0)
        tk.OptionMenu(root, self.kategorija, "Stanovanje", "Hrana", "Transport", "Ostalo").grid(row=2, column=1)
        
        tk.Button(root, text="Dodaj rashod", command=self.dodaj_rashod).grid(row=3, column=0, columnspan=2)

        # Prikaz trenutačnog balansa
        self.balance_label = tk.Label(root, text="Trenutni budžet: 0.0")
        self.balance_label.grid(row=4, column=0, columnspan=2)

        # Dodavanje gumba za tortni dijagram
        tk.Button(root, text="Prikaz tortnog dijagrama", command=self.prikazi_tortni_diagram).grid(row=5, column=0, columnspan=2)

        # Budžet
        self.balance = 0.0
        self.rashodi = {}

    def dodaj_rashod(self):
        prihod = self.prihod.get()
        rashod = self.rashod.get()
        kategorija = self.kategorija.get()

        # Ažuriraj saldo
        self.balance += prihod - rashod
        self.balance_label.config(text=f"Trenutni budžet: {self.balance:.2f}")

        # Dodaj rashod po kategorijama
        if kategorija in self.rashodi:
            self.rashodi[kategorija] += rashod
        else:
            self.rashodi[kategorija] = rashod

        # Spremi podatke u datoteku
        self.spremi_podatke()

    def spremi_podatke(self):
        try:
            with open("budzet.txt", "a") as file:
                file.write(f"Prihod: {self.prihod.get()}, Rashod: {self.rashod.get()} ({self.kategorija.get()})\n")
        except Exception as e:
            messagebox.showerror("Greška", str(e))

    def prikazi_tortni_diagram(self):
        kategorije = list(self.rashodi.keys())
        vrijednosti = list(self.rashodi.values())
        
        plt.figure(figsize=(6,6))
        plt.pie(vrijednosti, labels=kategorije, autopct='%1.1f%%', startangle=90)
        plt.title("Rashodi po kategorijama")
        plt.show()


# Pokreni aplikaciju
root = tk.Tk()
app = BudgetApp(root)
root.mainloop()


