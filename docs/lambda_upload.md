# バックエンドインフラ構成
AWS API gateway + lambda + DocumentDB

# デプロイ

## デプロイ準備 (S3へコードをアップロード)
srcのzip化 `infra/s3_upload.sh`を使用

```bash
bash s3_upload.sh
```

ただし、上記ではzipファイルの作成のみに留められるので、S3へのアップロードは別途行う(GUI or CLIコマンド)

また、第1引数にS3のバケット名を指定するとS3バケットの作成&アップロードを行います  
(ただし`aws-cli`の認証情報を事前に設定しておく)

```bash
bash s3_upload.sh <s3-bucket-name>
```
### その他S3操作コマンドメモ

バケットを空にする場合

```bash
aws s3 rm s3://<s3-bucket-name> --recursive
```

バケットを削除する場合

```bash
aws s3 rb s3://<s3-bucket-name>
```

## cloudformation
インフラの構成はcloudformationを使用する

バックエンドを構築する際は`backend_template.yaml`を使用してAWS Cloudformationから構築を行う  
(事前に上記S3へコードをアップロードしておき、CFNのテンプレートパラメータからS３バケットを指定する)