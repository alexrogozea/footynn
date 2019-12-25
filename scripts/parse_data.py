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

def get_headers_score(row, score=True):
    header_dict = {}
    h_keys = ['fthg', 'ftag', 'b365h', 'b365d', 'b365a']
    if not score:
        h_keys = ['hg', 'ag', 'avgh', 'avgd', 'avga']
    h_vals = ['gh', 'ga', 'oh', 'od', 'oa']
    for x in range(len(row)):
        for n_key in range(len(h_keys)):
            if h_keys[n_key] in row[x].lower():
                header_dict[h_vals[n_key]] = x

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
                    headers = get_headers_score(row, has_score)
                else:
                    for head in list(headers.keys()):
                        row_result[head] = row[headers[head]]
                    results.append(row_result)
                row_c += 1
        except Exception as e:
            print(e, data_file)

    return results

def get_data_from_folder(folder):
    total_data = []

    for root, dirs, files in os.walk(folder):
        for file in files:
            if '.csv' in file:
                data_file = os.path.join(root, file)
                total_data.extend(get_data_points(data_file))

    total_data = total_data[:-1]

    return total_data

# print(len(get_data_from_folder('data/')))
