
import pandas as pd
import configparser
import logging

import configparser
import fileinput


dirname = os.path.dirname(__file__)
config = configparser.ConfigParser()
#config.read(os.path.join(dirname, 'config.ini'))
#logfile = os.path.join(dirname,config.get('Log','logfile'))
#logging.basicConfig(filename=logfile,level=logging.WARNING)


template  = os.path.join(dirname, "recipes" ,"attendance", "uxapi" , "attendance-template.json")
tsv  = os.path.join(dirname, "recipes" ,"attendance", "tsv" , "attendance.tsv")

def main():

    print(template)
    tsv_df = pd.read_csv(tsv, sep='\t', encoding="utf-8")
    print(tsv_df)

    
    for column in tsv_df:
        str_id = "**" + column + "**"
        #print(str_id)
        #print(tsv_df[column][0])
        with fileinput.FileInput(template, inplace=True, backup='.bak') as file:
            for line in file:
                print(line.replace(str_id, str(tsv_df[column][0])), end='')



    




if __name__ == '__main__':
   main()