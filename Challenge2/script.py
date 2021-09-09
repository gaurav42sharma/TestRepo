import re 
import time
import json
import urllib.request

res = {}
base_url = 'http://169.254.169.254/latest/meta-data/'

def find_contents(metaurl):
 return urllib.request.urlopen(metaurl).read().decode("utf-8")

def iterate_content(contents):
    for folder in contents.splitlines():   
        string_check= re.compile('/') 
        if(string_check.search(folder) == None):  
            finalurl=base_url+folder 
            final_val = find_contents(finalurl)
            res[folder] = final_val
        else: 
            pass
    return res

result = iterate_content(find_contents(base_url))

print(result)



