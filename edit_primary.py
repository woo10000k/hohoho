import json
import os
import time

path = "./origin"
path42 = "./copyto"
pathlist = []
pathlist42 = []

for (path, dir, file) in os.walk(path):
#    dir = sorted(dir)
    if len(file) != 0:
        file = sorted(file)
        for i in range(len(file)):
            pathlist.append(path + "/" + file[i])

for (path42, dir, file) in os.walk(path42):
#    dir = sorted(dir)
    if len(file) != 0:
        file = sorted(file)
        for i in range(len(file)):
            pathlist42.append(path42 + "/" + file[i])


u=0
x=0
obj=0
j=0

for k in range(len(pathlist)):
    file_name = pathlist[k]
    
    if file_name[-3:] == "swp":
        file_name = "./origin/" + (file_name[:-4])[10:]    

    for v in range(len(pathlist42)):
        file_name_42 = pathlist42[v]        
        
        if(file_name[8:]) == (file_name_42[8:]):
            j+=1
            with open(file_name) as p:
                origin_data = json.load(p)
            origin_obj=origin_data["objects"]
            with open(file_name_42) as c:
                copyto_data = json.load(c)
            copyto_obj=copyto_data["objects"]
            
            if len(origin_obj) == len(copyto_obj):
                for q in range(len(origin_obj)):
                    origin_primary = origin_obj[q]["primary"]
                    copyto_primary = copyto_obj[q]["primary"]
                    obj +=1
                    if origin_primary != copyto_primary:
#                        print("origin===", origin_primary)
#                        print("copyto===", copyto_primary)    
                        copyto_primary = "{}".format(origin_primary)
#                        print("origin===", origin_primary)
#                        print("copyto===", copyto_primary)
                        copyto_data["objects"][q]["primary"]= "{}".format(origin_primary)
#                        print(copyto_data["objects"][q]["primary"])
#                        print(file_name_42)
                        u += 1
                        with open(file_name_42, 'w', encoding='utf-8') as c:
                            json.dump(copyto_data, c ,indent="\t")
                        with open(file_name_42, encoding='utf-8') as c:
                            copyto_data = json.load(c)
                        print(copyto_data["objects"][q]["primary"])
                        
                    
                    
print(u)
print(j)
print(obj)


#json primary 수정
