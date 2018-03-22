#!/bin/bash
#
#
#
# rafts_heartbeat.py mechanism
# setting it up to run as a system service (hopefully)
#
# /etc/rc.d/init.d/<servicename>
#
# <description of the service>
# <any general comments about this init script>
#
#
#!/bin/bash
#
# glassfish4    GlassFish Server Open Source Edition 4.0
#
# chkconfig: 345 70 30
# description: GlassFish Server is a Java EE Application Server Platform
# processname: glassfish4

# Source function library.
/etc/init.d/functions

RETVAL=0
#prog="glassfish4"
prog="rafts_heartbeat.py"
LOCKFILE=/var/lock/subsys/$prog

# Declare variables for GlassFish Server
#GLASSFISH_DIR=/home/gfish/glassfish4
progdir=/RAFTS/Dependencies/modules

start() {
        echo -n "Starting $prog: "
        #daemon --user $GLASSFISH_USER $ASADMIN start-domain $DOMAIN
        # it appears that this will work, just make sure that heartbeat 
        # only references absolute paths.
        # might want to include a set of installation type scripts
        # to allow it to install more cleanly.
        python3 /RAFTS/Dependencies/modules/rafts_heartbeat.py & 
        RETVAL=$?
        [ $RETVAL -eq 0 ] && touch $LOCKFILE
        echo
        return $RETVAL
}

stop() {
        echo -n "Shutting down $prog: "
        #$ASADMIN stop-domain domain1 && success || failure
        RETVAL=$?
        [ $RETVAL -eq 0 ] && rm -f $LOCKFILE
        echo
        return $RETVAL
}

status() {
        echo -n "Checking $prog status: "
        #$ASADMIN list-domains | grep $DOMAIN
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
    status)
        status
        ;;
    restart)
        stop
        start
        ;;
    *)
        echo "Usage: $prog {start|stop|status|restart}"
        exit 1
        ;;
esac
exit $RETVAL