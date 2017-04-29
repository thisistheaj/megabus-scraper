# -*- coding: utf-8 -*-
import scrapy
import datetime as dt
from operator import methodcaller

class UsmegabusSpider(scrapy.Spider):
    name = "usmegabus"
    allowed_domains = ["us.megabus.com"]

    querydate = dt.date.today()
    delt = dt.timedelta(days=1)

    def newUrl(self,origin, destination,month, day, year):
        return 'http://us.megabus.com/JourneyResults.aspx?' + \
            'originCode=' + str(origin) + \
            '&destinationCode=' + str(destination) + \
            '&outboundDepartureDate=' + str(month) + '%2f' + str(day) + '%2f' + str(year) + \
            '&inboundDepartureDate=' + \
            '&passengerCount=' + str(1) + \
            '&transportType=' + str(0) + \
            '&concessionCount=' + str(0) + \
            '&nusCount=' + str(0) + \
            '&outboundWheelchairSeated=' + str(0) + \
            '&outboundOtherDisabilityCount=' + str(0) + \
            '&inboundWheelchairSeated=' + str(0) + \
            '&inboundOtherDisabilityCount=' + str(0) + \
            '&outboundPcaCount=' + str(0) + \
            '&inboundPcaCount=' + str(0) + \
            '&promotionCode=' + \
            '&withReturn=' + str(0)
 
    def start_requests(self):
        qd = self.querydate
        yield scrapy.Request(self.newUrl(127,123,qd.month,qd.day,qd.year), self.parse)

    def parse(self, response):
        bus_results = response.css('div.journeyresult div#JourneyResylts_OutboundList_main_div').extract_first()
        if bus_results is not None:
            yield {
                'Date': str(self.querydate.month) + '/' + str(self.querydate.day) + '/' + str(self.querydate.year),
                'results': list(filter(lambda x: x != '' and x != 'From', list(map(methodcaller('strip'),response.css('ul.journey li.five p ::text').extract()))))
            }
            self.querydate += self.delt 
            qd = self.querydate
            yield scrapy.Request(self.newUrl(127,123,qd.month,qd.day,qd.year), self.parse)
#        else:
#            self.querydate -= self.delt 
#            yield {
#                'Latest Date': str(self.querydate.month) + '/' + str(self.querydate.day) + '/' + str(self.querydate.year)
#            } 

