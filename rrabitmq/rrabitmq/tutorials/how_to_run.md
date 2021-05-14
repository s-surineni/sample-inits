* create network `docker network create rabbit-nw`
# start rabbit mq
*  `docker run --rm --network rabbit-nw  --hostname my-rabbit --name some-rabbit -p 5672:5672 -p 15672:15672 rabbitmq:3`
*  `docker run --rm --network rabbit-nw  --hostname my-rabbit --name some-rabbit -p 5672:5672 -p 15672:15672 rabbitmq:3-management`
# running python code
* build docker image
* run send.py with `docker run --rm --network rabbit-nw pyrab python send.py`
* hostname must mach in send.py and whatever is given while starting docker rabbitmq
* run receiver with `docker run --rm --network rabbit-nw pyrab python -u receive.py`
* access management endpoint at http://container-ip:15672/
* `docker run --rm --network rabbit-nw -v ${PWD}:/usr/src/app py3 python send.py`
