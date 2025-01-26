# AWS Glue Job Integration Test

このプロジェクトは、AWS Glueジョブのローカル開発環境とテストを実行するための環境です。LocalStackを使用してS3をエミュレートし、AWS Glueの開発用コンテナを利用してGlueジョブをローカルで実行・テストすることができます。


## 必要なソフトウェア

- Docker 24.0.1
- Docker Compose 2.19.1
- Task 3.30.0

## セットアップ

1. リポジトリをクローン:
```bash
git clone https://github.com/mmocchi/glue-job-integration-test.git
cd glue-job-integration-test
```

2. 開発環境の起動:
```bash
task up
```

## ジョブの実行

```bash
task run-job
```

## テストの実行

以下のコマンドでテストを実行できます：

```bash
task test
```

## プロジェクト構成

```
.
├── data/              # 実行のためのデータ
├── src/               # ソースコード
│   └── glue_job.py   # Glueジョブの実装
├── tests/             # テストコード
├── compose.yml        # Docker Compose設定
└── Taskfile.yml       # タスク定義
```

