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

# test_file = os.path.join(DATA_FOLDER, 'BELGIUM_0', 'BELGIUM_0_0304.csv')

def get_headers_score(row):
    header_dict = {}
    for x in range(len(row)):
        # if 'home' in row[x].lower():
        #     header_dict['home'] = x
        # if 'away' in row[x].lower():
        #     header_dict['away'] = x
        if 'fthg' in row[x].lower():
            header_dict['gh'] = x
        if 'ftag' in row[x].lower():
            header_dict['ga'] = x
        if 'b365h' in row[x].lower():
            header_dict['oh'] = x
        if 'b365d' in row[x].lower():
            header_dict['od'] = x
        if 'b365a' in row[x].lower():
            header_dict['oa'] = x
        # if '>2.5' in row[x].lower():
        #     header_dict['go25'] = x
        # if '<2.5' in row[x].lower():
        #     header_dict['gu25'] = x

    return header_dict

def get_headers_no_score(row):
    header_dict = {}
    for x in range(len(row)):
        if 'hg' in row[x].lower():
            header_dict['gh'] = x
        if 'ag' in row[x].lower():
            header_dict['ga'] = x
        if 'avgh' in row[x].lower():
            header_dict['oh'] = x
        if 'avgd' in row[x].lower():
            header_dict['od'] = x
        if 'avga' in row[x].lower():
            header_dict['oa'] = x

    return header_dict

def get_data_points(data_file):
    country = os.path.basename(data_file).split('_')[0]
    has_score = country in SCORE_NATIONS
    headers = {}
    results = []
    with open(data_file, 'r') as csvf:
        csv_r = csv.reader(csvf, delimiter=',')
        row_c = 0
        try:
            for row in csv_r:
                row_result = {}
                if row_c == 0:
                    if has_score:
                        headers = get_headers_score(row)
                    else:
                        headers = get_headers_no_score(row)
                else:
                    for head in list(headers.keys()):
                        row_result[head] = row[headers[head]]
                    results.append(row_result)
                row_c += 1
        except Exception as e:
            print(e, data_file)

    return results

DATA_FOLDER = 'data/'
total_data = []

for root, dirs, files in os.walk(DATA_FOLDER):
    for file in files:
        if '.csv' in file:
            data_file = os.path.join(root, file)
            total_data.extend(get_data_points(data_file))

total_data = total_data[:-1]
print(len(total_data))
for a in total_data:
    print(a)
