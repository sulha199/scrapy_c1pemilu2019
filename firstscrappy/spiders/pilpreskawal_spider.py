import scrapy
import json
import datetime
from random import randint
from scrapy.http.request import Request

class PilpresSpider(scrapy.Spider):
	name = "pilpreskawal"
	start_urls = [
		'https://pantau.kawalpilpres2019.id/api/tps.json?nocache=' + str(randint(100000,999999999))
	]
	branchLimit = 999999 # when testing the code it is better to make its value to 1 in order to shorten the runtime
	finalResult = []

	def makeUrl(self, kodeWilayah):
		return 'https://pantau.kawalpilpres2019.id/api/tps-' + str(kodeWilayah) + '.json?nocache=' + str(randint(100000,999999999))

	def parse(self, response):
		jsonresponse = json.loads(response.body_as_unicode())
		count = 0
		for propinsi in jsonresponse:
			count += 1
			if (count <= self.branchLimit and count <= len(jsonresponse)):
				result = {
					'idPropinsi': propinsi.get('id'),
					'propinsi': propinsi
				}
				request = Request(self.makeUrl(result.get('idPropinsi')), callback=self.parsePropinsi, meta=result)
				yield request
			else:
				yield

	def parsePropinsi(self, response):
		propinsi = response.meta['propinsi']
		idPropinsi = response.meta['idPropinsi']
		jsonresponse = json.loads(response.body_as_unicode())
		count = 0
		for kab in jsonresponse:
			count += 1
			if (count <= self.branchLimit and kab.get('id').isnumeric()):
				result = {
					'idKab': kab.get('id'),
					'kab': kab,
					'idPropinsi': idPropinsi,
					'propinsi': propinsi,
				}
				request = Request(self.makeUrl(result.get('idKab')), callback=self.parseKab, meta=result)
				yield request
			else:
				yield


	def parseKab(self, response):
		propinsi = response.meta['propinsi']
		idPropinsi = response.meta['idPropinsi']
		idKab = response.meta['idKab']
		kab = response.meta['kab']
		jsonresponse = json.loads(response.body_as_unicode())
		count = 0
		for kec in jsonresponse:
			count += 1
			if (count <= self.branchLimit and kec.get('id').isnumeric()):
				result = {
					'idPropinsi': idPropinsi,
					'idKab': idKab,
					'propinsi': propinsi,
					'kab': kab,
					'idKec': kec.get('id'),
					'kec': kec
				}
				request = Request(self.makeUrl(result.get('idKec')), callback=self.parseKec, meta=result)
				yield request
			else:
				yield

	def parseKec(self, response):
		propinsi = response.meta['propinsi']
		idPropinsi = response.meta['idPropinsi']
		idKab = response.meta['idKab']
		kab = response.meta['kab']
		idKec = response.meta['idKec']
		kec = response.meta['kec']
		jsonresponse = json.loads(response.body_as_unicode())
		count = 0
		for kel in jsonresponse:
			count += 1
			if (count <= self.branchLimit and kel.get('id').isnumeric()):
				result = {
					'idPropinsi': idPropinsi,
					'idKab': idKab,
					'propinsi': propinsi,
					'kab': kab,
					'idKec': idKec,
					'kec': kec,
					'idKel' : kel.get('id'),
					'kel': kel
				}
				request = Request(self.makeUrl(result.get('idKel')), callback=self.parseKel, meta=result)
				yield request
			else:
				yield

	

	def parseKel(self, response):
		propinsi = response.meta['propinsi']
		idPropinsi = response.meta['idPropinsi']
		idKab = response.meta['idKab']
		kab = response.meta['kab']
		idKec = response.meta['idKec']
		kec = response.meta['kec']
		idKel = response.meta['idKel']
		kel = response.meta['kel']
		jsonresponse = json.loads(response.body_as_unicode())

		count = 0
		for tps in jsonresponse:
			count += 1
			if (count <= self.branchLimit and tps.get('id').isnumeric()):
				result = {
					'idPropinsi': idPropinsi,
					'propinsi': propinsi.get('nama_wilayah'),
					'idKab': idKab,
					'kab': kab.get('nama_wilayah'),
					'idKec': idKec,
					'kec': kec.get('nama_wilayah'),
					'idKel' : idKel,
					'kel': kel.get('nama_wilayah'),
					'tps': tps.get('nama_wilayah'),
					'01': tps.get('jokowi_amin'),
					'02': tps.get('prabowo_sandi')
				}
				yield result
			else:
				yield