import utils
import json
from src.source_to_dsl import *
from src.dsl_to_target import *

def converter(source, target, file, api_key, base_id, table_name):
    DSL = ""

    # from source to DSL
    if source.lower() == "csv":
        DSL = csv_to_dsl(file)
    elif source.lower() == 'airtable':
        DSL = airtable_to_dsl(api_key, base_id, table_name)

    field_type = {}
    for key, val in DSL[0].items():
        if val.replace('.','',1).isdigit():
            field_type[key] = "Number"
        elif "@" in val:
            field_type[key] = "Email"
        else:
            field_type[key] = "String"
    DSL["field_type"] = field_type

    # print DSL
    print("------------ DSL: ------------")
    print(json.dumps(DSL, indent=4))
    print("converting ...")

    # from DSL to source
    if target.lower() == "airtable":
        dsl_to_airtable(DSL, api_key, base_id, table_name)
    elif target.lower() == "csv":
        dsl_to_csv(DSL, file)
    
    return 