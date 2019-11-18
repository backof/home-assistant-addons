#!/bin/sh

APIURL=`jq -r .apiUrl /data/options.json`
APIKEY=`jq -r .apiKey /data/options.json`
HOST=`jq -r .host /data/options.json`
SHAREDSECRET=`jq -r .sharedSecret /data/options.json`
INTERVALMIN=`jq -r .intervalMinutes /data/options.json`

python3 updatedns.py APIURL APIKEY HOST SHAREDSECRET INTERVALMIN
