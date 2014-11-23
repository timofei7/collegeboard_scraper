from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from collegeboard.items import CollegeItem
from string import strip

WHOLESECTIONS=[u'Type of School',u'Setting',u'Most Popular Majors', u'General Athletics', u"Degree's Available",\
u'Learning Environment', u'Special Study Options', u'Off-Campus Study Options', u"Sport's Levels Available",\
u'Tests', u'Financial Aid Deadlines']

class CollegeBoardSpider(BaseSpider):
	name = 'collegeboard.org'
	allowed_domains = ['collegeboard.org']
	start_urls = []
	for i in range(5000):  #should be 5000
		start_urls.append('https://bigfuture.collegeboard.org/college-university-search/print-college-profile?id='+str(i))

	def parse(self, response):
		x = HtmlXPathSelector(response)

		college = CollegeItem()
		college['CollegeBoardUrl'] = response.url
		college['Name'] = x.select("//h1/text()").extract()[0].strip()


		college['Location'] = x.select("//h2/text()").extract()[0].strip()
		
		try:
			usize = x.select('//p/text()').re(r'Total undergraduates :\s*(.*)')[0].strip()
			if usize == u'--':
				usize = x.select('//p/text()').re(r'Degree-seeking undergrads :\s*(.*)')[0].strip()
			college['UndergradSize'] = usize
		except: pass


		try:
			college['RegularApplicationDeadline'] = x.select('//p/text()').re(r'Regular Application Deadline :\s*(.*)')[0].strip()
		except: pass
		else:
			try:
				college['RegularApplicationDeadline'] = x.select('//p/text()').re(r'Regular application due:\s*(.*)')[0].strip()
			except: pass


		tds = x.select('//td')
		for index,link in enumerate(tds):
			try:
				tdcategories=link.select('h2/text()').extract()
				if len(tdcategories) > 0:
					tdcategory=tdcategories[0].strip()
					if tdcategory == u'Main Address':
						try: 
							college['URL'] = link.select('p/text()').extract()[2].strip()
						except: pass
					if tdcategory == u'General Athletics':
						college['SportsDivision'] = link.select('//p/text()').re(r'Sport Member :\s*(.*)')
					if tdcategory in WHOLESECTIONS:
						varname = ''.join(e for e in tdcategory if e.isalnum())
						college[varname] = map(strip, link.select('p/text()').extract())
			except Exception, e:
				print "HIT AN ERROR: %s" % e
				print link


		return college
