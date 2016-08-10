from fabric.api import *

def john_install():
    #set host
    with settings(host_string='10.0.5.210'):
        run("hostname -f")
        sudo("wget https://raw.githubusercontent.com/johnSerrano/airbnb_clone/master/deploy/deploy.sh")
        sudo("sh deploy.sh")
        sudo("rm deploy.sh")
