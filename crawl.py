import json, sys, os, time,re,colorama,requests,time,random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
os.system('title Crawl_Data')
#https://www.facebook.com/groups/ReviewAnUongCanTho/posts/1133272720708413/
link_crawl = 'https://www.facebook.com/groups/ReviewAnUongCanTho/posts/1135324213836597/'




# #Khai báo browser
# browser = webdriver.Chrome(executable_path= 'C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe')

# # #mở chrome profile 3- Profile Cần Thơ
# options = webdriver.ChromeOptions()
# options.add_argument(r'--user-data-dir=D:\\a tool\\profile_tds\\User Data')
# options.add_argument('profile-directory=Profile 3')
# options.add_argument('--mute-audio')
# driver = webdriver.Chrome(executable_path=r'C:\\Program Files\\Google\Chrome\\Application\\chromedriver.exe', options=options)
# # driver.maximize_window() #khong set full man hinh
# ###options.headless = True # chạy ngầm



## You must click allow or not allow in selenium driver if you dont use profile chrome
from selenium import webdriver # thêm thư viện webdriver
from selenium.webdriver.common.keys import Keys #thêm thư viện keys cho máy

tk ="vohoangduy0596@gmail.com"
mk ="08nguyen16396742"

# mở chrome lên
driver = webdriver.Chrome(executable_path=r"C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe")
driver.set_window_size(700,1000)

#mở trang web
driver.get("https://www.facebook.com")

#điền tài khoản

user = driver.find_element_by_id("email") #tìm kiểu của tài khoản(sau chữ id)
user.send_keys(tk)#điền tài khoản
time.sleep(5)
#điền mật khẩu
password = driver.find_element_by_id("pass") #tìm kiểu của mật khẩu(sau chữ id)
password.send_keys(mk) #điền mật khẩu
time.sleep(5)
#nhấn enter
password.send_keys(Keys.ENTER)
time.sleep(5)

# mở trang facebook cần crawl
time.sleep(10)

driver.set_window_size(700,1000)
dr = driver.get(link_crawl)
time.sleep(5)

#cuộn xuống một đoạn để thấy bình luận liên quan nhất-cuộn đến chỗ đó mới nhận được
driver.execute_script("window.scrollTo(0,1150)")
time.sleep(4)
# driver.execute_script("window.scrollTo(0,1500)")
# time.sleep(10)
# time.sleep(10)
# time.sleep(100)
#========vào mục bình luận=========
#bấm vào mục phù hợp nhất hay bình luận liên quan nhất
# binh_luan = driver.find_element(By.NAME, 'Bình luận liên quan nhất')
# binh_luan.click()


### You must click allow or not allow in selenium driver if you dont use profile chrome
try:

	driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div[3]/div/div/div[4]/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div[8]/div/div[4]/div/div/div[2]/div[2]/div/div/div/span').click()
								 # '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div[3]/div/div/div[4]/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div[8]/div/div[4]/div/div/div[2]/div[2]/div[2]/div/div/span'
								 # '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div[3]/div/div/div[4]/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div[8]/div/div[4]/div/div/div[2]/div[2]/div/div/div/span'
except:
	driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[4]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div[8]/div/div[4]/div/div/div[2]/div[2]/div/div/div/span').click()
	
time.sleep(3)
# time.sleep(100)
#bấm vào mục tất cả bình luận
driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div[1]/div/div[3]/div[1]/div/div[1]/span').click()
time.sleep(3)

#bấm vào mục xem thêm n bình luận nữa
end = True
while end == True:
	try:
		#bấm vào mục xem thêm n bình luận nữa
		try:
			driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div/div/div[8]/div/div[5]/div/div/div[2]/div[4]/div/div[2]/span/span').click()
			driver.execute_script("window.scrollTo(0,1500)")
			time.sleep(5)
			end = True
		#bấm vào mục xem các bình luận trước
		except:
			driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div[3]/div/div/div[4]/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div[8]/div/div[4]/div/div/div[2]/div[2]/div[1]/div[2]/span/span').click()
			driver.execute_script("window.scrollTo(0,1500)")			
			time.sleep(5)
			end = True
	except:
		print('Đã tải hết bình luận')
		end = False

# print('Đã thoát khỏi vòng lặp')
#tìm tất cả comment và ghi ra màn hình

