# Partie 0

```bash
aws s3api put-bucket-ownership-controls --bucket c84968a181123514814882tlw66503827742-samplebucket-ywp0aj41j5eo --ownership-controls 'Rules=[{ObjectOwnership=BucketOwnerPreferred}]'

aws s3api put-public-access-block --bucket <bucket-name> --public-access-block-configuration "BlockPublicAcls=false,IgnorePublicAcls=false,BlockPublicPolicy=false,RestrictPublicBuckets=false"

aws s3api put-object-acl --bucket <bucket-name> --key index.html --acl public-read

```

# Partie 1

- Voici toutes les commandes shell  :

```bash
aws --version
```

```bash
aws s3 ls
```

```bash
cat list-buckets.py
```

```bash
python3 list-buckets.py
```

```bash
aws s3 cp list-buckets.py s3://<bucket-name>
```

```bash
df -H /home
```

```bash
aws s3 ls
```

```bash
aws s3 cp s3://<bucket-name>/list-buckets.py .
```

```bash
sudo pip3 install boto3
```

```bash
aws s3api put-bucket-ownership-controls --bucket c84968a181123514814882tlw66503827742-samplebucket-ywp0aj41j5eo --ownership-controls 'Rules=[{ObjectOwnership=BucketOwnerPreferred}]'
```

```bash
aws s3api put-public-access-block --bucket <bucket-name> --public-access-block-configuration "BlockPublicAcls=false,IgnorePublicAcls=false,BlockPublicPolicy=false,RestrictPublicBuckets=false"
```

```bash
aws s3api put-object-acl --bucket <bucket-name> --key index.html --acl public-read
```

# Partie 2
### Commandes Shell AWS Concises

1. **Afficher la version d'AWS CLI :**
   ```bash
   aws --version
   ```
   - Affiche la version actuelle de l'AWS CLI installée.

2. **Lister les buckets S3 :**
   ```bash
   aws s3 ls
   ```
   - Liste tous les buckets S3 dans le compte AWS.

3. **Afficher le contenu du fichier `list-buckets.py` :**
   ```bash
   cat list-buckets.py
   ```
   - Affiche le contenu du fichier `list-buckets.py` dans le terminal.

4. **Exécuter le script Python `list-buckets.py` :**
   ```bash
   python3 list-buckets.py
   ```
   - Exécute le script Python `list-buckets.py` avec Python 3.

5. **Copier un fichier dans un bucket S3 :**
   ```bash
   aws s3 cp list-buckets.py s3://<bucket-name>
   ```
   - Copie le fichier `list-buckets.py` dans le bucket S3 spécifié.

6. **Afficher l'espace disque disponible dans CloudShell :**
   ```bash
   df -H /home
   ```
   - Affiche la quantité de stockage disponible dans le répertoire `/home`.

7. **Copier un fichier depuis un bucket S3 :**
   ```bash
   aws s3 cp s3://<bucket-name>/list-buckets.py .
   ```
   - Copie le fichier `list-buckets.py` depuis le bucket S3 spécifié vers le répertoire actuel.

8. **Installer la bibliothèque Boto3 avec pip :**
   ```bash
   sudo pip3 install boto3
   ```
   - Installe la bibliothèque Boto3 pour interagir avec les services AWS via Python.

9. **Définir les contrôles de propriété du bucket :**
   ```bash
   aws s3api put-bucket-ownership-controls --bucket c84968a181123514814882tlw66503827742-samplebucket-ywp0aj41j5eo --ownership-controls 'Rules=[{ObjectOwnership=BucketOwnerPreferred}]'
   ```
   - Configure le bucket S3 pour que le propriétaire du bucket devienne propriétaire des objets chargés.

10. **Configurer le blocage d'accès public pour un bucket :**
    ```bash
    aws s3api put-public-access-block --bucket <bucket-name> --public-access-block-configuration "BlockPublicAcls=false,IgnorePublicAcls=false,BlockPublicPolicy=false,RestrictPublicBuckets=false"
    ```
    - Configure les paramètres de blocage d'accès public pour le bucket S3 spécifié.

11. **Définir l'ACL d'un objet pour un accès public :**
    ```bash
    aws s3api put-object-acl --bucket <bucket-name> --key index.html --acl public-read
    ```
    - Rend l'objet `index.html` dans le bucket S3 spécifié publiquement accessible en lecture.

# Partie 3
# Commande 1
- aws s3api put-bucket-ownership-controls --bucket c84968a181123514814882tlw66503827742-samplebucket-ywp0aj41j5eo --ownership-controls 'Rules=[{ObjectOwnership=BucketOwnerPreferred}]'
# Commande 2
- aws s3api put-public-access-block --bucket c84968a181123514814882tlw66503827742-samplebucket-ywp0aj41j5eo --public-access-block-configuration "BlockPublicAcls=false,IgnorePublicAcls=false,BlockPublicPolicy=false,RestrictPublicBuckets=false"
# Commande 3
- aws s3api put-object-acl --bucket c84968a181123514814882tlw66503827742-samplebucket-ywp0aj41j5eo --key index.html --acl public-read


