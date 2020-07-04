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

# kill old gunicorn
ps ax|grep -m 1 gunicorn|awk {'print $1'} | xargs kill -9

gunicorn --daemon --workers 3 --bind unix:/web/blog.kalen.pw/kalenpw.sock kalenpw.wsgi
