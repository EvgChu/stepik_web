echo "Start nginx"
sudo rm -rf /etc/nginx/sites-enabled/default
sudo cp -f etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

echo "Start gunicorn" 
if [[ "$VIRTUAL_ENV" != "" ]]
then
    echo "VIRTUAL_ENV" 
    sudo ./venv/bin/gunicorn -c etc/conf_gunicorn_hello.py hello:simple_app &
    sudo ./venv/bin/gunicorn -c etc/conf_gunicorn_dj.py ask.wsgi:application &
else
    echo "not VIRTUAL_ENV" 
    sudo apt-get update
    sudo apt-get install -y python3.5
    sudo apt-get install -y python3.5-dev
    sudo unlink /usr/bin/python3
    sudo ln -s /usr/bin/python3.5 /usr/bin/python3
    sudo pip3 install --upgrade pip
    sudo pip3 install --upgrade django==2.1
    sudo pip3 install --upgrade gunicorn

    sudo gunicorn -c etc/conf_gunicorn_hello.py hello:simple_app &
    sudo gunicorn -c etc/conf_gunicorn_dj.py ask.wsgi:application &
fi


# sleep 1
# curl -vv 'http://127.0.0.1/'
# curl -vv 'http://127.0.0.1/hello/?a=1&a=2&b=3'
# curl -vv 'http://127.0.0.1:8080/?a=1&a=2&b=3'