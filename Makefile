DOCKER_NETWORK = docker-hadoop_default
ENV_FILE = hadoop.env
current_branch := ubuntu-20.04
build:
	docker build -t exclowd/hadoop-python-base:$(current_branch) --platform=linux/amd64 ./base
	docker build -t exclowd/hadoop-python-namenode:$(current_branch) --platform=linux/amd64 ./namenode
	docker build -t exclowd/hadoop-python-datanode:$(current_branch) --platform=linux/amd64 ./datanode
	docker build -t exclowd/hadoop-python-resourcemanager:$(current_branch) --platform=linux/amd64 ./resourcemanager
	docker build -t exclowd/hadoop-python-nodemanager:$(current_branch) --platform=linux/amd64 ./nodemanager
	docker build -t exclowd/hadoop-python-historyserver:$(current_branch) --platform=linux/amd64 ./historyserver
	docker build -t exclowd/hadoop-python-submit:$(current_branch) --platform=linux/amd64 ./submit

wordcount:
	docker build -t hadoop-wordcount ./submit
	docker run --network ${DOCKER_NETWORK} --env-file ${ENV_FILE} exclowd/hadoop-python-base:$(current_branch) hdfs dfs -mkdir -p /input/
	docker run --network ${DOCKER_NETWORK} --env-file ${ENV_FILE} exclowd/hadoop-python-base:$(current_branch) hdfs dfs -copyFromLocal -f /opt/hadoop-3.2.1/README.txt /input/
	docker run --network ${DOCKER_NETWORK} --env-file ${ENV_FILE} hadoop-wordcount
	docker run --network ${DOCKER_NETWORK} --env-file ${ENV_FILE} exclowd/hadoop-python-base:$(current_branch) hdfs dfs -cat /output/*
	docker run --network ${DOCKER_NETWORK} --env-file ${ENV_FILE} exclowd/hadoop-python-base:$(current_branch) hdfs dfs -rm -r /output
	docker run --network ${DOCKER_NETWORK} --env-file ${ENV_FILE} exclowd/hadoop-python-base:$(current_branch) hdfs dfs -rm -r /input
