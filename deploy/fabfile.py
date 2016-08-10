from fabric.api import *

def john_install():
    #set host
    with settings(host_string='10.0.5.172'):
        run("hostname -f")
        sudo("wget https://raw.github.com/johnSerrano/airbnb_clone/master/deploy.sh")
        sudo("sh deploy.sh")
