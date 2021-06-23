import requests
import re

url = 'http://www.columbia.edu/~fdc/sample.html'

my_req = requests.get(url=url)
res = my_req.text
# pattern = re.compile('<h3 id=([^>]*)>([^<]*)</h3>')
print(re.findall(r'<h3 id=".*">(.*)</h3>', res))

# зачёт!
