from distutils.core import setup
from utils import copy_scripts_to_bin

copy_scripts_to_bin("./build_server.py")

setup(
    name='Huster',
    version='0.1',
    author='ZQPei',
    author_email='peiziqiang@gmail.com',
    packages=['huster'],
    url='https://github.com/ZQPei/Huster',
    scripts=[],
    description='HTTP Uploading Server Tool.',
    install_requires=[],
)
