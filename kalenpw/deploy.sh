#!/bin/bash

serverDir="/web/blog.kalen.pw"

cd ~/blog.kalen.pw
git pull origin master

rsync -r ~/blog.kalen.pw/ "$serverDir" --delete

cd $serverDir

rm "$serverDir/kalenpw/settings.py"
mv "$serverDir/kalenpw/settings_prod.py" "$serverDir/kalenpw/settings.py"

rm -rf "$serverDir/venv"
virtualenv venv -p python3
source /web/blog.kalen.pw/venv/bin/activate
pip install -r requirements.txt
pip install gunicorn

./manage.py collectstatic

sudo mv /home/kalenpw/Secrets/blog.kalen.pw_secrets.json /web/blog.kalen.pw/kalenpw/secrets_prod.json

# kill old gunicorn
pkill -f gunicorn

gunicorn --daemon --workers 3 --bind unix:/web/blog.kalen.pw/kalenpw.sock kalenpw.wsgi
