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
