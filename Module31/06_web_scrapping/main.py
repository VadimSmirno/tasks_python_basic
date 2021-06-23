import requests
import re


url = 'http://www.columbia.edu/~fdc/sample.html'

my_req = requests.get(url=url)
res = my_req.text

print (re.findall(r'<h3.+</h3>',res))


# TODO, для того, чтобы вывод получился как в примере, необходимо немного поправить регулярное выражение.

