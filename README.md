# owlvey_sre
owlvey_sre



## dependencies 

### mysql docker
docker pull mysql:8.0
docker network create --driver bridge sre-net
docker run --name sre-mysql -p 3306:3306 --network sre-net -e MYSQL_ROOT_PASSWORD=p@ssw0rd -d mysql:8.0
docker start instanceid

docker ps 

### api flask
pip3 install -r requirements.txt 


