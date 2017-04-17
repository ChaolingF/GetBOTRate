import csv
import datetime
import time
import requests
from bs4 import BeautifulSoup

url ="http://rate.bot.com.tw/xrt?Lang=zh-TW"
period = input('Please enter how many seconds do you want to update the rate:')
seconds = int(period)
first_time_to_scarpe = 'yes'

while True:
	rate_r =  requests.get(url)
	rate_soup = BeautifulSoup(rate_r.content,'html.parser')

	currency = rate_soup.findAll(class_="hidden-phone print_show")
	rate = rate_soup.findAll(class_="rate-content-cash text-right print_hide")

	currency_number = (len(currency))
	print(datetime.datetime.now().today())
	print('\nCurrent Rate is : \n')
	fieldnames=['Time']
	final_rate=[datetime.datetime.now().today()]

	for i in range(0,currency_number-1):
	# Strip() Return a copy of the string with leading characters removed. http://www.runoob.com/python/att-string-strip.html
		fieldnames.append(currency[i].text.strip())
		final_rate.append(rate[i*2+1].text)
		print(currency[i].text.strip(),rate[i*2+1].text)

	#Write Chinese into csv file https://docs.python.org/3.2/library/csv.html
	with open ('GetRate.csv','a',newline='',encoding='utf-8-sig') as csvfile:		
		writer = csv.writer(csvfile, delimiter=',')
		if first_time_to_scarpe == 'yes':
			writer.writerow(fieldnames)
		writer.writerow(final_rate)
	first_time_to_scarpe = 'No'

	print('Now is',datetime.datetime.now().today())
	print('\nWait for',period,'seconds to update\n')
	time.sleep(seconds)