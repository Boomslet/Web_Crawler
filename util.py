import os
"""
"""


#
def create_dirs(url_name):
    ind = url_name.find(".") + 1
    name = url_name[ind:]
    
    if not os.path.exists(name):
        print('Creating ' + name)
        os.mkdir(name)


#
def write_file(path, data):
    with open(path, 'a') as f:
        f.write(data)
