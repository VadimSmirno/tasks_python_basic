import requests
import re

url = 'http://www.columbia.edu/~fdc/sample.html'

my_req = requests.get(url=url)
res = my_req.text
print(re.findall(r'<h3 id=".*">(.*)</h3>', res))

# зачёт!
