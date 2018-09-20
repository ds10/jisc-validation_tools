import json
import os


dirname = os.path.dirname(__file__)

# This assumes that first line has name on with a # heading and first two ##headings are description and notes. Every entity must have a format


def main():

    #this makes a basic json object
    obj =  dict()
    atr = dict()


    mdfiles = os.path.join(dirname,"mdfiles")
    for filename in os.listdir(mdfiles):
        if filename.endswith('.md'): 
            with open(os.path.join(mdfiles, filename)) as f:
                #read all lines and strip out newline
                content = f.readlines()
                content = [x.strip() for x in content]
                #the first line is the dictionary, minus the hash
                content[0] = content[0][2:] 
                obj[content[0]]  = dict()               

                #find indices of titles
                indicesofentities = [i for i, s in enumerate(content) if s.startswith('## ')]
                indicesofentities = indicesofentities[2:]
                indicesofformats = [i for i, s in enumerate(content) if s.startswith('### Format')]
               

                ##remove
                for entity in indicesofentities:
                    print(entity)
                    content[entity] = content[entity][3:]

                ##create structure
                f = 0
                for entity in indicesofentities:
                    idx = indicesofformats[f] + 1
                    atr[content[entity]] =  content[idx]
                    obj[content[0]] = atr
                    f+=1

                ##write to json
                filename = content[0] + ".json"
                filepath = os.path.join(dirname,"mdfiles",filename)
                with open(filepath, 'w') as outfile:
                    json.dump(obj, outfile)


   

if __name__ == '__main__':
   main()