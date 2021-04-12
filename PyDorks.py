from requests_html import HTMLSession



text = 'site:* intitle:"Component Browser Login"'
url = 'https://www.google.com/search?q=' + text


s = HTMLSession()
r = s.get(url)

r.html.render(sleep=1)

heads = r.html.xpath('/html/body/div[7]/div/div[9]/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div/div[1]/a/div/cite', first=True)

print(heads)

'''links = heads.find('/div/cite')
print(links)
for item in links:
	print(item)'''