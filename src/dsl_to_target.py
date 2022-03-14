import airtable
import csv

def dsl_to_airtable(dsl, api_key, base_id, table_name, clear=True):
    at = airtable.Airtable(base_id, api_key)
    records = at.get(table_name)
    exist_ids = [i['id'] for i in records['records']]
    if clear:
        for ei in exist_ids:
            at.delete(table_name, ei)
    for key, val in dsl.items():
        if key == "field_type":
            continue
        at.create(table_name, val)
    return


def dsl_to_csv(dsl, file):
    fields = dsl[0].keys()
    with open(file, 'w') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(fields)
        for key, vals in dsl.items():
            if key == "field_type":
                continue
            csv_writer.writerow(vals.values())
    return