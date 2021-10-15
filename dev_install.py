# use this to update the pytgcalls 
# due to the project in beta... we have to install it from differnet source and setup
# this file also has your telegram_vc_sample auth keys.
import os 
import sys
import shutil
import subprocess
import sys
from setuptools import Extension
from setuptools import find_packages
from setuptools import setup
from setuptools.command.build_ext import build_ext
import glob
import tempfile
import json

my_project_path = os.path.abspath(os.path.dirname(__file__))
print("Extension",my_project_path)


telegram_key = open('../telegram_vc_sample/auth_telegram.txt', 'r')
telegram_keys = json.load(telegram_key)
API_KEY = telegram_keys['API_KEY']
API_HASH = telegram_keys['API_HASH']
STRING_SESSION = telegram_keys['STRING_SESSION']
CHAT_ID = telegram_keys['CHAT_ID']
print(CHAT_ID)




is_linux = sys.platform.startswith('linux')
def get_node_installed():
    node =" yes |sudo apt install nodejs"
    npm =" yes |sudo apt install npm"
    install_node = subprocess.run(node, shell=True)
    install_npm = subprocess.run(npm, shell=True)

print("is_linux is -------------------------------->",is_linux)
if is_linux is True:
    get_node_installed()
else:
    print("not a linux system")
    


def looking_for_pytgcalls():
    all_folder ="../telegram_vc_sample"
    look_for_fodler = [ f.path for f in os.scandir(all_folder) if f.is_dir() ]

    for folder in look_for_fodler:
        if folder == "../telegram_vc_sample/pytgcalls":
            return True        
    else:
        print("did not find pytgcalls in project..")
        return False


def install_pytgcalls():
    try:
        install_telethon = "pip install Telethon"
        install_pytgcalls_dev = "git clone -b dev https://github.com/pytgcalls/pytgcalls && cd pytgcalls && python setup.py install"
        telethon = subprocess.run(install_telethon, shell=True)
        pytgcalls = subprocess.run(install_pytgcalls_dev, shell=True)
    except Exception as e:
        print("check to see if you have git install")
        exit()

def is_installed():
    main_dir  = my_project_path
    temp_dir = tempfile.mkdtemp()
    print(main_dir)
    folder  = f"{main_dir}/pytgcalls/build/" + "lib*/pytgcalls"
    print("folder",folder)
    for file in glob.iglob(folder, recursive=True):
        move_folder = shutil.move(file, temp_dir)
        shutil.rmtree(main_dir+"/pytgcalls")
        print("DONE")
    move_temp_to_main_dir = shutil.move(temp_dir+"/pytgcalls", main_dir)
    print("DONE MOVING STUFF AROUND")



# git clone -b dev https://github.com/pytgcalls/pytgcalls && cd pytgcalls && python setup.py install
