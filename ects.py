####################################################################################
#####             ECTS calculator                                               ####
#####    for the courses selection in the dual degree ENSAE - M2DS              ####
####################################################################################

import tkinter as tk
from tkinter import messagebox

ects_master_ds = 0
ects_ensae_s1 = 0
ects_ensae_s2 = 0


def ajouter_matiere():
    global ects_master_ds, ects_ensae_s1, ects_ensae_s2
    
    nom_matiere = nom_matiere_var.get()
    ects = int(ects_var.get())
    formation_choisie = formation_var.get()
    semestre_choisi = semestre_var.get()
    transfert_ects = int(transfert_var.get())
    transfert_formation = transfert_var_formation.get()

    if nom_matiere == "":
        messagebox.showwarning("Erreur", "Veuillez entrer le nom de la matière.")
        return

    if formation_choisie == "Master DS":
        ects_master_ds += ects
        liste_master_ds.insert(tk.END, f"{nom_matiere}: {ects} ECTS")
        if transfert_formation in ["ENSAE S1", "ENSAE S2"]:
            if transfert_formation == "ENSAE S1":
                ects_ensae_s1 += transfert_ects
                liste_ensae_s1.insert(tk.END, f"Transfert de {nom_matiere}: {transfert_ects} ECTS")
            elif transfert_formation == "ENSAE S2":
                ects_ensae_s2 += transfert_ects
                liste_ensae_s2.insert(tk.END, f"Transfert de {nom_matiere}: {transfert_ects} ECTS")
            
    elif formation_choisie == "ENSAE":
        if semestre_choisi == "S1":
            ects_ensae_s1 += ects
            liste_ensae_s1.insert(tk.END, f"{nom_matiere}: {ects} ECTS")
        elif semestre_choisi == "S2":
            ects_ensae_s2 += ects
            liste_ensae_s2.insert(tk.END, f"{nom_matiere}: {ects} ECTS")
            
        if transfert_formation == "Master DS":
            ects_master_ds += transfert_ects
            liste_master_ds.insert(tk.END, f"Transfert de {nom_matiere}: {transfert_ects} ECTS")

    # Maj crédits affichés
    lbl_ects_master.config(text=f"ECTS Master DS: {ects_master_ds}")
    lbl_ects_ensae_s1.config(text=f"ECTS ENSAE S1: {ects_ensae_s1}")
    lbl_ects_ensae_s2.config(text=f"ECTS ENSAE S2: {ects_ensae_s2}")

    verifier_validation()

def supprimer_matiere():
    global ects_master_ds, ects_ensae_s1, ects_ensae_s2

    selection_master = liste_master_ds.curselection()
    selection_ensae_s1 = liste_ensae_s1.curselection()
    selection_ensae_s2 = liste_ensae_s2.curselection()

    if selection_master:
        item = liste_master_ds.get(selection_master)
        ects = int(item.split(": ")[1].split()[0])
        ects_master_ds -= ects
        liste_master_ds.delete(selection_master)
        lbl_ects_master.config(text=f"ECTS Master DS: {ects_master_ds}")
    
    elif selection_ensae_s1:
        item = liste_ensae_s1.get(selection_ensae_s1)
        ects = int(item.split(": ")[1].split()[0])
        ects_ensae_s1 -= ects
        liste_ensae_s1.delete(selection_ensae_s1)
        lbl_ects_ensae_s1.config(text=f"ECTS ENSAE S1: {ects_ensae_s1}")
    
    elif selection_ensae_s2:
        item = liste_ensae_s2.get(selection_ensae_s2)
        ects = int(item.split(": ")[1].split()[0])
        ects_ensae_s2 -= ects
        liste_ensae_s2.delete(selection_ensae_s2)
        lbl_ects_ensae_s2.config(text=f"ECTS ENSAE S2: {ects_ensae_s2}")
    

    verifier_validation()

def verifier_validation():
    if ects_master_ds < 42:
        lbl_validation.config(text="Validation Master DS: INSUFFISANTE (moins de 42 ECTS)")
    else:
        lbl_validation.config(text="Validation Master DS: OK")


root = tk.Tk()# fenêtre principale
root.title("Calcul des ECTS")

# Variables
nom_matiere_var = tk.StringVar(root)
ects_var = tk.StringVar(root)
formation_var = tk.StringVar(root)
formation_var.set("Master DS")

semestre_var = tk.StringVar(root)
semestre_var.set("S1")

transfert_var = tk.StringVar(root)
transfert_var.set("0")

transfert_var_formation = tk.StringVar(root)
transfert_var_formation.set("Aucun")

# UI
frame = tk.Frame(root)
frame.pack(pady=10)

lbl_nom_matiere = tk.Label(frame, text="Nom de la matière:")
lbl_nom_matiere.pack()

entry_nom_matiere = tk.Entry(frame, textvariable=nom_matiere_var)
entry_nom_matiere.pack()

lbl_ects = tk.Label(frame, text="Nombre de crédits ECTS:")
lbl_ects.pack()

entry_ects = tk.Entry(frame, textvariable=ects_var)
entry_ects.pack()

lbl_formation = tk.Label(frame, text="Attribuer à:")
lbl_formation.pack()

# Option pour choisir la formation à laquelle attribuer les crédits
menu_formation = tk.OptionMenu(frame, formation_var, "Master DS", "ENSAE")
menu_formation.pack()

# choix du semestre si ENSAE est choisi
lbl_semestre = tk.Label(frame, text="Semestre (si ENSAE):")
lbl_semestre.pack()

menu_semestre = tk.OptionMenu(frame, semestre_var, "S1", "S2")
menu_semestre.pack()


lbl_transfert = tk.Label(frame, text="Transférer des crédits:")
lbl_transfert.pack()

entry_transfert = tk.Entry(frame, textvariable=transfert_var)
entry_transfert.pack()

lbl_transfert_formation = tk.Label(frame, text="Transférer à:")
lbl_transfert_formation.pack()

menu_transfert_formation = tk.OptionMenu(frame, transfert_var_formation, "Aucun", "Master DS", "ENSAE S1", "ENSAE S2")
menu_transfert_formation.pack()

# ajout de la matière
btn_ajouter_matiere = tk.Button(frame, text="Ajouter Matière", command=ajouter_matiere)
btn_ajouter_matiere.pack(pady=5)

# supprime une matière sélectionnée
btn_supprimer_matiere = tk.Button(frame, text="Supprimer Matière", command=supprimer_matiere)
btn_supprimer_matiere.pack(pady=5)

# cours séparés par formation et semestre
lbl_ects_master = tk.Label(frame, text=f"ECTS Master DS: {ects_master_ds}")
lbl_ects_master.pack()

liste_master_ds = tk.Listbox(frame, width=70, height=5)
liste_master_ds.pack(pady=5)

lbl_ects_ensae_s1 = tk.Label(frame, text=f"ECTS ENSAE S1: {ects_ensae_s1}")
lbl_ects_ensae_s1.pack()

liste_ensae_s1 = tk.Listbox(frame, width=70, height=5)
liste_ensae_s1.pack(pady=5)

lbl_ects_ensae_s2 = tk.Label(frame, text=f"ECTS ENSAE S2: {ects_ensae_s2}")
lbl_ects_ensae_s2.pack()

liste_ensae_s2 = tk.Listbox(frame, width=70, height=5)
liste_ensae_s2.pack(pady=5)

# Vérification de la validation
lbl_validation = tk.Label(frame, text="Validation Master DS: INSUFFISANTE")
lbl_validation.pack(pady=10)



# RUN
root.mainloop()
