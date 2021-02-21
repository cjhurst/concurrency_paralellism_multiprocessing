FROM mysql:5.7

RUN apt-get update && apt-get install -y python3 python3-pip
RUN apt-get install htop

