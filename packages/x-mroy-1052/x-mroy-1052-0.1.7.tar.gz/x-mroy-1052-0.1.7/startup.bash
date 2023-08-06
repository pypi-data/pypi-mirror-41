#!/bin/bash

if [ !  -d /var/log/supervisord ];then
    mkdir /var/log/supervisord
fi

SUPER_CONF = /etc/supervisor/conf.d

if [ ! "$(which supervisord)" ];then
    echo -n "install supervisord ..."
    #pip3 install -U git+https://github.com/Supervisor/supervisor.git 1>/dev/null 2>/dev/null;
    apt install -y  supervisor 1>/dev/null 2>/dev/null
    echo  " ok"
fi


supervisorctl reread;
supervisorctl update;


if [ ! "$(ps aux | grep supervisord | grep -v grep | xargs )" ];then
    echo -n  "[+] Startup supervisord"
    # supervisord -c ~/.config/SwordNode/supervisord.conf
    service supervisor start
    if [ $? -eq 0 ];then 
        echo  " successful"
    else
        echo  " failed"
    fi
fi

reload() {
    echo -n "[+] update "
    supervisorctl reread;
    supervisorctl update;
    echo "ok"
}

start() {
    echo -n "[+] Start Server "
    supervisorctl start x-neid
    supervisorctl start x-auth
    supervisorctl start x-node-test
    echo " ok"
}

stop() {
    echo -n "[+] Stop Server "
    supervisorctl stop x-neid
    supervisorctl stop x-auth
    supervisorctl stop x-node-test
    echo " ok"
}

restart() {
    echo -n "[+] Restart Server "
    supervisorctl restart x-neid
    supervisorctl restart x-auth
    supervisorctl restart x-node-test
    echo " ok"
}

upgrade() {
    echo "[+] upgrade ..."
    pip3 install -U git+https://github.com/Qingluan/SwordNode.git 1>/dev/null 2>/dev/null;
    echo -n " ok"
}

if [[ $1 == "start" ]];then
    start
elif [[ $1 == "stop" ]];then
    stop
elif [[ $1 == "restart" ]];then
    restart
elif [[ $1 == "upgrade" ]];then
    upgrade
fi
