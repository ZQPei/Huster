import os
import sys
if sys.version_info.major == 2:
    from SimpleHTTPServerWithUpload_py2 import test
elif sys.version_info.major == 3:
    from SimpleHTTPServerWithUpload_py3 import test


if __name__ == '__main__':
    sys.argv.append('8088')
    port = int(sys.argv[1])
    if os.getcwd() != '/':
        os.chdir('/')
    test(port=port)