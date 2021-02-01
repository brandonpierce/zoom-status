#!/usr/bin/env bash

SERVER="localhost"

status=$(ps -ef | grep -i 'CptHost' | grep -v 'grep')

if [[ ${status} ]];
    then
        echo "in a meeting";
        curl -i -H "Content-Type: application/json" -X PUT -d '{"status":"online"}' "http://${SERVER}:5000/zoom"
    else
        echo "not in a meeting";
        curl -i -H "Content-Type: application/json" -X PUT -d '{"status":"offline"}' "http://${SERVER}:5000/zoom"
fi
