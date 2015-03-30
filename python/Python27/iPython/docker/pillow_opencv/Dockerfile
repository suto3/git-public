FROM ubuntu:14.04

MAINTAINER suto3 <suto3suto3@gmail.com>

ENV DEBIAN_FRONTEND noninteractive

# Not essential, but wise to set the lang
# Note: Users with other languages should set this in their derivative image
RUN apt-get update && apt-get install -y language-pack-en language-pack-ja
ENV LANGUAGE en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8

RUN locale-gen en_US.UTF-8
RUN dpkg-reconfigure locales

# Python binary dependencies, developer tools
RUN apt-get update && apt-get install -y -q \
    build-essential \
    make \
    gcc \
    gfortran \
    libfreetype6-dev \
    libxft-dev \
    libopenblas-dev \
    liblapack-dev \
    libzmq-dev \
    libcurl4-openssl-dev \
    zlib1g-dev \
    git \
    python \
    python-dev \
    python-pip \
    python-sphinx \
    python-mock \
    python-nose \
    python-jinja2 \
    python-tornado \
    python-zmq \
    python-numpy \
    python-matplotlib \
    python-pandas \
    python-scipy \
    python-jsonschema \
    python-requests \
    python-pygments \
    python-pymongo \
    sqlite3 \
    libsqlite3-dev \
    pandoc \
    libopencv-dev \
    python-opencv \
    nodejs \
    nodejs-legacy \
    npm \
    fonts-takao \
    fonts-ipafont \
    curl


RUN apt-get clean

# In order to build from source, need less
RUN npm install -g 'less@<3.0'

RUN pip install invoke
RUN pip install --upgrade \
    pillow \
    mock \
    nose \
    jinja2 \
    tornado \
    pyzmq \
    numpy \
    matplotlib \
    pandas \
    scipy \
    jsonschema \
    requests \
    mistune \
    pygments \
    pymongo \
    patsy \
    statsmodels \
    scikit-learn \
    ggplot \
    networkx \
    bokeh \
    sphinx \
    ipython

RUN iptest2

ENV HOME /root
RUN ipython profile create nbserver

# Install handy extension(s).
RUN ipython -c "%install_ext http://raw.github.com/jrjohansson/version_information/master/version_information.py"

# Configure "nbserver" profile
RUN sed -i \
        -e "s/^# c.NotebookApp.ip = 'localhost'$/c.NotebookApp.ip = '0.0.0.0'/" \
        -e "s/^# c.NotebookApp.port = 8888$/c.NotebookApp.port = 8888/" \
        -e "s;^# c.NotebookApp.notebook_dir = '/.*'$;c.NotebookApp.notebook_dir = '/notebook';" \
        -e "s/^# c.NotebookApp.open_browser = True$/c.NotebookApp.open_browser = False/" \
        -e "s/^# c.IPKernelApp.matplotlib = None$/c.IPKernelApp.matplotlib = 'inline'/" \
        -e "s/^# c.IPKernelApp.extensions = \[\]$/c.IPKernelApp.extensions = ['version_information']/" \
        /root/.ipython/profile_nbserver/ipython_notebook_config.py

# For IPython Notebook to share resources with other containers.
EXPOSE 8888
VOLUME ["/notebook"]

ENV LANG ja_JP.UTF-8
WORKDIR /notebook
# Use shell form to work with notebook.
CMD ipython notebook --profile=nbserver


