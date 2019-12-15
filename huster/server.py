import os
import sys
if sys.version_info.major == 2:
    from .SimpleHTTPServerWithUpload_py2 import server
elif sys.version_info.major == 3:
    from .SimpleHTTPServerWithUpload_py3 import server
else:
    raise RuntimeError("Python version not found!")

__all__ = ['build_server', 'run_server']

    
def run_server(port=8088, base_dir="/"):
    if os.path.isdir(base_dir):
        os.chdir(base_dir)
    else:
        raise UserWarning("base_dir is not a rightful directory")
        os.chdir("/")

    server(port=port)
    

def parse_args():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", default=8000, type=int)
    parser.add_argument("--base_dir", default="/", type=str)
    return parser.parse_args()


def build_server():
    args = parse_args()
    run_server(port=args.port, base_dir=args.base_dir)


if __name__ == "__main__":
    build_server()
    