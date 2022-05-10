## My personal blog

Currently a work in progress, but can be found at <a href="https://blog.kalen.pw">blog.kalen.pw</a>

Simple Django + Alpine.js + Bootstrap


### Dev Environment

```
#macos prereqs
brew instal postgres
brew instal openssl
brew install gsl
# note you can find this with brew info openssl
export LDFLAGS="-L/opt/homebrew/opt/openssl@3/lib"
export CPPFLAGS="-I/opt/homebrew/opt/openssl@3/include"

# install Virtualenv
sudo pip3 install virtualenv

# create python3 venv, note: you may need to specify version
virtualenv venv -p python3
# virtualenv venv -p /opt/homebrew/opt/python@3.8/bin/python3

#activate venv
source venv/bin/active # or activate.fish
 
# install dependancies, note postgres must be install or psycopg2 will fail to install
pip install -r requirements.txt

cd kalenpw
cp example_secrets.json secrets.json
(then update secrets.json with postgres info)

./manage.py createsuperuser
./manage.py migrate
./manage.py runserver
 
```