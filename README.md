# NOC Collector
## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
* ```express_poller.py``` - Running via scheduler, polls MPLS routers (aggregators of multi-campus network) via SNMP for detect various troubles and notifies thru Telegram.
* ```nd_backup.py``` - Running via scheduler, collects current MPLS routers configuration every 24 hours.

## Technologies
Project is created with:
* PostgreSQL 13
* multiprocess 0.70.12.2
* paramiko 2.10.3
* psycopg2 2.9.1
* pyTelegramBotAPI 4.4.0
* python3_netsnmp 1.1a1
* schedule 1.1.0

## Setup
To run this project, setup Gitlab CI/CD and variables for your environment and deploy image to your docker.
