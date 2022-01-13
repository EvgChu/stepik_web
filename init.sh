echo "Start nginx"
sudo rm -rf /etc/nginx/sites-enabled/default
sudo cp -f etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
printenv VIRTUAL_ENV
echo "Start gunicorn" 
sudo ./venv/bin/gunicorn -c conf_gunicorn_hello.py hello:simple_app &

sleep 1
curl -vv 'http://127.0.0.1/'
curl -vv 'http://127.0.0.1/hello/?a=1&a=2&b=3'
curl -vv 'http://127.0.0.1:8080/?a=1&a=2&b=3'