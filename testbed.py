import m_ssh
import re

cmd_run = "cat /var/log/syslog | grep DHCPACK | grep 07:00:07:07:07:07 | tail -1"
result = m_ssh.run("10.10.10.8", cmd_run, "u1", "p1")
if result:
    foobar = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', result[0])

serv_ip = None
if foobar:
    serv_ip = foobar.group(0)

print serv_ip
result = m_ssh.run(serv_ip, "ps -ef", "root", "pa$$w0ord")

#print result

for list in result:
    print list
