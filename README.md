# TikTokPars
ТикТок парсер
Необходимые библиотеки:
pip install bs4 
pip installlxml
pip install re
pip install json

Парсит: даные о пользователе по его уникальному никнеиму unique_id, даные о видео по его ссылке.
Для использования скачаите скрипт и поместите в туже папку где будет основнойкод,для импорта из папки from TikTokPars import tiktokparser если скрипт не в папке  пишем import tiktokparser далее используем нужные методы:
Метод  UserDat принимает значенье стринг сылка на профиль пользователя
Пример:
from tiktokparser import UserDat
nickname = 'tiktok'
URL = 'https://www.tiktok.com/@' + nickname
User = UserDat(URL)
print(User.nickName)
print(User.userId)

Можно вызвать:
    _userData : возвращяет dict
		secUid : возвращяет str
		userId : возвращяет str
		isSecret : возвращяет str
		uniqueId : возвращяет str
		nickName : возвращяет str
		signature : возвращяет str
		covers : возвращяет str
		covers_0 : возвращяет str
		covers_1 : возвращяет str
		coversMedium : возвращяет str
		coversMedium_0 : возвращяет str
		coversMedium_1 : возвращяет str
		following  : возвращяет str
		fans : возвращяет str
		heart : возвращяет str
		video : возвращяет str
		verified  : возвращяет str
		digg  : возвращяет str
		ftc : возвращяет str
		relation : возвращяет str
		openFavorite : возвращяет str


Метод  UserFallowers принимает 2 значенье: 1 стринг, сылка на профиль пользователя, 2 нужен токен с сайта: https://rapidapi.com/logicbuilder/api/tiktok
Пример:
from tiktokparser import UserDatFallowers
nickname = 'tiktok'
URL = 'https://www.tiktok.com/@' + nickname
token = 'token'
Fallowers = UserFallowers(URL,token)
print(Fallowers.total_fallowers)
print(Fallowers.nicknames)

Можно вызвать:
    response : json ответ со всеми даными
    total_fallowers : int 
    unique_id : dict
    nicknames : dict
    links : dict

Метод  UserInfoStats принимает  значенье стринг сылка на профиль пользователя
Пример:
from tiktokparser import UserInfoStats
nickname = 'tiktok'
URL = 'https://www.tiktok.com/@' + nickname
User = UserFallowers(URL)
print(User.videoCount)
print(User.heartCount)

Можно вызвать:
    data : все даные которые есть  ниже в dict
		followingCount : str 
		followerCount : str
		heartCount : str
		videoCount : str
		diggCount : str


Метод  UserInfoUser принимает  значенье стринг сылка на профиль пользователя
Пример:
from tiktokparser import UserInfoUser
nickname = 'tiktok'
URL = 'https://www.tiktok.com/@' + nickname
User = UserInfoUser(URL)
print(User.id)
print(User.avatarThumb)

Можно вызвать:
    data : все даные которые есть  ниже в dict
		data : str
		id  : str
		uniqueId  : str
		nickname  : str
		avatarThumb  : str
		avatarMedium  : str
		signature : str
		verified : str
		secret  : str
		secUid  : str
		openFavorite  : str
		relation : str


Метод  VideoInfo принимает  значенье стринг сылка на video
Пример:
from tiktokparser import VideoInfo

URL = 'https://www.tiktok.com/@video'
Video = VideoInfo(URL)
print(Video.title)
print(Video.html)
Можно вызвать:
    data : все даные которые есть  ниже в dict
	  version : str
	  type : str
		title : str
		author_url : str
		author_name : str
		width : str
		height : str
		html : str
		thumbnail_width  : str
		thumbnail_height : str
		thumbnail_url : str
		provider_url : str
		provider_name : str
