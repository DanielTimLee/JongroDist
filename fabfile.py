from fabric.api import *

# add SSH Config at Local Host File
env.use_ssh_config = True
env.activate = 'source venv/bin/activate && source .env'

drop_database = '"drop database smtm_oauth;drop database smtm_application;"'
create_database = '"create database smtm_application;create database smtm_oauth;"'

def install():
    run('rm -rf JongroDist')
    run('git clone https://github.com/DanielTimLee/JongroDist')
    with cd('~/JongroDist/'):
        run('virtualenv --python=python3 venv')
        run('mysql -uroot -p -e ' + drop_database)
        run('mysql -uroot -p -e ' + create_database)
        with prefix(env.activate):
            run('pip install -r requirements.txt')
            run('bower install --allow-root')
            run('python server.py')


def deploy():
    with cd('~/JongroDist/'):
        run('git checkout master')
        run('git pull origin master')
        with prefix(env.activate):
            run('pip install -r requirements.txt')
            run('bower install --allow-root')


def register_upstart():
    sudo('rm -f /etc/init/jongrodist.service')
    sudo('ln -s /home/ubuntu/jongrodist/jongrodist.upstart.service /etc/init/jongrodist.upstart')
    sudo('initctl reload-configuration')


def start():
    sudo('initctl start jongrodist.upstart')


def stop():
    sudo('initctl stop jongrodist.upstart')


def status():
    sudo('initctl status jongrodist.upstart')


def proxy_start():
    sudo('service nginx start')


def proxy_stop():
    sudo('service nginx stop')
