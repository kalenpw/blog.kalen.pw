# React + Laravel + Nginx ###

This walks you through setting up Nginx to bridge separate React and Laravel applications. Working knowledge of both is assumed. If you need help learning React or Laravel plenty of good tutorials exist online.

## Project Structure
```bash
ExampleApp
│
├── backend
│   ├── app
│   ├── artisan
│   ├── bootstrap
│   ├── composer.json
│   ├── composer.lock
│   ├── config
│   ├── database
│   ├── package.json
│   ├── phpunit.xml
│   ├── public
│   │   ├── favicon.ico
│   │   ├── index.php
│   │   ├── robots.txt
│   │   └── web.config
│   ├── README.md
│   ├── resources
│   ├── routes
│   ├── server.php
│   ├── storage
│   ├── tests
│   ├── vendor
│   └── webpack.mix.js
├── frontend
│    ├── favicon.ico
│    ├── index.html
│    ├── logo192.png
│    ├── logo512.png
│    ├── manifest.json
│    └── robots.txt
```

Your directory structure likely looks slightly different as this hasn't been cleaned for production.

## Nginx Config
```nginx
server {
    # listen for http and https
    listen 80;
    listen 443 ssl;

    # for multiple web servers on same server
    server_name www.example.com example.com;

    # frontend
    location / {
        root /web/ExampleApp/Frontend;
        index index.html;
        try_files $uri /index.html;
    }

    # backend
    # assumes you've used api routes in Laravel
    location ^~ /api/ {
        root /web/ExampleApp/Backend/public;
        try_files $uri $uri/ /index.php?query_string;
    }

    # setup PHP
    location ~ \.php$ {
        root /web/ExampleApp/Backend/public;
        fastcgi_pass unix:/run/php/php7.2-fpm.sock;
        fastcgi_index index.php;
        fastcgi_param SCRIPT_FILENAME $realpath_root$fastcgi_script_name;
        include fastcgi_params;
    }

    error_page 404 /404.html;
}
```
with that setup requests that start with `/api` will be routed to your Laravel backend and other requests will be handled by the React application.