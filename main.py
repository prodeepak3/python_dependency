# Hello World program in Python
import pip   
import json
lst = []
def install(package):
    return pip.main(['install', package]);
with open('file.json') as json_data:
    d = json.load(json_data);
    for key, value in dict.items(d["dependencies"]):
        if(install(key+"=="+value)!=0):
            lst.append(key)
			
print("Packages not installed: \n");
for item in lst:
    print(item+"\n");


