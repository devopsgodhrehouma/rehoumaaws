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
