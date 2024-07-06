Oui, vous pouvez transformer ce script Python en script shell pour autoriser tous les accès sur tous les objets dans chaque bucket et récupérer les noms automatiquement. Voici un script shell pour ce faire :

```sh
#!/bin/bash

# Liste tous les buckets
buckets=$(aws s3api list-buckets --query 'Buckets[].Name' --output text)

for bucket_name in $buckets; do
    echo "Processing bucket: $bucket_name"

    # Définir les contrôles de propriété du bucket
    aws s3api put-bucket-ownership-controls \
        --bucket "$bucket_name" \
        --ownership-controls "Rules=[{ObjectOwnership=BucketOwnerPreferred}]"

    # Configurer le blocage d'accès public pour le bucket
    aws s3api put-public-access-block \
        --bucket "$bucket_name" \
        --public-access-block-configuration "BlockPublicAcls=false,IgnorePublicAcls=false,BlockPublicPolicy=false,RestrictPublicBuckets=false"

    # Lister tous les objets dans le bucket
    objects=$(aws s3api list-objects-v2 --bucket "$bucket_name" --query 'Contents[].Key' --output text)

    for object_key in $objects; do
        echo "Setting public-read ACL for object: $object_key"

        # Définir l'ACL de chaque objet pour un accès public
        aws s3api put-object-acl \
            --bucket "$bucket_name" \
            --key "$object_key" \
            --acl public-read
    done
done
```

### Explications

1. **Lister tous les buckets**:
    ```sh
    buckets=$(aws s3api list-buckets --query 'Buckets[].Name' --output text)
    ```

2. **Boucle à travers chaque bucket**:
    ```sh
    for bucket_name in $buckets; do
        ...
    done
    ```

3. **Définir les contrôles de propriété du bucket**:
    ```sh
    aws s3api put-bucket-ownership-controls \
        --bucket "$bucket_name" \
        --ownership-controls "Rules=[{ObjectOwnership=BucketOwnerPreferred}]"
    ```

4. **Configurer le blocage d'accès public pour le bucket**:
    ```sh
    aws s3api put-public-access-block \
        --bucket "$bucket_name" \
        --public-access-block-configuration "BlockPublicAcls=false,IgnorePublicAcls=false,BlockPublicPolicy=false,RestrictPublicBuckets=false"
    ```

5. **Lister tous les objets dans le bucket**:
    ```sh
    objects=$(aws s3api list-objects-v2 --bucket "$bucket_name" --query 'Contents[].Key' --output text)
    ```

6. **Boucle à travers chaque objet et définir l'ACL pour un accès public**:
    ```sh
    for object_key in $objects; do
        echo "Setting public-read ACL for object: $object_key"

        aws s3api put-object-acl \
            --bucket "$bucket_name" \
            --key "$object_key" \
            --acl public-read
    done
    ```

Enregistrez ce script dans un fichier, par exemple `make_all_public.sh`, puis rendez-le exécutable et exécutez-le :

```sh
chmod +x make_all_public.sh
./make_all_public.sh
```

Ce script shell parcourra tous vos buckets et rendra chaque objet public automatiquement.