### Commande 1 : Définir les contrôles de propriété du bucket

```bash
aws s3api put-bucket-ownership-controls --bucket c84968a181123514814882tlw66503827742-samplebucket-ywp0aj41j5eo --ownership-controls 'Rules=[{ObjectOwnership=BucketOwnerPreferred}]'
```

**Explication détaillée :**

Cette commande configure les contrôles de propriété du bucket pour un bucket S3 spécifique. Voici une explication détaillée des éléments de la commande :

- `aws s3api`: Cette commande utilise l'interface de ligne de commande AWS S3 API.
- `put-bucket-ownership-controls`: Cette opération spécifie les contrôles de propriété du bucket.
- `--bucket c84968a181123514814882tlw66503827742-samplebucket-ywp0aj41j5eo`: Le paramètre `--bucket` spécifie le nom du bucket S3 auquel s'appliquent les contrôles de propriété.
- `--ownership-controls 'Rules=[{ObjectOwnership=BucketOwnerPreferred}]'`: Le paramètre `--ownership-controls` définit les règles de propriété du bucket. Ici, la règle `ObjectOwnership=BucketOwnerPreferred` signifie que le propriétaire du bucket devient propriétaire des objets chargés.

**Résumé :** Cette commande configure le bucket spécifié pour que tous les objets chargés dans ce bucket soient possédés par le propriétaire du bucket, même si l'objet est téléchargé par un autre compte AWS.

---

### Commande 2 : Définir la configuration de blocage d'accès public

```bash
aws s3api put-public-access-block --bucket c84968a181123514814882tlw66503827742-samplebucket-ywp0aj41j5eo --public-access-block-configuration "BlockPublicAcls=false,IgnorePublicAcls=false,BlockPublicPolicy=false,RestrictPublicBuckets=false"
```

**Explication détaillée :**

Cette commande configure les paramètres de blocage d'accès public pour un bucket S3 spécifique. Voici une explication détaillée des éléments de la commande :

- `aws s3api`: Cette commande utilise l'interface de ligne de commande AWS S3 API.
- `put-public-access-block`: Cette opération spécifie la configuration de blocage d'accès public du bucket.
- `--bucket c84968a181123514814882tlw66503827742-samplebucket-ywp0aj41j5eo`: Le paramètre `--bucket` spécifie le nom du bucket S3 auquel s'appliquent les paramètres de blocage d'accès public.
- `--public-access-block-configuration "BlockPublicAcls=false,IgnorePublicAcls=false,BlockPublicPolicy=false,RestrictPublicBuckets=false"`: Ce paramètre définit les différentes options de blocage d'accès public. Les paramètres spécifiés ici sont :
  - `BlockPublicAcls=false`: Ne bloque pas les ACL publiques.
  - `IgnorePublicAcls=false`: Ne permet pas d'ignorer les ACL publiques.
  - `BlockPublicPolicy=false`: Ne bloque pas les politiques publiques.
  - `RestrictPublicBuckets=false`: Ne restreint pas les buckets publics.

**Résumé :** Cette commande configure le bucket spécifié pour qu'il n'ait aucune restriction sur les ACL publiques, les politiques publiques ou les buckets publics.

---

### Commande 3 : Définir l'ACL d'un objet pour un accès public

```bash
aws s3api put-object-acl --bucket c84968a181123514814882tlw66503827742-samplebucket-ywp0aj41j5eo --key index.html --acl public-read
```

**Explication détaillée :**

Cette commande configure la liste de contrôle d'accès (ACL) d'un objet dans un bucket S3 pour qu'il soit accessible publiquement en lecture. Voici une explication détaillée des éléments de la commande :

- `aws s3api`: Cette commande utilise l'interface de ligne de commande AWS S3 API.
- `put-object-acl`: Cette opération spécifie la configuration de l'ACL d'un objet.
- `--bucket c84968a181123514814882tlw66503827742-samplebucket-ywp0aj41j5eo`: Le paramètre `--bucket` spécifie le nom du bucket S3 contenant l'objet.
- `--key index.html`: Le paramètre `--key` spécifie le nom de l'objet pour lequel l'ACL est définie.
- `--acl public-read`: Le paramètre `--acl` définit l'ACL à `public-read`, ce qui signifie que l'objet est accessible en lecture par quiconque.

**Résumé :** Cette commande rend l'objet `index.html` du bucket spécifié publiquement accessible en lecture.

---

Ces commandes configurent diverses propriétés et accès pour un bucket S3 et ses objets. Elles permettent de gérer la propriété des objets, de définir les règles de blocage d'accès public et de configurer l'accès public pour des objets spécifiques.
