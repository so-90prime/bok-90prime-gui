[![Powered by pyINDI](https://img.shields.io/badge/powered%20by-pyINDI-blue?style=flat)](https://github.com/MMTObservatory/pyINDI)
![Support from Heising-Simons Foundation](https://img.shields.io/badge/support-Heising--Simons%20Foundation-brightgreen?style=flat)

# bok-90prime-gui
Web-based GUI for Bok/90Prime control. 


## Create Project

```bash
  % cd /home/primefocus
  % git clone https://github.com/so-90prime/bok-90prime-gui.git
  % cd /home/primefocus/bok-90prime-gui
  % echo "INDIHOST='localhost'" >> /home/primefocus/bok-90prime-gui/.env
  % echo "INDIPORT=7624"        >> /home/primefocus/bok-90prime-gui/.env
  % echo "WEBHOST='localhost'"  >> /home/primefocus/bok-90prime-gui/.env
  % echo "WEBPORT=5555"         >> /home/primefocus/bok-90prime-gui/.env
```


## Installing (with conda)

```bash
  % conda install --file /home/primefocus/bok-90prime-gui/conda.yml
```


## Installing (without conda)

```bash
  % python3 -m pip install python-dotenv
  % python3 -m pip install tornado
  % python3 -m pip install git+https://github.com/MMTObservatory/pyINDI.git
```

## Run

```bash
  % python3 /home/primefocus/bok-90prime-gui/src/bok.py
```


--------------------------------------

Last Modified: 20220829

Last Author: Phil Daly (pndaly@arizona.edu)
