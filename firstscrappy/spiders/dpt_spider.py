import scrapy
import json
import datetime
from scrapy.http.request import Request
from scrapy.selector import Selector

class DptSpider(scrapy.Spider):
	name = "dpt"
	cssSelector = 'section.content table.table.table-bordered tbody tr'
	start_urls = [
		'https://lindungihakpilihmu.kpu.go.id/index.php/rekap',
	]
	branchLimit = 99999 # when testing the code it is better to make its value to 1 in order to shorten the runtime

	def getIdFromUrl(self, url):
		return url.split("/")[-1]

	def parse(self, response):
		propinsis = response.css(self.cssSelector).getall()
		count = 0
		for propinsiHtml in propinsis:
			count += 1
			if (count <= self.branchLimit):
				hxs = Selector(text = propinsiHtml)
				result = {
						'propinsi': hxs.css('td a::text').get(),
						'propinsiUrl': hxs.css('td a').attrib['href']
				}
				request = Request(result['propinsiUrl'], callback=self.parsePropinsi, meta=result)
				yield request

	def parsePropinsi(self, response):
		elements = response.css(self.cssSelector).getall()
		count = 0
		for html in elements:
			count += 1
			if (count <= self.branchLimit):
				hxs = Selector(text = html)
				result = response.meta
				result['kab'] = hxs.css('td a::text').get()
				result['kabUrl'] = hxs.css('td a').attrib['href']
				request = Request(result['kabUrl'], callback=self.parseKab, meta=result)
				yield request

	def parseKab(self, response):
		elements = response.css(self.cssSelector).getall()
		count = 0
		for html in elements:
			count += 1
			if (count <= self.branchLimit):
				hxs = Selector(text = html)
				result = response.meta
				result['kec'] = hxs.css('td a::text').get()
				result['kecUrl'] = hxs.css('td a').attrib['href']
				request = Request(result['kecUrl'], callback=self.parseKec, meta=result)
				yield request

	def parseKec(self, response):
		elements = response.css(self.cssSelector).getall()
		count = 0
		for html in elements:
			count += 1
			if (count <= self.branchLimit):
				hxs = Selector(text = html)
				result = response.meta
				result['kel'] = hxs.css('td a::text').get()
				kelId = self.getIdFromUrl(hxs.css('td a').attrib['href'])
				result['kelUrl'] = 'https://lindungihakpilihmu.kpu.go.id/index.php/dpk/verifikasi/' + kelId
				request = Request(result['kelUrl'], callback=self.parseKel, meta=result)
				yield request

	def parseKel(self, response):
		elements = response.css('table.table.table-bordered tbody tr').getall()
		count = 0
		for html in elements:
			count += 1
			if (count <= self.branchLimit):
				hxs = Selector(text = html)
				result = {
					'idPropinsi': self.getIdFromUrl(response.meta['propinsiUrl']),
					'propinsi': response.meta['propinsi'],
					'idKab': self.getIdFromUrl(response.meta['kabUrl']),
					'kab': response.meta['kab'],
					'idKec': self.getIdFromUrl(response.meta['kecUrl']),
					'kec': response.meta['kec'],
					'idKel': self.getIdFromUrl(response.meta['kelUrl']),
					'kel': response.meta['kel'],
					'tps': hxs.css('td a::text').get(),
					'dpt': hxs.css('td::text').getall()[-1]
				}
				yield result
 