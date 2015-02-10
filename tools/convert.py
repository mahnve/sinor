_unsorted = None
_in_sorted_order = None


import glob
import datetime
import os

files = glob.glob('*.markdown')

for f in files:
    print(f)
    date_part = f[0:10]
    name_part = f[11:]
    the_date = datetime.datetime.strptime(date_part, "%Y-%m-%d").date()
    dir = the_date.strftime("%Y/")
    if not os.path.exists(dir):
        os.makedirs(dir)
    new_path = dir + name_part
    with open(f) as f1:
        with open(new_path, 'w') as f2:
            f2.write('date: {}\n'.format(date_part))
            for line in f1:
                f2.write(line)
