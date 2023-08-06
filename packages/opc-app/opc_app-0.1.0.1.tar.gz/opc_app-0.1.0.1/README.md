# opc_http_gateway

This is a simple http gateway to fetch values from a kep server running on the
local machine.

with the current setup the windows machine can be accessed externally on the vpn at
```
http://10.100.0.199:5000
```
or if plugged into the router / on the same local network
```
http://192.168.10.3:5000
```

# pre-requisites

*make sure everything is 32-bit*

- make sure python 2.7 32-bit is installed

- make sure you winstall the latest binary for pywin32, make sure it is 32-bit as well

- then install OpenOPC, which is 32-bit so you don't have a choice

## how to use

### if you have a terminal emulator like git bash because you're not insane

go into the app directory ```~/Downloads/opchttpgateway/app```

install the requirements
```
pip install -r ../requirements.txt
```

source the env ( it is up from the app dir)
```
. ./env
```

run the flask app
```
. run.sh
```

that's it!

### if you're insane and are using powershell or cmd

download the repo on the windows machine that is running the OPC server.

install the requirements
```
pip install -r ../requirements.txt
```

go into the app directory ```~/Downloads/opchttpgateway/app``` and copy / paste the environment variables from the .env.ps1 file into the powershell prompt so that we have the neccessary stuff

now run the app
```
. run.sh
```

# notes

This will only run on windows as it uses the [OpenOPC](http://openopc.sourceforge.net/) library that makes calls only available on windows :disappointed:

most commands above are from the app directory which is inside opchttpgateway, but you'll figure it out. and if you can't you should stop whatever it is you're trying to do :wink:
