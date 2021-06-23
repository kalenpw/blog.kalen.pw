#!/bin/bash

# puts all css and js into one file

jsSource=""
cssSource=""

jsDest=""
cssDest=""

if [ "$1" == "django" ]; then
    jsSource="./static/js"
    cssSource="./static/css"
    jsDest="./static/js/app.js"
    cssDest="./static/css/app.css"
else 
    exit 1
fi

date=$(date +"%Y-%m-%d %T")

echo "Don't forget to run from project root"

echo "Erasing app.js"

echo "// Generated $date" > $jsDest

for file in $jsSource/*
do
    cat $file >> $jsDest
    echo '' >> $jsDest
done

