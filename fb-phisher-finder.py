# -*- coding: utf-8 -*-
import facebook
import re
import urllib2
from urlparse import urlparse
import time

token = raw_input("Enter ACCESS TOKEN ")
#print token
blacklists = ['mymarket.ge', 'myauto.ge', 'facebook.com', 'www.facebook.com', 'youtube.com', 'www.youtube.com', 'myvideo.ge', 'www.myvideo.ge']

#Facebook.com login page regex
regex1='(i.imgur.com/XAYsHvZ.jpg|Facebook-ში შესვლა|დამტოვეთ ხაზზე|ელ. ფოსტა ან მობილური:|<meta name="description" content="Facebook არის სოციალური სარგებლიანობა|fbstatic-a.akamaihd.net/rsrc.php|http://www.picz.ge/img/s1/1503/3/8/84fd4c9d1cbc.png)'

#graphapi and token
graph =  facebook.GraphAPI(access_token=token)

#Group post starting number
num="0"

#URL starting number
url="0"



groups = graph.get_object("me/groups")

for num1 in range(len(groups["data"])):

	group =  groups["data"][num1]["id"]
	#calling the group feed
	try:
		group_posts = graph.get_connections(group, "feed", limit=30)
		time.sleep(1)
	except:
		continue

	#loop for getting all posts from group
	for num in range(len(group_posts["data"])):
#		time.sleep(2)
		#regexp for finding URLs
		try:
			match = re.findall('https?://[^\s<>"]+|www\.[^\s<>"]+', group_posts["data"][num]["message"])
		except KeyError:
			continue	
		if match:
			
			for url in match:
				url2 = urlparse(url)
				url2 = url2.netloc
					
				if url2 not in blacklists:
					try:
						
						html_content = urllib2.urlopen(url).read()
							
					except:
#						print "eroria simon"
						continue
						
					matches = re.findall(regex1, html_content)
					if len(matches) != 0:
   						print '\033[5;41;32mFacebook Phisher Detected\033[0m' + ' ' + url
					#uncomment for debugging
					else:
   						print 'Nothing Found In:' + ' ' + url
