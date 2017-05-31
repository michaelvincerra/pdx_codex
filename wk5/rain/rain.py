"""

"""
from rainday import RainDay

import os

RAIN_DIR = '/Users/michaelevan/temp/pdx_code/PythonFullStack/1_Python/3_Applied_Python/labs/rain_data/'




def file_handler(filesystem_path: str) -> str:   # context manager; input a str and output a str
    """
    Accepts a filesystem  Path
    Opens the File, and returns the entire file
    contents as a single string  literal.
    """

    with open(filesystem_path, 'r') as f:   # f is a file object
        raw_text = f.read()    # returns the entire content of file as a string.
        return raw_text


def split_strip(raw_data: str) -> list:  # Helper function
    split_up = raw_data.split('\n')
    no_header = split_up[11:]
    return no_header


def processor():
    # text = list(os.listdir(RAIN_DIR))                 # User Menu for multiple datasheets.

    full_path = os.path.join(RAIN_DIR, 'sample.rain')   # learn the os. commands.

    rain_data = file_handler(full_path)                 # Accepts params from file_handler above to open file contents

    stripped_data = split_strip(rain_data)              # Accepts params from split_strip above

    stripped = [data for data in stripped_data if data != '']   # Listcomp to remove the empty [] in list

    lines = [data.split() for data in stripped]                 # Est. lines only for stripped data

    # data_dict = [RainDay(date=rain_day[0], total=rain_day[1], hours=rain_day[2:]) for rain_day in lines]   # THIS USES THE CLASS METHOD


    #          '01-MAR-2002'    293      '293'   ['0', '0', ... ]
    data_dict = {rain_day[0]: (int(rain_day[1]), rain_day[2:]) for rain_day in lines if '-' not in rain_day[1:]}  # set rain_day[0] as key, which is ('DATE')

    max_rain = max(data_dict.items(), key=lambda t: t[1][0])    # data_dict.items() creates a list of tuples as a generator
    # max_rain = max(data_dict, key=lambda rd: rd.total) # THIS USES THE CLASS


    max_day = max_rain[0]
    max_amt = max_rain[1][0]

    print(max_day, max_amt)                                                                # lambda says focus on tuple [1][0] to determine result
    # print(data_dict.items())

    # captured = max_rain


    message1 = f'''
                On {max_day}, in Portland, Oregon, it rained {max_amt}
                hundreths of an inch.  Do you feel happier now? What's the 
                weather like today?
                '''
    message2 = f'''
                # WRITE A LIST COMP TO ARRIVE AT THE SUM OF EACH YEAR. 
    
                '''

    print (message1, message2)


processor()





# def processor():
#
#     # text = list(os.listdir(RAIN_DIR))
#
#     full_path = os.path.join(RAIN_DIR, 'sample.rain')
#
#     rain_data = file_handler(full_path)
#     return rain_data
#
#
# def split_strip(raw_data: str) -> list:
#     string_data = processor()
#     split_up = string_data.split('\n')
#     header = split_up[11:]
#     return header
#
#
