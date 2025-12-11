# 📋 Mémo de Déploiement : Dashboard Triple A

### 1\. PRÉPARATION 

Avant de copier les fichiers, vérifie ces 3 points :

  * **[ ] Structure des dossiers :** Ne change rien à l'organisation standard.

    ```text
    /AAA/
     ├── app.py (ton script)
     ├── templates/ (tes fichiers .html)
     └── static/    (tes fichiers .css, .js, images)
    ```

  * **[ ] Chemins de fichiers (Paths) :**

      * **INTERDIT :** `C:\Users\Moi\Dossier`
      * **CORRECT :** Utiliser `pathlib` ou des chemins relatifs.

  * **[ ] Configuration du serveur (Si Flask/Web) :**
    Dans ton fichier Python, assure-toi que l'application écoute sur toutes les interfaces, pas juste en local :

    ```python
    # À la fin de ton fichier principal
    if __name__ == "__main__":
        app.run(host='0.0.0.0', port=5000) # 0.0.0.0 est CRUCIAL sur une VM
    ```
    
-----

### 2\. INSTALLATION (Sur la VM Ubuntu)

Une fois tes fichiers copiés dans le dossier `~/AAA` sur la VM :

**A. Mise à jour et pré-requis**

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3-pip python3-venv -y
```

**B. Configuration de l'environnement virtuel**
*Place-toi dans le dossier :*

```bash
cd ~/AAA
```

*Créer l'environnement isolé (nommé "venv") :*

```bash
python3 -m venv venv
```

*Activer l'environnement (A faire à chaque connexion \!) :*

```bash
source venv/bin/activate
```

*(Tu dois voir `(venv)` s'afficher au début de ta ligne de commande).*

**C. Installation des librairies**

```bash
pip install -r requirements.txt
```

*(Si tu n'as pas de fichier requirements.txt, installe manuellement, ex: `pip install flask pandas`)*.

-----

### 3\. LANCEMENT

**A. Ouvrir le port (Pare-feu)**
Autorise le trafic sur le port de ton application (ex: 5000) :

```bash
sudo ufw allow 5000
```

**B. Démarrer le script**
Assure-toi que `(venv)` est bien activé, puis :

```bash
python3 ton_fichier_principal.py
```

**C. Tester**
Sur ton navigateur Windows, tape l'adresse IP de ta VM suivie du port :
`http://192.168.X.X:5000`

-----

### 💡 Astuce de dépannage

Si tu as une erreur "File not found" (Fichier introuvable) alors que le fichier est bien là, c'est souvent un problème de **casse** (Majuscule/Minuscule).

  * Windows s'en fiche (`Logo.png` = `logo.png`).
  * Linux est strict (`Logo.png` n'est PAS `logo.png`).
    **Vérifie tes noms de fichiers et tes imports \!**

-----
