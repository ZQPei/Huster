# Huster

HTTP Uploading Server Tool


![](https://img.shields.io/badge/python2-passing-brightgreen)
![](https://img.shields.io/badge/python3-passing-brightgreen)


## Install

You can install it from pip or source code.

- install from pip

    ```bash
    pip install huster
    ```

- install from source code

    ```bash
    git clone https://github.com/ZQPei/Huster.git
    cd Huster
    python setup.py install # use sudo if necessary
    ```


## Usage

```bash
build_server --port [port=8000] --base_dir [base_dir="/"]
```

or

```bash
python -m huster.server --port [port=8000] --base_dir [base_dir="/"]
```

For simplification, the following command can redirect the output to `/dev/null`.
```bash
nohup build_server --port 8000 >/dev/null 2>&1 &
```


## Example
If you have built a server on your machine, you can assess it by browsing `http://xxx.xxx.xxx.xxx:8000`. 

It provides a button to upload file from local to server.

![bash](./demo/huster_demo_bash.png)

![demo](./demo/huster_demo.png)


