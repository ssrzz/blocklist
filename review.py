# coding=UTF-8
from twitter import *
import json 
import sys
from pprint import pprint
import urllib


def get_keysNtokens(keyFile):
        return [str(v) for (k, v) in sorted(json.load(open(keyFile, 'r')).items())]

# def getScreen
auth = "/usr/local/info/fayder.json"
t = Twitter(auth=OAuth(*get_keysNtokens(auth)))

with open('list0314.csv', 'r') as f:
	for ln in f.readlines()[:10]:
		uid = ln.strip()
		# u = t.get_user(uid)
		x = t.statuses.user_timeline(_id=uid, count=1)
		# pprint(x)
		try:
			print("|{}|{}|".format(uid, x[0]['user']['screen_name']))
		except Exception as e:
			print("|{}|{}|".format(uid, 'UNKNOWN'))