#in tất cả các link người comment
tags_link = '//a[@aria-hidden = "false"]'
link_list =driver.find_elements(By.XPATH,tags_link)



#in tất cả các tên 
tags_name = '//span[@class = "x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x4zkp8e x676frb x1nxh6w3 x1sibtaa x1s688f xzsf02u"]'
#							  x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x4zkp8e x676frb x1nxh6w3 x1sibtaa x1s688f xzsf02u
name_list = driver.find_elements(By.XPATH,tags_name)
temp = 0
#chỉ ghi vào mới và xóa cái cũ
tep = open('D:\\a tool\\DATACT\\data_cantho.csv',"w+",encoding='utf')
tieude = "Name,Link"+'\n'
tep.write(tieude)

#đọc hết tep link_thu
dong = tep.readline().strip()
while dong != '':
	dong = tep.readline().strip()

#ghi vào tệp
for i in link_list:
	if temp == 0:
		temp = temp +1
		pass

	else:
		try:
			link = i.get_attribute('href')
			name = name_list[temp-1].text
			string = str(link)
			vitri_batdau = string.find('1000')

			vitri_ketthuc = string.find('?')-1

			
			link1 = string[int(vitri_batdau):int(vitri_ketthuc)]

			text = str(name)+","+str(link)+'\n'
			tep.write(text)
			print("name facebook: " +str(name)+","+"link facebook: "+str(link)+'\n')
			temp = temp +1
		except IndexError:
			pass
		except:
			print('Lỗi rồi')
			exit()


# #cấu trúc tags "//tên_thẻ[@tên_loại_thẻ = 'tên thuộc tính đó']" ==> 
# tags = "//div[@class = 'x1n2onr6']"

# comment_list = driver.find_elements_by_xpath(tags)
# # print(comment_list)

# #in từng comment ra màn hình

# for comment in comment_list:
# 	#hiển thị tên người và nội dung cách nhau dấu :
# 	#người post
# 	tag_poster = '//div[@class = "x1r8uery x1iyjqo2 x6ikm8r x10wlt62 x1pi30zi"]'
# 	link_facebook = driver.find_element_by_xpath(tag_poster).get_attribute('href')
# 	print("link facebook: " +str(link_facebook))

# 	# class_tags_name = '//span[@class = "x3nfvp2"]'
# 	# name_poster = driver.find_element_by_xpath(class_tags_name)
# 	# print("name poster: "+str(name_poster.text))

# 	# tags_content = '//div[@class = "xdj266r x11i5rnm xat24cr x1mh8g0r x1vvkbs"]'
# 	# content_poster = driver.find_element_by_xpath(tags_content)
# 	# print("content: "+ str(content_poster.text))

# 	# print(content_poster.text)


#=======================================lấy link facebook========
# # #cấu trúc tags "//tên_thẻ[@tên_loại_thẻ = 'tên thuộc tính đó']" ==> 



#================================


print('Done')
driver.quit()
time.sleep(10)
print('======Starting Run ADD FRIEND======')
os.system("python add_friend.py")




#mở chrome profile 3
# options = webdriver.ChromeOptions()
# options.add_argument(r'--user-data-dir=D:\\a tool\\profile_tds\\User Data')
# options.add_argument('profile-directory=Profile 3')
# options.add_argument('--mute-audio')
# driver = webdriver.Chrome(executable_path=r'C:\\Program Files\\Google\Chrome\\Application\\chromedriver.exe', options=options)


# # mở trang facebook cần crawl
# link = 'https://www.tiktok.com/@sao.bongda/video/7025214955632856347'
# dr = driver.get(link)
# time.sleep(5)

# tags1 = '//div[@class = "tiktok-bylcfd-StyledUserLinkName e1g2efjf4"]'
# link_list =driver.find_elements_by_xpath(tags1)
# for i in link_list:
# 	tags_link1 = '//a[@class = "tiktok-bylcfd-StyledUserLinkName e1g2efjf4"]'
# 	temp = driver.find_element_by_xpath(tags_link1).get_attribute('href')
# 	print(temp)
# tiktok-bylcfd-StyledUserLinkName e1g2efjf4
# tiktok-bylcfd-StyledUserLinkName e1g2efjf4
# tiktok-bylcfd-StyledUserLinkName e1g2efjf4
