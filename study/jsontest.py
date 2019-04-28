#!/usr/bin/python
import json
import demjson

json = '{"a":1,"b":2,"c":3,"d":4,"e":5}';

text = demjson.decode(json)
print  text


# jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}';
#
# text = json.loads(jsonData)
# print text