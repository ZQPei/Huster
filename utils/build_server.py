#!/home/pzq/anaconda3/bin/python

import sys
from huster.server import build_server, parse_args


def huster():
    args = parse_args()
    build_server(port=args.port, base_dir=args.base_dir)
    sys.exit()


if __name__ == "__main__":
    huster()