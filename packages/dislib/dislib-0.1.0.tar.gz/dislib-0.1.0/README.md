<h1 align="center">
  <br>
  <a href="https://www.bsc.es/">
    <img src="docs/bsc_logo.png" alt="Barcelona Supercomputing Center" height="60px">
  </a>
  <br>
  <br>
  The Distributed Computing Library
  <br>
</h1>

<h3 align="center">Distributed computing library implemented over PyCOMPSs programming model for HPC.</h3>

<p align="center">
  <a href="https://dislib.readthedocs.io/en/latest/?badge=latest">
    <img src="https://readthedocs.org/projects/dislib/badge/?version=latest"
         alt="Documentation Status"/>
  </a>
  <a href="https://github.com/bsc-wdc/dislib/releases">
    <img src="https://badge.fury.io/gh/bsc-wdc%2Fdislib.svg"
         alt="GitHub version">
  </a>
  <a href="https://travis-ci.org/bsc-wdc/dislib">
    <img src="https://travis-ci.org/bsc-wdc/dislib.svg?branch=master"
         alt="Build Status">
  </a> 
  <a href="https://codecov.io/gh/bsc-wdc/dislib">
    <img src="https://codecov.io/gh/bsc-wdc/dislib/branch/master/graph/badge.svg"
         alt="Code Coverage"/>
  </a>
    
</p>

<p align="center"><b>
    <a href="https://www.bsc.es/research-and-development/software-and-apps/software-list/comp-superscalar/">Website</a> •  
    <a href="https://dislib.readthedocs.io/en/latest">Documentation</a> •
    <a href="https://github.com/bsc-wdc/dislib/releases">Releases</a>
</b></p>


## Introduction

The Distributed Computing Library (dislib) provides distributed algorithms ready to use as a library. So far, dislib is highly focused on machine learning algorithms, and it is greatly inspired by [Scikit-learn](https://scikit-learn.org/). However, other types of numerical algorithms might be added in the future. Dislib has been implemented on top of PyCOMPSs programming model, and it is being developed by the [Workflows and Distributed Computing group](https://github.com/bsc-wdc) of the [Barcelona Supercomputing Center](https://www.bsc.es/). The library is designed to allow easy local development through docker. Once the code is finished, it can be run directly on any distributed platform without any further changes. This includes clusters, supercomputers, clouds, and containerized platforms. For more information on which infrastructures and architectures are supported refer to [Availability](#availability).



## Contents

- [Quickstart](#quickstart)
- [Availability](#availability)
- [Contributing](#contributing)
- [License](#license)


## Quickstart

Follow the steps below to get started with wdc Dislib.

#### 1. Install Docker and docker-py

**Warning:** requires docker version >= 17.12.0-ce


1. Follow these instructions

   - [Docker for Mac](https://store.docker.com/editions/community/docker-ce-desktop-mac). Or, if you prefer to use [Homebrew](https://brew.sh/).

   - [Docker for Ubuntu](https://docs.docker.com/install/linux/docker-ce/ubuntu/#install-docker-ce-1).

   - [Docker for Arch Linux](https://wiki.archlinux.org/index.php/Docker#Installation).

Be aware that for some distros the docker package has been renamed from `docker` to `docker-ce`. Make sure you install the new package.

2. Add user to docker group to run dislib as a non-root user.

    - [Instructions](https://docs.docker.com/install/linux/linux-postinstall/)


3. Check that docker is correctly installed

```
docker --version
docker ps # this should be empty as no docker processes are yet running.
```

4. Install [docker-py](https://docker-py.readthedocs.io/en/stable/)

```
sudo pip3 install docker
```

#### 2. Install the dislib

Download the **[latest release](https://github.com/bsc-wdc/dislib/releases)**.


Extract the tar file from your terminal:
```bash
tar -zxvf dislib_v0.1.0.tar.gz
```

Move it into your desired installation path and link the binary to be executable from anywhere:
```bash
sudo mv dislib_v* /opt/dislib
sudo ln -s /opt/dislib/dislib /usr/local/bin/dislib
```



#### 3. Start dislib in your development directory

Initialize the dislib where your source code will be (you can re-init anytime). This will allow docker to access your local code and run it inside the container.

**Note** that the first time dislib needs to download the docker image from the registry, and it may take a while.
```
# Without a path it operates on the current working directory.
dislib init

# You can also provide a path
dislib init /home/user/replace/path/
```

#### 4. Run a sample application

**Note**: running the docker dislib does not work with applications with GUI or with visual plots such as `examples/clustering_comparison.py`).

First clone dislib repo and checkout release 0.1.0 (docker version and dislib code should preferably be the same to avoid inconsistencies):

```bash
git clone https://github.com/bsc-wdc/dislib.git
git co v0.1.0
```

Init the dislib environment in the root of the repo.
The source files path are resolved from the init directory which sometimes can be confusing. As a rule of thumb, initialize the library in a current directory and check the paths are correct running the file with `python3 path_to/file.py` (in this case `python3 examples/rf_iris.py`).

```bash
cd dislib
dislib init
dislib exec examples/rf_iris.py
```

The log files of the execution can be found at $HOME/.COMPSs.

You can also init the library inside the examples folder. This will mount the examples directory inside the container so you can execute it without adding the path:
```bash
cd dislib/examples
dislib init
dislib exec rf_iris.py
```

#### 5. Adding more nodes


**Note**: adding more nodes is still in beta phase. Any suggestion, issue, or feedback is highly welcome and appreciated.


To add more computing nodes, you can either let docker create more workers for you or manually create and config a custom node.

For docker just issue the desired number of workers to be added. For example, to add 2 docker workers:
```
dislib components add worker 2
```

You can check that both new computing nodes are up with:

```
dislib components list
```

If you want to add a custom node it needs to be reachable through ssh without user. Moreover, dislib will try to copy the `working_dir` there, so it needs write permissions for the scp.

For example, to add the local machine as a worker node:

```
dislib components add worker '127.0.0.1:6'
```

* '127.0.0.1': is the IP used for ssh (can also be a hostname like 'localhost' as long as it can be resolved).
* '6': desired number of available computing units for the new node.

**Please be aware** that `dislib components` will not list your custom nodes because they are not docker processes and thus it can't be verified if they are up and running.

## Availability

Currently, the following supercomputers have already PyCOMPSs installed and ready to use. If you need help configuring your own cluster or supercomputer, drop us an email and we will be pleased to help.

- Marenostrum 4 - Barcelona Supercomputing Center (BSC)
- Minotauro - Barcelona Supercomputing Center (BSC)
- Nord 3 - Barcelona Supercomputing Center (BSC)
- Cobi - Barcelona Supercomputing Center (BSC)
- Juron - Jülich Supercomputing Centre (JSC)
- Jureca - Jülich Supercomputing Centre (JSC)
- Ultraviolet - The Genome Analysis Center (TGAC)
- Archer - University of Edinburgh’s Advanced Computing Facility (ACF)

Supported architectures:
- [Intel SSF architectures](https://www.intel.com/content/www/us/en/high-performance-computing/ssf-architecture-specification.html)
- [IBM's Power 9](https://www.ibm.com/it-infrastructure/power/power9-b)

## Contributing

Contributions are **welcome and very much appreciated**. We are also open to starting research collaborations or mentoring if you are interested in or need assistance implementing new algorithms.
Please refer [to our Contribution Guide](CONTRIBUTING.md) for more details.


## License

Apache License Version 2.0, see [LICENSE](LICENSE)
