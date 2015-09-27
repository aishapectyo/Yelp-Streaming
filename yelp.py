# Yelp-Streaming

#!/usr/bin/env python\

from __future__ import division
import json
import csv
from collections import Counter
import numpy as np
import requests
import oauth2
import nltk
import unicodedata
import string


def get_yelp_businesses(location, category_filter = 'restaurants'):
    # from https://github.com/Yelp/yelp-api/tree/master/v2/python
    consumer_key    = '7ZkNKBC5X-SU7OJ2vuFglA'
    consumer_secret = 'emAhY004tYwqaAlUL-sh_fw4uXQ'
    token           = 'HStkkQdl-kAmJZ2QRV5gBG-4qH-baRSf'
    token_secret    = 'qBrCwkPIU5r_wYlm5KbRm_1o5xc'

    consumer = oauth2.Consumer(consumer_key, consumer_secret)

    url = 'http://api.yelp.com/v2/search?category_filter=%s&location=%s&sort=1' % (category_filter,location)

    oauth_request = oauth2.Request('GET', url, {})
    oauth_request.update({'oauth_nonce': oauth2.generate_nonce(),
                          'oauth_timestamp': oauth2.generate_timestamp(),
                          'oauth_token': token,
                          'oauth_consumer_key': consumer_key})

    token = oauth2.Token(token, token_secret)

    oauth_request.sign_request(oauth2.SignatureMethod_HMAC_SHA1(), consumer, token)

    signed_url = oauth_request.to_url()
    resp = requests.get(url=signed_url)
    return resp.json()
zipcodes=(72712, 72757, 72756, 72762, 72765, 72703, 72714, 72715, 72701, 72702, 72745, 72770, 72761, 72764)
#ben_restaurants = get_yelp_businesses('72764')
nwa_restaurants = {}
c=[]
for zipcode in zipcodes:
        nwa_restaurants = get_yelp_businesses(zipcode)
        for business in nwa_restaurants['businesses']:
        	categories = [category[0] for category in business['categories']]
        	#print categories
        	cat_len  = len(categories)
        	for j in xrange(cat_len):
        		c.append(categories[j])


counts = Counter(c)
print counts
print(len(counts))
