import requests
import lxml.html as lx

html = requests.get('https://habr.com/ru/')
page = lx.fromstring(html.content)

post = page.xpath('//li[@class="content-list__item content-list__item_post shortcuts_item"]')
post_name = post[0].xpath('//a[@class="post__title_link"]/text()')



