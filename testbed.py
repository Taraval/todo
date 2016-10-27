from mod import *
import re

cmd_run = "cat /var/log/syslog | grep DHCPACK | grep 08:00:27:04:f6:6d | tail -1"
result = m_ssh.run("10.5.5.1", cmd_run, "testbed1", "testbed1")
if result:
    foobar = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', result[0])

serv_ip = None
if foobar:
    serv_ip = foobar.group(0)

print serv_ip
result = m_ssh.run(serv_ip, "ps -ef", "root", "nbv12345")

#print result

for list in result:
    print list
