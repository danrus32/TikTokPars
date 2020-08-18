import requests, datetime, os, random, sys
from bs4 import BeautifulSoup
import lxml.html as html
import re
import json
prox = {}
def ProxyCreate():
	get_proxy ('http://foxtools.ru/Proxy?al=True&am=True&ah=True&ahs=True&http=True&https=False')
	proxy = 'proxies.txt'
	proxies = open (proxy, 'r').read().splitlines()
	
	return proxies
headers_useragents = list ()
def useragent_list():
	global headers_useragents
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	return(headers_useragents)
	
def randomString(size):
	out_str = ''
	for i in range(0, size):
		a = random.randint(65, 90)
		out_str += chr(a)
	return(out_str)

def initHeaders():
	useragent_list()
	global headers_useragents
	headers = {
				'User-Agent': random.choice(headers_useragents),
				'Cache-Control': 'no-cache',
				'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
				'Referer': 'http://www.google.com/?q=' + randomString(random.randint(5,10)),
				'Keep-Alive': str(random.randint(110,120)),
				'Connection': 'keep-alive'
				}

	return headers

def get_proxy (url):
    r = requests.get (url)

    soup = BeautifulSoup (r.text, 'lxml')
    line = soup.find ('table', id = 'theProxyList').find ('tbody').find_all ('tr')	

    file = open ('proxies.txt', 'w+')
    
    for tr in line:
        td = tr.find_all ('td')

        ip = td[1].text
        port = td[2].text

        file.write ('http://' + ip + ':' + port + '\n')
	
class Parser:
	def __init__ (self,URL):
		
		for p in ProxyCreate():
			prox['http'] = p
			headers = initHeaders()
			response = requests.get(URL,proxies=prox,headers= headers)
			soup = BeautifulSoup(response.text,'lxml')
			response.encoding = 'utf-8'
			html.fromstring(response.text)
			file = open ('response.txt', 'w+',encoding="utf-8")
			file.write(str(response.text))
			
			script = soup.find('script',text=re.compile('props'))
			script = re.sub('<script crossorigin="anonymous" id="__NEXT_DATA__" type="application/json">','',str(script))
			script = re.sub('</script>','',str(script))
			
			self.jsonDataScript = json.loads(str(script))
			break
class UserData:
	def __init__(self,URL):

		self._userData = Parser(URL).jsonDataScript['props']['pageProps']['userData']
		self.secUid  = self._userData['secUid']
		self.userId  = self._userData['userId']
		self.isSecret = self._userData['isSecret']
		self.uniqueId  = self._userData['uniqueId']
		self.nickName  = self._userData['nickName']
		self.signature  = self._userData['signature']
		self.covers = self._userData['covers']
		self.covers_0  = self.covers[0]
		self.covers_1  = self.covers[1]
		self.coversMedium = self._userData['coversMedium']
		self.coversMedium_0 = self.coversMedium[0]
		self.coversMedium_1 = self.coversMedium[1]
		self.following  = self._userData['coversMedium']
		self.fans  = self._userData['fans']
		self.heart  = self._userData['heart']
		self.video  = self._userData['video']
		self.verified  = self._userData['verified']
		self.digg  = self._userData['digg']
		self.ftc  = self._userData['ftc']
		self.relation = self._userData['relation']
		self.openFavorite = self._userData['openFavorite']
class userInfo:
	def __init__(self,URL):
		self._userInfo_stats =Parser(URL).jsonDataScript['props']['pageProps']['userInfo']['stats']
		self._userInfo_user = Parser(URL).jsonDataScript['props']['pageProps']['userInfo']['user']
class UserFallowers :
	def __init__(self,nickname,token):
		def Fallowers(nickname):
			url = "https://tiktok.p.rapidapi.com/live/user/follower/list"

			querystring = {"username":nickname,"max_cursor":"0","limit":"40"}

			headers = {
				'x-rapidapi-host': "tiktok.p.rapidapi.com",
				'x-rapidapi-key': token
				}

			response = requests.request("GET", url, headers=headers, params=querystring)
			print(response.json())
			return response.json()
		self.response = Fallowers(nickname)
		self.total_followers =  self.response['total_followers']
		self.fallowers = self.response['followers']
		self.unique_id = {}
		i = -1 
		for value in self.fallowers:
			i += 1
			u = '@' + str(value["unique_id"])
			self.unique_id[value]  = u
		self.nicknames = {}
		i = -1
		for value in self.fallowers:
			i += 1
			n = value["nickname"]
			self.nicknames[value]  = n 
		self.links = {}	
		i = -1
		for value in self.fallowers:
				i += 1
				l = 'https://www.tiktok.com/@'+str(self.value["unique_id"])
				self.links[value]  = l 
