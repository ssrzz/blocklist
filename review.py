# coding=UTF-8
from twitter import *
import json 
import sys
from pprint import pprint
import urllib


def get_keysNtokens(keyFile):
        return [str(v) for (k, v) in sorted(json.load(open(keyFile, 'r')).items())]

auth = "/usr/local/info/fayder.json"
t = Twitter(auth=OAuth(*get_keysNtokens(auth)))
breakpoint = True
posted = json.load(open('posted.json', 'r'))
pprint(posted)

with open('blocklist.csv', 'r') as f:
	for ln in f.readlines():
		uid = ln.strip()
		if uid in posted: continue
		posted[uid] = True
		try:
			x = t.statuses.user_timeline(_id=uid, count=1)			
			print("|{}|{}|".format(uid, x[0]['user']['screen_name']))
		except Exception as e:
			print("|{}|{}|".format(uid, 'UNKNOWN'))
	json.dump(posted, open('posted.json', 'w'), indent=2)

