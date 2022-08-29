[![Powered by pyINDI](https://img.shields.io/badge/powered%20by-pyINDI-blue?style=flat)](https://github.com/MMTObservatory/pyINDI)
![Support from Heising-Simons Foundation](https://img.shields.io/badge/support-Heising--Simons%20Foundation-brightgreen?style=flat)

# bok-90prime-gui
Web-based GUI for Bok/90Prime control. 


## Create Project

```bash
  % git clone https://github.com/so-90prime/bok-90prime-gui.git
  % cd bok-90prime-gui
  % echo "INDIHOST='localhost'" >> .env
  % echo "INDIPORT=7624"        >> .env
  % echo "WEBHOST='localhost'"  >> .env
  % echo "WEBPORT=5555"         >> .env
```


## Installing (with conda)

```bash
  % conda install --file conda.yml
```


## Installing (without conda)

```bash
  % python3 -m pip install python-dotenv
  % python3 -m pip install tornado
  % python3 -m pip install git+https://github.com/MMTObservatory/pyINDI.git
```


--------------------------------------

Last Modified: 20220829

Last Author: Phil Daly (pndaly@arizona.edu)
