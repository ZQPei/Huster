from distutils.core import setup

setup(
    name='Huster',
    version='0.0.1',
    author='ZQPei',
    author_email='peiziqiang@gmail.com',
    packages=['huster'],
    url='https://github.com/lufficc/Vizer',
    scripts=[],
    description='Boxes and masks visualization tools.',
    install_requires=[
        "opencv-python",
        "numpy",
        "Pillow",
    ],
)
