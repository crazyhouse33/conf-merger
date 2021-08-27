# conf-merger

A litle python soft to cut down giant blop of configuration files into reusable and sharable litle pieces.

The goal being to create different kinds of kernels configs like this:

```
conf-merger -p linux-kernel -o mydesktop.conf keyboard screen mouse 
conf-merger -p linux-kernel -o server.conf linux-kernel keyboard bfs-shedule 
conf-merger -p linux-kernel -p /path/conf -o vmCenter.conf keyboard vmWareHypervisor grsecurity 
```
 
# Supported

 1. Linux kernel configuration

# Configuration folder

A configuration folder contain a set of reusable piece of configuration organized in a tree fashion.

## Regular configuration

A configuration block.

## Combo configuration

If /combo/ is present in a path to a configuration, then it's name is interpreted as a "-" separated list of configuration that, if all present in the user selection,  will trigger in the combo file.

## Alias configuration

If /alias/ is present in a path to a configuration, then the configuration is interpreted as a newline separated list of configuration to add to the mix. This feature is there only to facilitate breaking blocks of confs into smaller peaces without breaking scripts relying on the old block.

# Cli

Use -h option for detailed help per option
