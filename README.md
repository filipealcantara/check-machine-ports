#Introduction 
This app is to check wether the ports 9200 are open in the elasticsearch clusters because we don't use X-PACK, so it's not
available to us the authentication on port 9200.

#Getting Started
###	Installation process

1. git clone https://harikenco.visualstudio.com/DefaultCollection/Hariken/_git/port-checker

2. */5 * * * * python /home/ubuntu/port-checker/app.py

###	Software dependencies
python 3