# Vite環境 React

## 環境構築

```bash
npm create vite
```

以下のように選択

```text
Need to install the following packages:
create-vite@5.1.0
Ok to proceed? (y) y
✔ Project name: … viteapp
✔ Select a framework: › React
✔ Select a variant: › TypeScript

Scaffolding project in /Users/itaitsuyoshi/home/develop/vite-fastapi/viteapp...

Done. Now run:

  cd viteapp
  npm install
  npm run dev
```

その後立ち上げは

```bash
cd viteapp
npm install
npm run dev
```

## Docker環境構築手順

`docker-compose.yml`と同階層で実行する

### ビルド

```bash
docker-compose build

# キャシュを使用せずビルド (本番前環境作成時など)
docker-compose build --no-cache
```

### 起動

```bash
docker-compose up

# バックグラウンド起動
docker-compose up -d
```

### DBのマイグレーション

Docker環境内で

```bash
cd db
alembic upgrade head
```

ちなみにマイグレートファイルの構築

```bash
cd db
alembic init migrations
# マイグレーションファイルの作成 (DBの更新のたびにこれが必要)
alembic revision --autogenerate -m 'comments'
```

#### マイグレーションがうまく行かない場合

以下のようなエラーの場合

```text
INFO  [alembic.runtime.migration] Context impl MySQLImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
ERROR [alembic.util.messaging] Can't locate revision identified by 'cdc08cfd19de'
  FAILED: Can't locate revision identified by 'cdc08cfd19de'
```

mysql内の`alembic_version`テーブルが原因→ 削除してみる

[http://localhost:8000/](http://localhost:8000/)で環境へアクセス可能

#### APIのテスト実行
APIのテストおよび実行はSwagger上で行う

[http://localhost:8000/docs](http://localhost:8000/docs)でAPI仕様書(SwaggerUI)へ  
(ここからAPI実行可能)

他にもredocでAPI仕様の確認もできる

[http://localhost:8000/redoc](http://localhost:8000/redoc)

#### vite環境を立ち上げる場合

事前にローカルの環境で`npm install`を行っておくか以下のコマンドでdocker環境内に`npm install`を反映させておく

```bash
docker-compose exec frontend npm install
```

viteの起動

```bash
docker-compose exec frontend npm run dev
```

[http://localhost:5173/](http://localhost:5173/)でvite環境へアクセス可能


### コンテナ環境へのログイン

コンテナ環境内に入る必要があれば

```bash
# python(fastapi)環境
docker-compose exec webapi /bin/bash

# vue(vite)環境
docker-compose exec frontend /bin/bash

```

## API設計ポリシー

### ディレクトリ階層と役割

```text
fastapiapp
├── routers // API階層管理
│   └── route_xxx.py // API階層ごとに作成
├── schemas // モデル管理
│   └── xxx.py // モデルごとに管理
├── database.py // データベース設定管理
└── main.py // エントリーポイント
```