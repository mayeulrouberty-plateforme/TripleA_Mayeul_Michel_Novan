import psutil, time, os, collections, platform, socket
from pathlib import Path
from flask import Flask, render_template
chemin=Path("C:/Users/miche/Downloads")
hostname = socket.gethostname()

def adresse_ipv4():
    return socket.gethostbyname(hostname)

def adresse_ipv6():
    DnsIPAddr = socket.gethostbyaddr(hostname)
    return DnsIPAddr[2]

def nom_ordi():
    return psutil.users()[0].name

def nom_os():
    return platform.system()

def version_systeme():
    return platform.release()

def date_heure_actuelle():
    return time.strftime(f"%d-%m-%Y, il est %H:%M", time.localtime())

def date_heure_boot():
    return time.strftime("%d-%m-%Y à %H:%M", time.localtime(psutil.boot_time()))    

def nombre_utilisateur():
    return len(psutil.users())

def processeur_pourCent():
    psutil.cpu_percent()
    time.sleep(0.5)
    return psutil.cpu_percent()

def coeurs_processeur():
    return psutil.cpu_count()

def cpu_frequence():
    freq = psutil.cpu_freq().current
    return freq

def obtenir_couleur_proc(pourcentage):
    pourcentage = float(pourcentage)
    if pourcentage < 50:
        return "bar-green"
    elif pourcentage < 75:
        return "bar-orange"
    else:
        return "bar-red"

def RAM_totale():
    RAM_totale = psutil.virtual_memory().total
    result = "%.2f" % (RAM_totale/1000000000)
    return (result)

def RAM_utilisee():
    RAM_utilisee = psutil.virtual_memory().used
    result = "%.2f" % (RAM_utilisee/1000000000)
    return (result)

def RAM_pourcent():
    RAM_pourcent = psutil.virtual_memory().percent
    result="%.2f" % RAM_pourcent
    return (result)

def obtenir_couleur_ram(pourcentage):
    pourcentage = float(pourcentage)
    if pourcentage < 50:
        return "bar-green"
    elif pourcentage < 75:
        return "bar-orange"
    else:
        return "bar-red"

import psutil

def process_full():
    # On récupère le nombre de cœurs pour normaliser le pourcentage
    nb_coeurs = psutil.cpu_count()

    def get_top_processes(n=6):
        processes = []
        # On parcourt les processus
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
            p_info = proc.info

            # division du résultat par me nombre de coeurs
            if p_info['cpu_percent'] is not None:
                p_info['cpu_percent'] = p_info['cpu_percent'] / nb_coeurs

            processes.append(p_info)

        # Fonction de tri
        def get_cpu_percent(process):
            return process['cpu_percent']

        processes.sort(key=get_cpu_percent, reverse=True)
        return processes[:n]

    top_processes = get_top_processes(6)
    dict_processus = {}
    # On boucle de 1 à 6 pour créer les variables nom_1, nom_2, nom_3...
    for i in range(1, 7):
        if i <= len(top_processes):
            proc = top_processes[i-1]            
            dict_processus[f"nom_{i}"] = proc['name']
            dict_processus[f"pid_{i}"] = proc['pid']
            dict_processus[f"cpu_{i}"] = proc['cpu_percent']
    return dict_processus

def PDF_counter(): 
    PDFCounter = 0
    for root, dirs, files in os.walk(chemin):
        for file in files:    
            if file.endswith('.pdf'):
                PDFCounter += 1
        return PDFCounter

def TXT_counter():
    TXTCounter = 0
    for root, dirs, files in os.walk(chemin):
        for file in files:    
            if file.endswith('.txt'):
                TXTCounter += 1
        return TXTCounter

def PY_counter():
    PYCounter = 0
    for root, dirs, files in os.walk(chemin):
        for file in files:    
            if file.endswith('.py'):
                PYCounter += 1
        return PYCounter

def JPG_counter():
    JPGCounter = 0
    for root, dirs, files in os.walk(chemin):
        for file in files:    
            if file.endswith('.jpg'):
                JPGCounter += 1
        return JPGCounter

def statistiques_fichiers():
    # On utilise la variable 'chemin' définie en haut de votre fichier
    # Comme c'est déjà un objet Path, pas besoin de le convertir
    
    # 1. Récupérer tous les fichiers (ignore les dossiers)
    try:
        tous_les_fichiers = [f for f in chemin.iterdir() if f.is_file()]
    except FileNotFoundError:
        return 0, [] # Sécurité si le dossier n'existe pas

    total_fichiers = len(tous_les_fichiers)
    
    if total_fichiers == 0:
        return 0, []

    # 2. Compter les extensions
    extensions = [f.suffix.lower() for f in tous_les_fichiers] # .lower() pour éviter d'avoir .JPG et .jpg séparés
    compteur = collections.Counter(extensions)
    
    # 3. Préparer les données pour le HTML
    resultats = []
    
    for ext, quantite in compteur.items():
        pourcentage = (quantite / total_fichiers) * 100
        
        nom_ext = ext
        
        resultats.append({
            "extension": nom_ext,
            "quantite": quantite,
            "pourcentage": round(pourcentage, 2)
        })
    
    # Tri : les plus fréquents en premier
    resultats.sort(key=lambda x: x['quantite'], reverse=True)
    
    return total_fichiers, resultats

# def contenu_dossier_general():
#     extension_fichiers = [''.join(fichiers.suffix) for fichiers in chemin.iterdir()
#              if fichiers.is_file() and fichiers.suffix]
    
#     nombre_extensions = collections.Counter(extension_fichiers)
#     def pourcentage_fichiers():
#         for extension, count in nombre_extensions.items():
#             print(f"Il y a {count} fichier {extension} soit {100*count/contenu_dossier_fichier():.2f} % de la totalité des fichiers.")

def contenu_dossier_fichier():
    FileCounter = 0
    for root, dirs, files in os.walk(chemin):
            for _ in files:    
                FileCounter += 1
            return FileCounter
