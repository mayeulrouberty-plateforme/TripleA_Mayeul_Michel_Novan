from fonctions import*
app = Flask(__name__)
@app.route('/')

def accueil():
    adresseIpv4=adresse_ipv4()
    adresseIpv6=adresse_ipv6()
    nombreUtilisateur=nombre_utilisateur()
    nomOrdi=nom_ordi()
    nomOs=nom_os()
    versionSysteme=version_systeme()
    dateHeureBoot=date_heure_boot()
    dateHeureActuelle=date_heure_actuelle()

    processeurPourCent=processeur_pourCent()
    processeurCoeur=coeurs_processeur()
    processeurFrequence=cpu_frequence()
    couleurProc=obtenir_couleur_proc(processeurPourCent)

    ramPourCent = RAM_pourcent()
    ramUtilisee = RAM_utilisee()
    ramTotale = RAM_totale()
    couleurRam = obtenir_couleur_ram(ramPourCent)
    
    processFull=process_full()

    pdfCounter=PDF_counter()
    txtCounter=TXT_counter()
    pyCounter=PY_counter()
    jpgCounter=JPG_counter()
    total, listeExtensions = statistiques_fichiers()

    return render_template('template.html', **process_full(),
                nombreUtilisateur=nombreUtilisateur,
                dateHeureBoot=dateHeureBoot,
                dateHeureActuelle=dateHeureActuelle,
                versionSysteme=versionSysteme,
                nomOrdi=nomOrdi,
                nomOs=nomOs,

                processeurPourCent=processeurPourCent,
                processeurCoeur=processeurCoeur,
                processeurFrequence=processeurFrequence,
                couleurProc=couleurProc,

                ramPourCent=ramPourCent,
                ramUtilisee=ramUtilisee,
                ramTotale=ramTotale,
                couleurRam=couleurRam,

                pdfCounter=pdfCounter,
                txtCounter=txtCounter,
                pyCounter=pyCounter,
                jpgCounter=jpgCounter,

                total=total,
                listeExtensions=listeExtensions,

                adresseIpv4=adresseIpv4,
                adresseIpv6=adresseIpv6
    )

if __name__ == "__main__":
    app.run(debug=True)
