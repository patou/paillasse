# Script d'installation d'un fichier Wheel Python

import pip
import os


os.environ['HTTP_PROXY']="http://I24853:Montava36@proxy-surf.rte-france.com:3128"
os.environ['HTTPS_PROXY']="https://I24853:Montava36@proxy-surf.rte-france.com:3128"

from pip._internal import main as pipmain

def install_whl(path):
    pipmain(['install', path])

install_whl('D:\\Users\\poullennecgwi\\Downloads\\pgadmin4-4.14-py2.py3-none-any.whl')
