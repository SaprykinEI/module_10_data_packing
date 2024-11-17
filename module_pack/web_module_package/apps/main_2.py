import zipfile
from sys import path

path.append(r'..\packages')
path = r'pac'

with zipfile.ZipFile(r'Z:\Training\Top-school\Class Work\module_pack\web_module_package\extrapack.zip') as zip_ref:
    zip_ref.extractall(r'Z:\Training\Top-school\Class Work\module_pack\web_module_package\zip_package')

