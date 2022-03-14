import csv
import airtable

def csv_to_dsl(file):
    data = {}
    data["field_type"] = None
    with open(file, encoding='utf-8') as csvf:
        csvReader = csv.reader(csvf)
        fields = next(csvReader)
        fields = [_.strip() for _ in fields]
        id = 0
        for rows in csvReader:
            rows = [_.strip() for _ in rows]
            data[id] = dict(zip(fields, rows))
            id += 1
    return data


def airtable_to_dsl(api_key, base_id, table_name):
    data = {}
    data["field_type"] = None
    at = airtable.Airtable(base_id, api_key)
    records = at.get(table_name)
    for id, record in enumerate(records['records']):
        if record['fields'] != {}:
            data[id] = dict(record['fields'])
    return data