import json
import os
from collections import defaultdict
import re

dirname = os.path.dirname(__file__)



def main():

    mdfiles = os.path.join(dirname,"mdfiles")
    for filename in os.listdir(mdfiles):
        if filename.endswith('.md'): 
            with open(os.path.join(mdfiles, filename)) as f:
                print("yes")
                content = f.read()
                #print(content)
                #grab what you need fro regular expressions
                print re.search(r'[\n\r].*Object Name:\s*([^\n\r]*)', myfile.read()).group(1)

    exit()
    json = []
    entityname = {}

    entityname = {'entityName': 'assessment_instance'}
    json.append(entityname)
    entityname = {'name': 'ASSESS_INSTANCE_ID', 'format': 'String (255)'}
    json.append(entityname)

    print (json)
    json.dumps(json) 

if __name__ == '__main__':
   main()