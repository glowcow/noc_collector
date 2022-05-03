#!/bin/python3

import paramiko
import socket
import time
import sys
import telebot
import re

class bc:
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    BLINK = '\33[5m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def ssh_invoke(cmd, host, username, password):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            client.connect(hostname=host, username=username, password=password, timeout=5)
        except socket.timeout:
            print(f'{bc.RED}[!]{bc.ENDC} Host: {host} is unreachable, timed out')
            return False
        except paramiko.AuthenticationException:
            print(f'{bc.RED}[!]{bc.ENDC} Invalid credentials for {username}')
            return False
        except paramiko.ssh_exception.NoValidConnectionsError:
            print(f'{bc.RED}[!]{bc.ENDC} Connection refused by {host}')
            return False
        except paramiko.ssh_exception.SSHException as e:
            # socket is open, but not SSH service responded
            if e.message == 'Error reading SSH protocol banner':
                print(f'{bc.RED}[!]{bc.ENDC} {e.message} {hostname}')
                ssh_exec(cmd, host, username, password)
        else:
            #print(f'{bc.GREEN}[+]{bc.ENDC} Connection was established successfully to {host}')
            channel = client.invoke_shell(width=200, height=9000)
            time.sleep(2)
            channel.send('\n'+cmd+'\n')
            time.sleep(2)
            channel_data = str()
            out = channel.recv(999999)
            out = out.decode("ascii")
            #write_log(out)
            #print(f'{bc.WHITE}{out}{bc.ENDC}')
            channel.close()
            #print(f'{bc.RED}[!]{bc.ENDC} Disconnected from {host}')
            return out
    except:
        print(f'{bc.RED}[!]{bc.ENDC} Unknown SSH Error on {host}')
        return False

def write_log(result):
    wr_date = time.strftime('%b-%Y')
    log_date = time.strftime('%d-%b-%Y %H:%M:%S')
    result = result.split('\n')
    file = open(f'/FILE_SERVER/LOG/Script/{wr_date}_tele_bot_70240.log', 'a')
    for each in result:
        file.write(f'|{log_date}| {each}\n')
    file.close()

def tele_bot(msg):
    bot = telebot.TeleBot('949226977:AAH-CRfBcEdMHXInVc7XnUkDe-9johPAyDU')
    bot.send_message('-1001301855627', msg)

host = '176.213.132.137'
username = 'gutsconf'
password = '8nONIdjcVo'
cmd = (f'show router 70240 bgp routes 10.176.248.64/28')
result_raw = []
result = []
excld = ['10.191.244.41', '10.77.0.11', '10.77.0.3']

#Составление списка всех нейборов выданных коммандой cmd
for each in ssh_invoke(cmd, host, username, password).split('\n'):
    fnd = re.findall(r'[0-9]+(?:\.[0-9]+){3}', each)
    if fnd:
        each = each.split()[0]
        fnd = re.findall(r'[0-9]+(?:\.[0-9]+){3}', each)
        if fnd:
            result_raw.append(each)

#Исключение из этого списка нейборов из списка excld
for each in result_raw:
    if each in excld:
        continue
    else:
        result.append(each)

if len(result) == 0:
    write_log('===Неверных источников префиксов CODD_SVEKO не найдено===')
else:
    msg = "\n".join(result)
    tele_bot(f'===Неверные источники префиксов CODD_SVEKO===\n{msg}')
    write_log(f'===Неверные источники префиксов CODD_SVEKO===\n{msg}')
