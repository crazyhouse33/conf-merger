#!/usr/bin/python
import argparse
import os
from config.config_dir import default_dir 
from config.config_dir import class_matcher 

def parseArgs(*args):
    parser = argparse.ArgumentParser(description='Sub configuration manager')
    parser.add_argument('-p', '--path',  nargs='+', help= f"Paths to configuration folders. Can be relative to {default_dir} conf repository provided in this repo. Configurations will be searched from left to right providing an overiding mehanism")
    parser.add_argument('-t', '--type', choices= class_matcher.keys(), help= f"Force configuration type. Not required if given --conf-dir folders are named accordingly")
    parser.add_argument('-c', '--check', action= "store_true", help = "Fully check configuration of any selected individual configuration folder")
    parser.add_argument('-o', '--dest',  default="./result.conf", help = "Destination of the resulting configuration choice. (default: %(default)s )")
    #parser.add_argument('-l', '--list',  action= "store_true", help = "List all selectable configuration according to current --conf-dir selection")
    parser.add_argument('-b', '--build-dir',  default=".", type = dir_path, help = "Build directory used for kernels modes. (default: %(default)s )")
    parser.add_argument('configs', nargs='+', help = "Name of configs you want to merge")

    args = parser.parse_args(*args)
    return args

def dir_path(path):
    if os.path.isdir(path):
        return path
    else:
        raise argparse.ArgumentTypeError(f"readable_dir:{path} is not a valid path")

# TODO heritate specific parser for linux kernel dealing with build dir and stuff
