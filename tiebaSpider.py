# coding=utf-8
import requests

class TiebaSpider:
	def __init__(self, tieba_name):
		self.tieba_name = tieba_name
		self.url_temp = "https://tieba.baidu.com/f?wd=" + self.tieba_name + "&ie=utf-8&pn={}"
		self.headers = {"User-Agent":"Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1"}

	def get_url_list(self):  # 1.构建url列表
		return [self.url_temp.format(i*50) for i in range(1000)]

	def parse_url(self, url):
		# print(url)
		response = requests.get(url, headers=self.headers)
		return response.content.decode()

	def save_html(self, html_str, page_num):  # 保存html字符串
		file_path = "{}-第{}页.html".format(self.tieba_name, page_num)
		with open(file_path, "w", encoding="utf-8") as f:  # 李毅-第1页.html
			f.write(html_str)

	def run(self):  # 实现主要逻辑
 		# 1.构建url列表
		url_list = self.get_url_list()

		# 2.遍历，发送请求，获取响应
		for url in url_list:
			html_str = self.parse_url(url)
			# 3.保存
			page_num = url_list.index(url) + 1  # 页码数
			self.save_html(html_str, page_num)

	
if __name__ == "__main__":
	tieba_spider = TiebaSpider("lol")
	tieba_spider.run()
