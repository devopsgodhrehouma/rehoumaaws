 ```bash
git clone https://github.com/devopsgodhrehouma/rehoumaaws.git
cd rehoumaaws/
cd lab21/
python3 manage_s3_buckets.py
 ```

# Description


 ```bash
1. 00-script-du-lab-list_buckets.py

2. 01-commandes-du-lab.md

3. 02-tuto-commandes2-python-autoriser-all.md

4. 03-script-manage_s3_buckets_pour_all_universel.py

5. 03-script-manage_s3_buckets_pour_index.py

6. 04-script-manage_s3_buckets_pour_all_universel.sh

7. 04-tuto-commandes2-shell-autoriser-all.md
 ```
	


---

# AWS S3 Bucket Management Script

## Description

Ce script Python automatise la gestion des buckets S3 en exécutant les commandes AWS CLI suivantes pour chaque bucket :
1. Définir les contrôles de propriété du bucket.
2. Configurer le blocage d'accès public pour le bucket.
3. Définir l'ACL d'un objet pour un accès public.

## Prérequis

Avant d'utiliser ce script, assurez-vous d'avoir les éléments suivants installés et configurés sur votre machine :

1. **Python 3** - Vous pouvez télécharger et installer Python depuis [python.org](https://www.python.org/downloads/).
2. **AWS CLI** - Suivez les instructions d'installation sur [AWS CLI Installation Guide](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html).
3. **Boto3** - Installez la bibliothèque Boto3 en utilisant pip :
    ```bash
    pip install boto3
    ```
4. **Configurer AWS CLI** - Configurez votre AWS CLI avec vos identifiants AWS :
    ```bash
    aws configure
    ```
    Vous aurez besoin de votre `AWS Access Key ID`, `AWS Secret Access Key`, `Default region name`, et `Default output format`.

## Utilisation

1. **Cloner ce dépôt** :
    ```bash
    git clone <URL_DU_DEPOT>
    cd <NOM_DU_DEPOT>
    ```

2. **Créer un fichier Python** - Créez un fichier `manage_s3_buckets.py` et collez-y le script suivant :

    ```python
    import boto3
    import subprocess

    # Initialiser une session Boto3
    session = boto3.Session()

    # Créer un client S3
    s3_client = session.client('s3')

    # Lister tous les buckets
    buckets = s3_client.list_buckets()

    # Pour chaque bucket, exécuter les commandes AWS CLI
    for item in buckets['Buckets']:
        bucket_name = item['Name']
        print(f"Processing bucket: {bucket_name}")

        # Commande 1 : Définir les contrôles de propriété du bucket
        subprocess.run([
            "aws", "s3api", "put-bucket-ownership-controls",
            "--bucket", bucket_name,
            "--ownership-controls", "Rules=[{ObjectOwnership=BucketOwnerPreferred}]"
        ])

        # Commande 2 : Configurer le blocage d'accès public pour le bucket
        subprocess.run([
            "aws", "s3api", "put-public-access-block",
            "--bucket", bucket_name,
            "--public-access-block-configuration",
            "BlockPublicAcls=false,IgnorePublicAcls=false,BlockPublicPolicy=false,RestrictPublicBuckets=false"
        ])

        # Commande 3 : Définir l'ACL d'un objet pour un accès public
        # Remplacez 'index.html' par le nom de votre objet spécifique si nécessaire
        subprocess.run([
            "aws", "s3api", "put-object-acl",
            "--bucket", bucket_name,
            "--key", "index.html",
            "--acl", "public-read"
        ])
    ```

3. **Exécuter le script** - Dans le terminal, exécutez le script Python :
    ```bash
    python manage_s3_buckets.py
    ```

## Remarques

- Assurez-vous d'avoir les permissions nécessaires pour accéder et modifier les buckets S3 spécifiés.
- Modifiez le script selon vos besoins, par exemple, en changeant le nom de l'objet dans la commande `put-object-acl`.


