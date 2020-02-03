# Overview
This project is simply to test out and see how to make my docker daemon listen to a docker process and execute another docker container
What will be contained in this project is an api (as a docker container) that will be able to communicate with the docker daemon
to spin up a docker process whenever one of its endpoints is reached.

## Getting Started
Start the virtual environment by running the command

$ source venv/bin/activate

## Using volumes
I created a couple of sample programs (reader and writer) with the intention of learning to use volumes.

Construct a volume with the name dockerception
$ docker volume create dockerception 

Build the writer
$ cd writer
$ docker build -t writer .

Build the reader
$ cd reader
$ docker build -t reader .

Run the writer
$ docker run -it -v dockerception:/data writer

Note: What the -v flag does is mount the volume "dockerception" at the location /data in your docker image
From what I understand, the mounted location of your volume should be different from your working directory,
otherwise your working directory will be replaced with what is in your volume. If your volume is empty, then
your new working directory will be empty as well

Run the reader
$ docker run -it -v dockerception:/data reader

## Running docker in docker
This is actually rather simple. In the docker image you have, you will require it to have docker installed. 
If you're using alpine, you can simply include this line in your Dockerfile

$ apk add docker

With that line, we have docker now installed in the image, and we can run the container with the following command

$ docker run -v /var/run/docker.sock:/var/run/docker.sock -it <image_name>

Doing this will run the docker container with the dockerd daemon (from the host) attached onto it. Thus, whenever
you run any docker command inside of said container, you will see exactly what is seen when you run docker from outside
of the container. If you run something like "docker ps" in the container, the container itself should pop up.


