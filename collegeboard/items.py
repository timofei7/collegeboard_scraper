# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class CollegeItem(Item):
  # define the fields for your item here like:
  # name = Field()
	CollegeBoardUrl=Field()
	Name=Field()
	Location=Field()
	Setting=Field()
	TypeofSchool=Field()
	UndergradSize=Field()
	URL=Field()
	MostPopularMajors=Field()
	SportsDivision=Field()
	GeneralAthletics=Field()
	DegreesAvailable=Field()
	LearningEnvironment=Field()
	SpecialStudyOptions=Field()
	OffCampusStudyOptions=Field()
	SportsLevelsAvailable=Field()
	Tests=Field()
	FinancialAidDeadlines=Field()
	RegularApplicationDeadline=Field()


