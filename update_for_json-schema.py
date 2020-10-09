# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 10:35:07 2020

@author: ian.berg
"""

import os, json
rt = "C:\\Users\\ian.berg\\Documents\\GitHub\\GMNSpy\\spec"
for root, dir, files in os.walk(rt):
    for file in files:
        print(file)
        if file == "gmns.spec.json":
            continue
        name = file[:file.find(".")]
        f = open(os.path.join(rt, file))
        table = json.load(f)
        table["title"] = name
        table["properties"] = {}    
        for field in table['fields']:
            field_name = field['name']
            table['properties'][field_name] = field
            del table['properties'][field_name]['name']
            try:
                table['properties'][field_name].update(table['properties'][field_name]['constraints'])
                del table['properties'][field_name]['constraints']
            except KeyError:
                continue
        del table["fields"]
        f.close()
        g = open(os.path.join(rt, file), "w")
        json.dump(table, g, indent = 4)
        g.close()
