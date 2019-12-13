import sys
from .SimpleHTTPServerWithUpload import SimpleHTTPRequestHandler

__all__ = ['SimpleHTTPRequestHandler']


def build_server(port, base_dir="/"):
    import sys
    sys.argv.append('8088')
    if os.getcwd() != '/':
        os.chdir('/')
    test()
