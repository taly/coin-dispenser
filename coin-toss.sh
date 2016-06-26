#! /bin/bash

PIDFILE=/var/run/coin-toss.pid

case $1 in
    start)
        echo $$ > ${PIDFILE};
        exec python /home/pi/coin-dispenser/main.py 2>/dev/null
    ;;
    stop)
        kill `cat ${PIDFILE}` ;;
    *)
esac
exit 0
