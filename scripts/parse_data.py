#!/usr/bin/env python3
import os
import csv


SCORE_NATIONS = [
    'BELGIUM',
    'DEUTSCHLAND',
    'ENGLAND',
    'FRANCE',
    'GREECE',
    'ITALY',
    'NETHERLANDS',
    'PORTUGAL',
    'SCOTLAND',
    'SPAIN',
    'TURKEY'
]

NOSCORE_NATIONS = [
    'ARGENTINA',
    'AUSTRIA',
    'BRAZIL',
    'CHINA',
    'DENMARK',
    'FINLAND',
    'IRELAND',
    'JAPAN',
    'MEXICO',
    'NORWAY',
    'POLAND',
    'ROMANIA',
    'RUSSIA',
    'SWEDEN',
    'SWITZERLAND',
    'USA'
]

DATA_FOLDER = 'data/'

# for root, dirs, files in os.walk(DATA_FOLDER):
#     for file in files:
#         if '.csv' in file:
#             print(os.path.join(root, file))

test_file = os.path.join(DATA_FOLDER, 'BELGIUM_0', 'BELGIUM_0_0304.csv')

def get_headers(row):
    header_dict = {}
    header_keys = [
        'home',
        'away',
        'home_goals',
        'away_goals',
        'home_odds',
        'draw_odds',
        'away_odds',
        'over_2_5',
        'under_2_5'
    ]
    for x in range(len(row)):
        if 'home' in row[x].lower():
            header_dict['home'] = x
        if 'away' in row[x].lower():
            header_dict['away'] = x
        if 


with open(test_file, 'r') as csvf:
    csv_r = csv.reader(csvf, delimiter=',')
    row_c = 0
    headers = []
    for row in csv_r:
        if row_c == 0:
            headers = get_headers(row)
        row_c += 1