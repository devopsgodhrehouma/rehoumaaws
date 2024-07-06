import boto3
import subprocess

# Initialiser une session boto3
session = boto3.Session()

# Initialiser le client S3
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

    # Lister tous les objets dans le bucket
    objects = s3_client.list_objects_v2(Bucket=bucket_name)

    if 'Contents' in objects:
        for obj in objects['Contents']:
            object_key = obj['Key']
            print(f"Setting public-read ACL for object: {object_key}")

            # Commande 3 : Définir l'ACL de chaque objet pour un accès public
            subprocess.run([
                "aws", "s3api", "put-object-acl",
                "--bucket", bucket_name,
                "--key", object_key,
                "--acl", "public-read"
            ])
