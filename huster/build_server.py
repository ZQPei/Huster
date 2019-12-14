import os
import sys
if sys.version_info.major == 2:
    from .SimpleHTTPServerWithUpload_py2 import run_server
elif sys.version_info.major == 3:
    from .SimpleHTTPServerWithUpload_py3 import run_server
else:
    raise RuntimeError("Python version not found!")

__all__ = ['SimpleHTTPRequestHandler']

    
def build_server(port=8088, base_dir="/"):
    if os.path.isdir(base_dir):
        os.chdir(base_dir)
    else:
        raise UserWarning("base_dir is not a rightful directory")
        os.chdir("/")

    run_server(port=port)
    

def parse_args():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", default=8000, type=int)
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    port = args.port
    build_server(port=port)