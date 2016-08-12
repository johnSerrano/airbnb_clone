from fabric.api import *

def john_install():
    #set host
    with settings(host_string='192.168.2.118'):
        run("hostname -f")
        # sudo("wget https://raw.githubusercontent.com/johnSerrano/airbnb_clone/master/deploy/deploy.sh")
        put("deploy.sh")
        sudo("sh deploy.sh")
        sudo("rm deploy.sh")
