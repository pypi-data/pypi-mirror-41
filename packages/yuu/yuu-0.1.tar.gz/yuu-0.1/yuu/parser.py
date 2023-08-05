import hmac
import hashlib
import struct
import time
import uuid
import requests
import m3u8
from bs4 import BeautifulSoup as Soup

from base64 import urlsafe_b64encode
from binascii import unhexlify
from Crypto.Cipher import AES

from .common import STRTABLE, HKEY, _MEDIATOKEN_API, _LICENSE_API, _USERAPI, _KEYPARAMS, _M3U8HEADLINK, yuuError

def getAuthToken(proxy):
	def keySecret(devid):
		SECRETKEY = (b"v+Gjs=25Aw5erR!J8ZuvRrCx*rGswhB&qdHd_SYerEWdU&a?3DzN9B"
					b"Rbp5KwY4hEmcj5#fykMjJ=AuWz5GSMY-d@H7DMEh3M@9n2G552Us$$"
					b"k9cD=3TxwWe86!x#Zyhe")
		deviceid = devid.encode("utf-8")
		ts_1hour = (int(time.time()) + 60 * 60) // 3600 * 3600
		time_struct = time.gmtime(ts_1hour)
		ts_1hour_str = str(ts_1hour).encode("utf-8")
		
		h = hmac.new(SECRETKEY, digestmod=hashlib.sha256)
		h.update(SECRETKEY)
		tmp = h.digest()
		
		for i in range(time_struct.tm_mon):
			h = hmac.new(SECRETKEY, digestmod=hashlib.sha256)
			h.update(tmp)
			tmp = h.digest()
		h = hmac.new(SECRETKEY, digestmod=hashlib.sha256)
		h.update(urlsafe_b64encode(tmp).rstrip(b"=") + deviceid)
		tmp = h.digest()
		for i in range(time_struct.tm_mday % 5):
			h = hmac.new(SECRETKEY, digestmod=hashlib.sha256)
			h.update(tmp)
			tmp = h.digest()

		h = hmac.new(SECRETKEY, digestmod=hashlib.sha256)
		h.update(urlsafe_b64encode(tmp).rstrip(b"=") + ts_1hour_str)
		tmp = h.digest()

		for i in range(time_struct.tm_hour % 5):  # utc hour
			h = hmac.new(SECRETKEY, digestmod=hashlib.sha256)
			h.update(tmp)
			tmp = h.digest()
			
		return urlsafe_b64encode(tmp).rstrip(b"=").decode("utf-8")

	deviceid = str(uuid.uuid4())
	jsonData = {"deviceId": deviceid, "applicationKeySecret": keySecret(deviceid)}
	
	if proxy:
		res = requests.post(_USERAPI, json=jsonData, proxies={'http': proxy, 'https': proxy}).json()
	else:
		res = requests.post(_USERAPI, json=jsonData).json()
	try:
		token = res['token']
	except:
		raise yuuError('Failed to get usertoken')
	
	return ['bearer ' + token, deviceid]

def fetchVideoKey(ticket=None, authToken=None, proxy=None):
	auth = {"Authorization": authToken[0]}

	if proxy:
		restoken = requests.get(_MEDIATOKEN_API, params=_KEYPARAMS, headers=auth, proxies={'http': proxy, 'https': proxy}).json()
	else:
		restoken = requests.get(_MEDIATOKEN_API, params=_KEYPARAMS, headers=auth).json()
	mediatoken = restoken['token']

	if proxy:
		gl = requests.post(_LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket}, proxies={'http': proxy, 'https': proxy}).json()
	else:
		gl = requests.post(_LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket}).json()

	cid = gl['cid']
	k = gl['k']

	res = sum([STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k))])

	encvk = struct.pack('>QQ', res >> 64, res & 0xffffffffffffffff)

	h = hmac.new(unhexlify(HKEY), (cid + authToken[1]).encode("utf-8"), digestmod=hashlib.sha256)
	enckey = h.digest()

	aes = AES.new(enckey, AES.MODE_ECB)
	vkey = aes.decrypt(encvk)
	
	return vkey

def parsem3u8(m3u8, proxy=None):
	if proxy:
		r = requests.get(m3u8, proxies={'http': proxy, 'https': proxy})
	else:
		r = requests.get(m3u8)
	x = m3u8.loads(r)
	files = x.files
	iv = x.keys[0].iv[2:]
	ticket = x.keys[0].uri[18:]
	return [files, iv, ticket]

def webparse(url, res):
	req = requests.get(url)
	soup = Soup(req.text, 'html.parser')
	title = soup.find('span', attrs={'class': 'abm_cq_m abm_cq_l abm_cq_c'}).text 
	title = title[:title.rfind(' |')]
	epnum = soup.find('h1', attrs={'class': 'com-video-EpisodeSection__title abm_cq_j abm_cq_l abm_cq_a abm_cq_c'}).text
	m3u8link = '{x}/{vid}/{r}/playlist.m3u8'.format(x=_M3U8HEADLINK, vid=url[url.rfind('/')+1:], r=res)
	return title, epnum, m3u8link