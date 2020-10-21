# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 10:35:07 2020

@author: ian.berg
"""
# first pass-through
import os, json
rt = "C:\\Users\\ian.berg\\Documents\\GitHub\\GMNSpy\\spec"
# for root, dir, files in os.walk(rt):
#     for file in files:
#         print(file)
#         if file == "gmns.spec.json":
#             continue
#         name = file[:file.find(".")]
#         f = open(os.path.join(rt, file))
#         table = json.load(f)
#         table["title"] = name
#         table["properties"] = {}    
#         for field in table['fields']:
#             field_name = field['name']
#             table['properties'][field_name] = field
#             del table['properties'][field_name]['name']
#             try:
#                 table['properties'][field_name].update(table['properties'][field_name]['constraints'])
#                 del table['properties'][field_name]['constraints']
#             except KeyError:
#                 continue
#         del table["fields"]
#         f.close()
#         g = open(os.path.join(rt, file), "w")
#         json.dump(table, g, indent = 4)
#         g.close()


# next thing: copy descriptions from gmns.spec.json
f = open(os.path.join(rt, "gmns.spec.json"))
metatable = json.load(f)
f.close()
metatable['tables'] = {} 
for field in metatable['resources']:
    field_name = field['name']
    metatable["tables"][field_name] = field
    
for root, dir, files in os.walk(rt):
    for file in files:
        print(file)
        if file == "gmns.spec.json":
            continue
        name = file[:file.find(".")]
        f = open(os.path.join(rt, file))
        table = json.load(f)
        f.close()
        required = []
        for field in table['properties']:
            try:
                if field == "description":
                    continue
                if table['properties'][field]['required'] == True:
                    required.append(field)
            except KeyError:
                continue
        table['required'] = required
        # table['description'] = metatable['tables'][name]['description']
        # table['$id'] = "spec/" + metatable['tables'][name]['schema']
        g = open(os.path.join(rt, file), "w")
        json.dump(table, g, indent = 4)
        g.close()       