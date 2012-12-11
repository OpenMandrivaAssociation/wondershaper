#!/bin/sh
#
# chkconfig: 2345 80 20
# description: Helps maintain interactive latency on modem/ADSL/cable

# Source function library.
. /etc/rc.d/init.d/functions

#wondershaper="/usr/sbin/wshaper"
wondershaper="/usr/sbin/wshaper.htb"

name="Wonder Shaper"

RETVAL=0

start() {
    gprintf "Starting %s: " "$name"
    "$wondershaper" start
    RETVAL=$?
    [ $RETVAL == 0 ] && success "stop" || failure "stop"
    echo
    return $RETVAL
}

stop() {
    gprintf "Stopping %s: " "$name"
    "$wondershaper" stop
    RETVAL=$?
    [ $RETVAL == 0 ] && success "stop" || failure "stop"
    echo
    return $RETVAL
}

status() {
    "$wondershaper" status
    RETVAL=$?
    return $RETVAL
}

case "$1" in
        start)
            start
            ;;

        stop)
            stop
            ;;

        restart)
            stop
            start
            ;;

        status)
            status
            ;;

        *)
            gprintf "Usage: %s {start|stop|restart|status}\n" "$0"
            exit 1

esac

exit $REVAL