class UserInfoStats :
	def __init__(self,URL):
		self.data = userInfo(URL)._userInfo_stats
		self.followingCount = self.data['followingCount']
		self.followerCount = self.data['followerCount']
		self.heartCount = self.data['heartCount']
		self.videoCount = self.data['videoCount']
		self.diggCount = self.data['diggCount']
class UserInfoUser  :
	def __init__(self,URL):
		self.data = userInfo(URL)._userInfo_user
		self.id  = self.data['id']
		self.uniqueId  = self.data['uniqueId']
		self.nickname  = self.data['nickname']
		self.avatarThumb  = self.data['avatarThumb']
		self.avatarMedium  = self.data['avatarMedium']
		self.signature  = self.data['signature']
		self.verified  = self.data['verified']
		self.secret  = self.data['secret']
		self.secUid  = self.data['secUid']
		self.openFavorite  = self.data['openFavorite']
		self.relation = self.data['relation']
class VideoInfo :
	def _VideoInfo(URL):
		for p in ProxyCreate():
			prox['http'] = p
			headers = initHeaders()
			params = {
				'url' : URL,
				}
			response = requests.get('https://www.tiktok.com/oembed?',proxies=prox,headers= headers,params=params)
			return response.json()
	def __init__(self,URL):
		self.data = _VideoInfo(URL)
		self.version = data['version']
		self.type = data['type']
		self.title = data['title']
		self.author_url = data['author_url']
		self.author_name = data['author_name']
		self.width = data['width']
		self.height = data['height']
		self.html= data['html']
		self.thumbnail_width = data['thumbnail_width']
		self.thumbnail_height = data['thumbnail_height']
		self.thumbnail_url = data['thumbnail_url']
		self.provider_url = data['provider_url']
		self.provider_name = data['provider_name']
class help:
	def help():
		print("""UserData:\nsecUid\nuserId\nisSecret\nuniqueId\nnickName\nsignature\ncovers \ncovers_0\ncovers_1\ncoversMedium\ncoversMedium_0\ncoversMedium_1\nfollowing\nfans\nheart\nvideo\nverified\ndigg\nftc\nrelation\nopenFavorite 
		\nUserInfoStats:\ndata\nfollowingCount\nfollowerCount\nheartCount\nvideoCount\ndiggCount 
		\nUserInfoUserdata\nid\nuniqueId\nnickname\navatarThumb\navatarMedium\nsignature\nverified\nsecret\nsecUid\nopenFavorite \nrelation\n
		\nVideoInfo\nversion\n type\n title\n author_url\n author_name\n width \nheight\n html\nthumbnail_width\n thumbnail_height\n thumbnail_url \nprovider_url \nprovider_name\n
		\nUserFallowers\ntotal_followers\nfallowers\nunique_id\nlinks\nnicknames""")
	def UserData():
		print('UserData:\n\nsecUid\nuserId\nisSecret\nuniqueId\nnickName\nsignature\ncovers \ncovers_0\ncovers_1\ncoversMedium\ncoversMedium_0\ncoversMedium_1\nfollowing\nfans\nheart\nvideo\nverified\ndigg\nftc\nrelation\nopenFavorite')
	def UserInfoStats():
		print('UserInfoStats:\ndata\nfollowingCount\nfollowerCount\nheartCount\nvideoCount\ndiggCount ')
	
	def UserInfoUser():
		print('UserInfoUserdata\nid\nuniqueId\nnickname\navatarThumb\navatarMedium\nsignature\nverified\nsecret\nsecUid\nopenFavorite \nrelation\n')
	def VideoInfo():
		print("\nVideoInfo\nversion\n type\n title\n author_url\n author_name\n width \nheight\n html\nthumbnail_width\n thumbnail_height\n thumbnail_url \nprovider_url \nprovider_name\n")
	def UserFallowers():
			print("UserFallowers\ntotal_followers\nfallowers\nunique_id\nlinks\nnicknames")
