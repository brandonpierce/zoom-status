#!/usr/bin/env bash

status=$(ps -ef | grep -i 'CptHost15980' | grep -v 'grep')

if [[ ${status} ]];
    then
        echo "in a meeting";
    else
        echo "not in a meeting";
fi
