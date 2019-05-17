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
	to_be_blocked_accounts = [uid.strip() for uid in accounts if uid.strip() not in posted]		

	for idx, uid in enumerate(to_be_blocked_accounts):
		try:
			x = t.statuses.user_timeline(_id=uid, count=1)			
			print("[{:<3}/{:>3}] \t {:<30} {}".format(idx + 1, len(to_be_blocked_accounts), uid, x[0]['user']['screen_name']))

			new_item = "|{}|{}|\n".format(uid, x[0]['user']['screen_name'])
			if new_item not in readme:
				readme.append(new_item)
				f = open('README.md', 'w')
				f.write(''.join(readme))

			posted[uid] = True
			json.dump(posted, open('posted.json', 'w'), indent=2)
		except Exception as e:
			print("|{}|{}|".format(uid, 'UNKNOWN'))

