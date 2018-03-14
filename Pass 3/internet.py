from urllib.request import urlopen
with urlopen('https://crossfit.com/workout/') as response:
    for line in response:
        line = line.decode('utf-8')  # Decoding the binary data to text.
        if 'Wednesday' in line:  # leta efter något
            print(line)

from lxml import html 
import requests #måste installera lxml and requests!
page = requests.get('https://www.antagning.se/se/search?publishers=hv&period=VT_2018&searchableOnly=on&semesterPart=0')
tree = html.fromstring(page.content)
rows = tree.xpath('//h3[@class="heading4 moreinfolink"]/text()')
print(rows)

resp = requests.get('http://api.icndb.com/jokes/random/1')
data = resp.json()
joke = data['value'][0]["joke"]
print(joke)

"""import smtplib
server = smtplib.SMTP('localhost') # fungerar bara med en mailserver på localhost så klart
server.sendmail('william.jobe@hv.se', 'thedonald@whitehouse.gov',
    "To: thedonald@whitehouse.gov From: william.jobe@hv.se Testar SMTP från Python")
server.quit()"""