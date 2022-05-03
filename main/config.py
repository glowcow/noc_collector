#!/bin/python3

import os

class bc: #makes some colors
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    BLINK = '\33[5m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class snmp_com: #primary and old SNMP communities for check network devices, must be encoded in base64
    prim_com = os.environ['SNMP_COMM1']
    old_com = os.environ['SNMP_COMM2']

class radctl: #RADIUS rw user, all values must be encoded in base64
    username = os.environ['R_USR']
    password = os.environ['R_PASS']

class mik_acc: #mikrotik router rw user, all values must be encoded in base64
    username_m = os.environ['MT_USER']
    password_m = os.environ['MT_PASS']
    password_m2 = os.environ['MT_PASS2']

class sql_var: #usr_pg & pass_pg must be encoded in base64
    db_pg = os.environ['PG_DB']
    usr_pg = os.environ['PG_USR']
    pass_pg = os.environ['PG_PASS']
    host_pg = os.environ['PG_HOST']
    port_pg = 5432

class tg_api:
    bot_token = os.environ['TG_BOT']
    chat_id = os.environ['TG_CHAT']