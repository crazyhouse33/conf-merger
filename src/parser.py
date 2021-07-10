#!/usr/bin/python
import argparse
import os

def parseArgs(*args):
    parser = argparse.ArgumentParser(description='Kernel sub configuration manager')
    parser.add_argument('-c', '--conf-dir',  required = True, type =dir_path)
    parser.add_argument('-b', '--build-dir',  default=".", type = dir_path)
    parser.add_argument('-o', '--dest',  default="./result.conf")
    parser.add_argument('configs', nargs='+')

    args = parser.parse_args(*args)
    return args

def dir_path(path):
    if os.path.isdir(path):
        return path
    else:
        raise argparse.ArgumentTypeError(f"readable_dir:{path} is not a valid path")
