# DjangoTTS

使用說明

到`tts`目錄下，將 `.env.example` 更名為 `.env`

```shell
cd tts
mv .env.example .env
```

設定以下參數值

```python
MYSQL_ROOT_PASSWORD=
MYSQL_HOST=
MYSQL_DATABASE=
MYSQL_USER=
MYSQL_PASSWORD=
MYSQL_PORT=
SECRET_KEY=
```

到`tts_docker`目錄下，使用docker建立環境

```shell
cd tts_docker
docker compose up -d
```

成功的話可經由此連結查看

https://{your domain}/learn/
