#!/usr/bin/env bash
# 

exec {'http header':
command  => 'sudo apt update && 
             sudo apt -y install nginx && 
             c_header="\\\tadd_header X-Served-By \$hostname;\n" && 
             sudo sed -i "17i $c_header" /etc/nginx/nginx.conf && 
             sudo service nginx restart',
provider => shell,
}