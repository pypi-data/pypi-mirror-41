# nosypy
detection of anomalies in fixed camera time lapse sequences. 

[![License](http://img.shields.io/:license-mit-blue.svg)](http://octopress.mit-license.org) ![Version](https://img.shields.io/badge/version-0.0.2-blue.svg) ![Dependencies](https://img.shields.io/badge/dependencies-up%20to%20date-green.svg) 


## Install and setup virtualenv:

### Install **pip** first

    sudo apt-get install python3-pip

### Then install **virtualenv** using pip3

    sudo pip3 install virtualenv 

### Create virtualenv using Python3
    virtualenv -p python3 myenv

### Instead of using virtualenv you can use this command in Python3
    python3 -m venv myenv

>you can use any name insted of **myenv**

## Activate virtual environment

    source myenv/bin/activate

>the environment can be deactivated with the **deactivate** command

## Install Package using **pip** (recomended)
    pip install nosypy

## Install Package locally
    git clone https://github.com/brett-hosking/nosypy.git

### Install requirements from file 
    pip install -r requirements_CPU.txt
##### Or
    pip install -r requirements_GPU.txt

### Run pip to install package (locally)
    pip install .

## Upgrade Package (local)
    git pull
    pip install . --upgrade
