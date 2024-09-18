#!/bin/bash
# nc為netcat縮寫，這邊是在等待MySQL容器啟動
while ! nc -z db 3306 ; do
    echo "Waiting for the MySQL Server"
    sleep 3
done

# 取得靜態檔案放到static目錄下
python manage.py collectstatic --noinput&&
# 資料庫遷移
python manage.py makemigrations&&
python manage.py migrate&&
# 使用uwsgi來啟動django
uwsgi --ini /var/www/html/tts/uwsgi.ini&&
# 防止web容器退出
tail -f /dev/null

exec "$@"