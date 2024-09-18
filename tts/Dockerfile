FROM python:3.10

# 安裝netcat-traditional，用來確認其他container啟動狀態
RUN apt-get update && apt install -y netcat-traditional

MAINTAINER Luke Liao

# python環境變數
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# container 中建立專案目錄(這邊專案名稱為tts)，並將其設置為WORKDIR
ENV APP_HOME=/var/www/html/tts
RUN mkdir -p $APP_HOME
WORKDIR $APP_HOME

# 將當前目錄內的資料複製到容器內
ADD . $APP_HOME

# pip更新版本
RUN /usr/local/bin/python -m pip install --upgrade pip

# 安裝所需套件
RUN pip install -r requirements.txt

# start.sh 需要移除 windows 文件格式的\r換行，linux下才可正常執行
RUN sed -i 's/\r//' ./start.sh

# 增加執行權限
RUN chmod +x ./start.sh

# 啟動指令(包含資料庫初始化和wsgi啟動)
ENTRYPOINT /bin/bash ./start.sh