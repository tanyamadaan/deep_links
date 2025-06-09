import csv
import mapping
import json

def bulk_read(data_file, qr_data={}, qr_list = []):
    with open(data_file, mode ='r', encoding='utf-8-sig') as file: 
        csvFile = csv.DictReader(file)
        for row in csvFile:
            data = dict(row)
            for key, value in data.items():
                k = mapping.key_mapping[key]
                qr_data[k] = value  
            qr_list.append(json.dumps(qr_data))
    return qr_list