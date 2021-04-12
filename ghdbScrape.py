from requests_html import HTMLSession
print('''

╭━━╮╱╱╱╭╮╱╱╭━╮
╰╮╮┣━┳┳┫┣┳┳┫╋┣┳╮
╭┻╯┃╋┃╭┫━┫┃┃╭┫┃┃
╰━━┻━┻╯╰┻╋╮┣╯┣╮┃
╱╱╱╱╱╱╱╱╱╰━╯╱╰━╯

04-12-21
'''
)
url = 'https://www.exploit-db.com/google-hacking-database'

s = HTMLSession()
r = s.get(url)

r.html.render(sleep=1)

dorks = r.html.xpath('/html/body/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div[2]/div', first=True)

links = dorks.find('a')

for item in links:
	searches = item.text
	print(searches)
