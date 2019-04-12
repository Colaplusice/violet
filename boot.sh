#!/usr/bin/env bash

function run() {
   source ./.env
   gunicorn -c gunicorn.py run:app
}

function deploy() {
    # note: this need to change your real path for project
     path="/home/ubuntu/flask_project/violet"
   if [ ! -d $path ]; then
   ssh  ubuntu@111.231.82.45 "git clone https://github.com/Colaplusice/violet $path"
   else
   ssh  ubuntu@111.231.82.45 "cd $path ; git pull"
   fi
   ssh  ubuntu@111.231.82.45 "cd $path ; /home/ubuntu/miniconda3/bin/docker-compose up -d --build"
   ssh  ubuntu@111.231.82.45 "cd $path ; git push github master"
}

function createdb() {
   mysql -u root -pnewpass -e "create database $1 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"
}

# import .sql to database
dump_sql(){
    if mysql -u$USER -p$PASS -h $HOST -P $PORT  $DB_NAME < "$2"
    then
        echo "success"
    else
        echo "failed，exit code is $?"
        exit $?
    fi
}

Action=$1
shift
 case "$Action" in
 run)
    run ;;
 deploy)
    deploy;;
 migrate)
 migrate;;
 createdb )
 createdb "$1";;
 dump_sql )
 dump_sql "$1";;
    *) echo 'usage: ./boot.sh command
     command:
     runserver:                  run
     update code and deploy:     deploy
     migrate data                migrate
     createdb                   createdb [dbname]
     dump_sql                   dump_sql [sql]
     ' ;;

esac
