import sys
from lib import *

def main():
    solver = cc.CC_DAG()
    parser = smtp.smt_parser()
    print(sys.argv)
    equations,atoms = parser.parse(sys.argv[1])

if __name__ == "__main__":
    main()
