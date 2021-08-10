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

## Regular configuration
A configuration folder contain a set of reusable piece of configuration organized in a tree fashion.

## Combo configuration

If /combo/ is present in a path to a configuration, then it's name is interpreted as a "-" list of configuration that are needed in order to trigger the combo.

# Cli

Use -h option for detailed help per option
