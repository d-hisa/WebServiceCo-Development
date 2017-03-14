# yasudample
## 概要
サンプルというか作るアプリの骨組みです。
## 使い方
wikiの **mariadbについて** を読み、既にmariadbの初期設定を完了している前提。
### リポジトリ準備準備
1. リポジトリをクローンする  
`git clone https://github.com/d-hisa/WebServiceCo-Development.git`
1. ディレクトリ移動  
`cd WebServiceCo-Development/yasudample/app`
1. GoogleDriveから`secret_settings.py`をDLし、`manage.py`と同じディレクトリに配置  
`GoogleDrive/06.開発用ファイル/secret_settings.py`
1. `secret_settings.py`の中身を必要に応じて書き換え  
特にDB_PW。これは自分の環境でmariadbのrootユーザに指定したパスワードを書く。

### mariadbセッティング
#### maridbを起動
```bash
[Mac]
$ mysql.server start
[Windows]
???
[CentOS]
$ systemctl start mysqld
```
#### mariadbへログイン
```bash
[Mac / CentOS]
$ mysql -uroot
[Windows]
???
```
#### DBを作成
```sql
> create database enzemi
```

### sampleセッティング
下記コマンドを実行
```bash
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py loaddata fixtures/default.json
```
### 動かす
```bash
$ python manage.py runserver
```

## 現状
- [朝夜メール画面]
	* 新規登録とタスクの表示（生JSON）
- [個人設定]
	* 個人設定の１つめのユーザの情報更新ができる（id=1をハードコーディングしている）
