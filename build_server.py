#!/home/pzq/anaconda3/bin/python

from huster.build_server import build_server, parse_args


if __name__ == "__main__":
    args = parse_args()
    build_server(port=args.port, base_dir=args.base_dir)
    