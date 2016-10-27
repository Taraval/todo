#!/usr/bin/python
import paramiko
import time

def run(s_host, s_exec, s_username, s_password, i_port=22):
    """
    :param s_host: The server name or ip address.
    :param s_exec:  The command to be executed on the host.
    :param s_username: The username for the server.
    :param s_password: The Password used for the server.
    :param i_port: The port number of the server.
    :return: The result print out the result in list, and False when empty.
    """
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    l_result = False

    try:
        ssh.connect(s_host, i_port, s_username, s_password)
        stdin, stdout, stderr = ssh.exec_command(s_exec)
        if stdout:
            i_sleep = 0
            while not stdout.channel.eof_received:
                time.sleep(0.5)
                i_sleep += 0.5
                if i_sleep > 10:
                    stdout.channel.close()
                    break
            l_result = stdout.readlines()
    except Exception as err:
        print "error: " + str(err)
    ssh.close()

    return l_result
