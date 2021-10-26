# Martre
Python Network Mapper / Scanner

```
usage: martre.py target [ports [ports ...]]

positional arguments:
  target      Target network in CIDR format eg. 192.168.1.0/24
  ports       Ports to scan on alive hosts
```

**example**
```
python martre.py 192.168.1.0/24 20 21 22 23 80
```
```
192.168.1.1 is up.
 :80 is open.
192.168.1.20 is up.
 :80 is open.
192.168.1.21 is up.
 :21 is open.
 :80 is open.
192.168.1.100 is up.
192.168.1.201 is up.
 :80 is open.
```
