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

posted = json.load(open('posted.json', 'r'))
readme = open('README.md', 'r').readlines()

with open('blocklist.csv', 'r') as f:
	accounts = f.readlines()
	readme[10] = "{} blocked Twitter ad-accounts (accounts promoted by Twitter Ads Platform).\n".format(len(accounts))

	for ln in accounts:
		uid = ln.strip()
		if uid in posted: continue
		posted[uid] = True
	
		try:
			x = t.statuses.user_timeline(_id=uid, count=1)			
			print("|{}|{}|".format(uid, x[0]['user']['screen_name']))

			readme.append("|{}|{}|\n".format(uid, x[0]['user']['screen_name']))
			json.dump(posted, open('posted.json', 'w'), indent=2)
			f = open('README.md', 'w')
			f.write(''.join(readme))
		except Exception as e:
			print("|{}|{}|".format(uid, 'UNKNOWN'))

