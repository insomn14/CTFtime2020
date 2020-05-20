#!/bin/bash

while :
do
    su -c "exec socat TCP-LISTEN:1337,reuseaddr,fork EXEC:'/home/insomn14/CTF101/CTFtime2020/28.sharkyCTF/Pwn/Give Away1/give_away_1',stderr" - insomn14;
done

