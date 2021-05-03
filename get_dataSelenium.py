from selenium import webdriver
from time import sleep
import pandas as pd
from selenium.webdriver.common.keys import Keys
import csv
# 1.khai bao bien brower
brower = webdriver.Chrome(executable_path="./chromedriver.exe")# window 10
# brower = webdriver.Chrome(executable_path="./chromedriver")# linux
# 2.mo mot trang web
brower.get("https://diemthi.vnexpress.net/#area=2&college=undefined&q=score1")
for i in range(1, 5):# lấy 5 tỉnh
	# Đợi trang web mở
	sleep(5)

	# click form chọn tỉnh
	local = brower.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/span/span[1]/span/span[2]')
	local.click()
	# điền form lấy từng tỉnh
	local = brower.find_element_by_xpath("/html/body/span/span/span[1]/input")
	ma_tinh = i
	ma_tinh = str(i)
	local.send_keys(ma_tinh)
	local.send_keys(Keys.ENTER)
	sleep(5)
	# get data
	data = brower.find_element_by_xpath('//*[@id="result"]/div[2]/div[2]/div/div[2]/div[3]/div/table/tbody')

	# xuất data (Châu) -> csv
	data = data.text
	# data = data.split(' ')
	print(data)
	#data1 = open("data1.text","w+")
	#data1.writelines(data)
	#Xuli  = data1.readlines(data)
	#diemtoan = []
	#diemly = []
	#with open('data.csv', mode='w') as file:
	    #Xuli = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	    #Xuli.writerow(diemtoan)
	    #Xuli.writerow(diemly)
	# data1.close()

# 4.close brower
brower.close()
