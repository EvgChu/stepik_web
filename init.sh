echo "Start nginx"
sudo rm -rf /etc/nginx/sites-enabled/default
sudo cp -f etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

echo "Start MySql"
sudo /etc/init.d/mysql start
mysql -uroot -e "create database web;"
mysql -uroot -e "create user 'box'@'localhost' identified by '1234';"
mysql -uroot -e "grant all privileges on web.* to 'box'@'localhost' with grant option;"

cd ask
python3 manage.py makemigrations qa
python3 manage.py migrate
cd ..

echo "Start gunicorn" 
if [[ "$VIRTUAL_ENV" != "" ]]
then
    echo "VIRTUAL_ENV" 
    sudo ./venv/bin/gunicorn -c etc/conf_gunicorn_hello.py hello:simple_app &
    sudo ./venv/bin/gunicorn -c etc/conf_gunicorn_dj.py ask.wsgi:application &
else
    echo "not VIRTUAL_ENV" 
    sudo pip3 install django==2.0

    sudo gunicorn -c etc/conf_gunicorn_hello.py hello:simple_app &
    sudo gunicorn -c etc/conf_gunicorn_dj.py ask.wsgi:application &
fi

sudo /etc/init.d/mysql start



Wsleep 1
curl -vv 'http://127.0.0.1/'
curl -vv 'http://127.0.0.1/hello/?a=1&a=2&b=3'
curl -vv 'http://127.0.0.1:8080/?a=1&a=2&b=3'