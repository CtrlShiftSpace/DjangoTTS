FROM nginx:latest

# 刪除原有default.conf，並建立存放靜態檔案與ssl資料夾
RUN rm /etc/nginx/conf.d/default.conf \
&& mkdir -p /usr/share/nginx/html/mysite/static \
&& mkdir -p /usr/share/nginx/html/mysite/media \
&& mkdir -p /usr/share/nginx/ssl

# Media 目錄為可讀可寫，且權限為 775 與 www-data 才可正常顯示
RUN chown -R www-data:www-data /usr/share/nginx/html/mysite/static \
&& chmod -R 775 /usr/share/nginx/html/mysite/media

# 添加配置文件
ADD ./nginx.conf /etc/nginx/conf.d/

# 為了在容器中正常執行，需要保持 daemon off;
CMD ["nginx", "-g", "daemon off;"]