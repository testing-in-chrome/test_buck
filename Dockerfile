FROM ubuntu:16.04

RUN apt-get update -y
RUN apt-get install software-properties-common autotools-dev -y
RUN add-apt-repository ppa:webupd8team/java -y
RUN echo debconf shared/accepted-oracle-license-v1-1 select true | \
    debconf-set-selections
RUN apt-get update && apt-get install -yq \
    ant \
    automake autoconf \
    build-essential \
    clang \
    git \
    python python-dev \
    pkg-config \
    oracle-java8-installer \
    oracle-java8-set-default \
    sudo
WORKDIR /home
RUN git clone https://github.com/facebook/watchman.git
WORKDIR /home/watchman
RUN git checkout v4.7.0
RUN ./autogen.sh && ./configure
RUN make && make install
WORKDIR /home
RUN git clone https://github.com/facebook/buck.git
WORKDIR /home/buck
RUN ant
WORKDIR /home
RUN git clone https://github.com/testing-in-chrome/test_buck.git