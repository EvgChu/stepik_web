sudo rm -rf /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
# sudo ln -s /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
# sudo /etc/init.d/gunicorn restart
# sudo /etc/init.d/mysql start
sudo gunicorn --bind='0.0.0.0:8080' hello:simple_app &
curl -vv '127.0.0.1:8080/?a=1&a=2&b=3'
curl -vv '127.0.0.1:8080/?a=1&a=2&b=3'