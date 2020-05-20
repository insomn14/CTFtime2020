#!/bin/bash

while :
do
    su -c "exec socat TCP-LISTEN:20333,reuseaddr,fork EXEC:/pwn/0_give_away,stderr" - pwnuser;
done

