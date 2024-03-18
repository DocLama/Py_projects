import tkinter as tk
from tkinter import simpledialog, messagebox

def beaufort_chiffre(texte, cle):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    chiffre = ""
    for i, lettre in enumerate(texte.upper()):
        if lettre in alphabet:
            pos_texte = alphabet.find(lettre)
            pos_cle = alphabet.find(cle.upper()[i % len(cle)])
            nouvelle_lettre = alphabet[(pos_cle - pos_texte) % len(alphabet)]
            chiffre += nouvelle_lettre
        else:
            chiffre += lettre
    return chiffre

def beaufort_dechiffre(texte_chiffre, cle):
    return beaufort_chiffre(texte_chiffre, cle)

def process():
    choice = simpledialog.askstring("Input", "Voulez-vous chiffrer ou déchiffrer? (C/D)")
    texte = simpledialog.askstring("Input", "Entrez votre texte:")
    cle = simpledialog.askstring("Input", "Entrez votre clé:")

    if choice.upper() == 'C':
        result = beaufort_chiffre(texte, cle)
        messagebox.showinfo("Résultat", f"Texte chiffré: {result}")
    elif choice.upper() == 'D':
        result = beaufort_dechiffre(texte, cle)
        messagebox.showinfo("Résultat", f"Texte déchiffré: {result}")
    else:
        messagebox.showerror("Erreur", "Choix invalide. Veuillez entrer 'C' pour chiffrer ou 'D' pour déchiffrer.")


root = tk.Tk()
root.withdraw() 

process()
