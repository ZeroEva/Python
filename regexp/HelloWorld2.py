import re

txt = "[root#zero-server ~]$ werisvlkds"
x = re.findall('^\[.*]\$ $', txt)
for x0 in x:
    print(x0)
