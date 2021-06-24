"""Load CSV Files with the Python Standard Library"""

import csv
import numpy

filename = '../../pima-indians-diabetes.csv'
raw_data = open(filename, 'r')

# Or, you can use a URL
# from urllib import urlopen
# url = 'https://goo.gl/vhm1eU'
# raw_data = urlopen(url)

reader = csv.reader(raw_data, delimiter=',', quoting=csv.QUOTE_NONE)
x = list(reader)
data = numpy.array(x).astype('float')
print(data.shape)
