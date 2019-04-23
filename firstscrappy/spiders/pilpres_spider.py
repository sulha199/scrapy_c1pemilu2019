import scrapy
import json
from scrapy.http.request import Request

class PilpresSpider(scrapy.Spider):
	name = "pilpres"
	start_urls = [
		'https://pemilu2019.kpu.go.id/static/json/wilayah/0.json',
	]
	branchLimit = 999999999999999999

	def formatKodeWilayah(self, kodeWilayah):
		concat = kodeWilayah[0]
		for kode in kodeWilayah[1:]:
			concat = concat + '/' + str(kode)
		return concat

	def makeUrl(self, kodeWilayah):
		return 'https://pemilu2019.kpu.go.id/static/json/wilayah/' + self.formatKodeWilayah(kodeWilayah) + '.json'

	def makeTabulasiUrl(self, kodeWilayah):
		return 'https://pemilu2019.kpu.go.id/static/json/hhcw/ppwp/' + self.formatKodeWilayah(kodeWilayah) + '.json'

	def parse(self, response):
		jsonresponse = json.loads(response.body_as_unicode())
		count = 0
		for id, propinsi in jsonresponse.items():
			count += 1
			if (count <= self.branchLimit):
				result = {
					'idPropinsi': id,
					'propinsi': propinsi
				}
				request = Request(self.makeUrl([id]), callback=self.parsePropinsi, meta=result)
				yield request
			else:
				yield

	def parsePropinsi(self, response):
		propinsi = response.meta['propinsi']
		idPropinsi = response.meta['idPropinsi']
		jsonresponse = json.loads(response.body_as_unicode())
		count = 0
		for id, kab in jsonresponse.items():
			count += 1
			if (count <= self.branchLimit):
				result = {
					'idKab': id,
					'kab': kab,
					'idPropinsi': idPropinsi,
					'propinsi': propinsi,
				}
				request = Request(self.makeUrl([ idPropinsi, id]), callback=self.parseKab, meta=result)
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
		for id, kec in jsonresponse.items():
			count += 1
			if (count <= self.branchLimit):
				result = {
					'idPropinsi': idPropinsi,
					'idKab': idKab,
					'propinsi': propinsi,
					'kab': kab,
					'idKec': id,
					'kec': kec
				}
				request = Request(self.makeUrl([idPropinsi, idKab, id]), callback=self.parseKec, meta=result)
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
		for id, kel in jsonresponse.items():
			count += 1
			if (count <= self.branchLimit):
				result = {
					'idPropinsi': idPropinsi,
					'idKab': idKab,
					'propinsi': propinsi,
					'kab': kab,
					'idKec': idKec,
					'kec': kec,
					'idKel' : id,
					'kel': kel
				}
				request = Request(self.makeUrl([idPropinsi, idKab, idKec, id]), callback=self.parseKel, meta=result)
				yield request
			else:
				yield

	

	def parseKel(self, response):
		idPropinsi = response.meta['idPropinsi']
		idKab = response.meta['idKab']
		idKec = response.meta['idKec']
		idKel = response.meta['idKel']
		jsonresponse = json.loads(response.body_as_unicode())
		tabulasi = Request(self.makeTabulasiUrl([idPropinsi, idKab, idKec, idKel]), callback=self.parseTabulasi, meta = { 'kelList' :response.meta, 'tpsList': jsonresponse})
		yield tabulasi
		
	def parseTabulasi(self, response):
		tpsList = response.meta['tpsList']
		kelList = response.meta['kelList']
		propinsi = kelList['propinsi']
		idPropinsi = kelList['idPropinsi']
		idKab = kelList['idKab']
		kab = kelList['kab']
		idKec = kelList['idKec']
		kec = kelList['kec']
		idKel = kelList['idKel']
		kel = kelList['kel']
		jsonresponse = json.loads(response.body_as_unicode())
		tabulasi = jsonresponse.get('table')

		for id, tps in tpsList.items():
			result = {
				'idPropinsi': idPropinsi,
				'propinsi': propinsi.get('nama'),
				'idKab': idKab,
				'kab': kab.get('nama'),
				'idKec': idKec,
				'kec': kec.get('nama'),
				'idKel' : idKel,
				'kel': kel.get('nama'),
				'tps': tps.get('nama'),
				'01': tabulasi.get(id).get('21'),
				'02': tabulasi.get(id).get('22'),
			}
			yield result
