#!/usr/bin/python3
"""
    Uses the fake API to get an employer and export the info in csv formater
"""
import csv
import requests
from sys import argv

if __name__ == "__main__":
    id_em = argv[1]
    url_employ = "https://jsonplaceholder.typicode.com/users/{}".format(id_em)
    url_todos = url_employ +        f_csv.writerows(list_report)
