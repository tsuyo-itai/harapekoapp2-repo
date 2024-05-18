# MongoDBの操作コマンドについて

## Docker環境のMongoDBへログイン

```bash
docker-compose exec db mongosh "mongodb://root:password@localhost:27017"
```

## コマンド

### データベース一覧

```bash
show dbs
```

### データベース選択

```bash
use [データベース名]
```

### コレクション一覧

```bash
show collections
```

### ドキュメント全件取得

```bash
db.[コレクション名].find()
```

### ドキュメント全件削除

```bash
db.[コレクション名].drop()
```

EC2のイメージは「Amazon Linux2 AMI (HVM) Kernel 5.10」のものを使用 (これより新しいバージョンだとmongoshのインストール時の依存関係に失敗する)

EC2へログイン後

```bash
echo -e "[mongodb-org-4.0] \nname=MongoDB Repository\nbaseurl=https://repo.mongodb.org/yum/amazon/2013.03/mongodb-org/4.0/x86_64/\ngpgcheck=1 \nenabled=1 \ngpgkey=https://www.mongodb.org/static/pgp/server-4.0.asc" | sudo tee /etc/yum.repos.d/mongodb-org-4.0.repo
```

```bash
sudo yum install -y mongodb-org-shell
```


```python
import pymongo
import sys

client = pymongo.MongoClient('mongodb://${DocDBMasterUsername}:${DocDBMasterUserPassword}@${DocDBCluster.Endpoint}:27017/?tls=true&tlsCAFile=global-bundle.pem&retryWrites=false')

##Specify the database to be used
db = client.sample_database

##Specify the collection to be used
col = db.sample_collection

##Insert a single document
col.insert_one({'hello':'Amazon DocumentDB'})

##Find the document that was previously written
x = col.find_one({'hello':'Amazon DocumentDB'})

##Print the result to the screen
print(x)

##Close the connection
client.close()
```