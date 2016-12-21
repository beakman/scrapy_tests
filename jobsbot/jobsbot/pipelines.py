# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import requests
import time

class JobsbotPipeline(object):

    def process_item(self, item, spider):
    	title = item['title'][0]
    	content = item['content'][0]
    	place = item['header'][0]
    	url = item['url']
    	message = '%s \n -----------\n%s\n\n%s\n\n%s' % (title, content, place, url)

    	if item['city'] == 'fuengirola':
        	requests.get('https://api.telegram.org/bot279656133:AAHoIJwa8iG7v7-V6i8zCL6YKaYRFqqep_g/sendMessage?chat_id=@trabajofuengirola&disable_notification=true&disable_web_page_preview=true&text='+message)
        	time.sleep(5)
    	if item['city'] == 'malaga':
        	requests.get('https://api.telegram.org/bot279656133:AAHoIJwa8iG7v7-V6i8zCL6YKaYRFqqep_g/sendMessage?chat_id=@trabajomalaga&disable_notification=true&disable_web_page_preview=true&text='+message)
    		time.sleep(5)
    	if item['city'] == 'andalucia':
        	requests.get('https://api.telegram.org/bot279656133:AAHoIJwa8iG7v7-V6i8zCL6YKaYRFqqep_g/sendMessage?chat_id=@trabajoandalucia&disable_notification=true&disable_web_page_preview=true&text='+message)
    		time.sleep(5)
		if item['city'] == 'sevilla':
        	requests.get('https://api.telegram.org/bot279656133:AAHoIJwa8iG7v7-V6i8zCL6YKaYRFqqep_g/sendMessage?chat_id=@trabajosevilla&disable_notification=true&disable_web_page_preview=true&text='+message)
    		time.sleep(5)