# -*- coding: utf-8 -*-
import facebook
import re
import urllib2
from urlparse import urlparse

blacklists = ['facebook.com', 'www.facebook.com']

#Facebook.com login page regex
regex1='(Facebook-ში შესვლა|დამტოვეთ ხაზზე|ელ. ფოსტა ან მობილური:|<meta name="description" content="Facebook არის სოციალური სარგებლიანობა|<script src="https://fbstatic-a.akamaihd.net/rsrc.php)'

#graph api and token
graph = facebook.GraphAPI(access_token="PUT_TOKEN_HERE")

#calling all groups
groups = graph.get_object("me/groups")

for num1 in range(len(groups["data"])):

	group =  groups["data"][num1]["id"]

	group_posts = graph.get_connections(group, "feed", limit=25)

	#loop for getting all posts from group
	for num in range(len(group_posts["data"])):
	
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
							
					except urllib2.HTTPError:
					#	print "eroria simon"
						continue
						
					matches = re.findall(regex1, html_content)
					if len(matches) != 0:
   						print '\033[5;41;32mFacebook Phisher Detected\033[0m' + ' ' + url
					#uncomment for debugging
					#else:
   				#		print 'Nothing Found In:' + ' ' + url
