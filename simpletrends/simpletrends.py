from instagram.client import InstagramAPI

SUPPORTED_FORMATS = ['json']

class SimpleTrends(): 

	access_token = "3463673370.9d470f7.5ef8019afecd446eaf7b74c410596676"
	client_secret = "d9520b95d70249d49ac8c0539fdf030c"
	api = InstagramAPI(access_token=access_token, client_secret=client_secret)

	def __init__(self, *args, **kwargs):
		format = kwargs.get('format', 'json')
		if format in SUPPORTED_FORMATS:
			self.format = format
		else:
			raise Exception("Unsupported format")
		super(SimpleTrends, self).__init__(**kwargs)

	def getRecentTags():
		# 1. WORKING
		# example for searching users
		#user_search = api.user_search(q="mboyanna", count=10)
		#print(user_search)


		# 2. BROKEN
		# expecting json but the instagram API returns HTML
		# example for searching media, 
		#recent_media, next_ = api.user_recent_media(user_id="mboyanna", count=10)
		#for media in recent_media:
		#    print(media.caption.text)
		#print(recent_media)

		# 3. 
		# search for the given tag
		#recent_tags = api.tag_recent_media(tag_name="urbandecay", count=10)
		# need [user][username] ; [createdtime] ; [pagination][min_tag_id]
		#for tag in recent_tags.data:
		#	print(tag.username)
		#	print(tag.createdtime)
		#print(recent_tags.pagination.min_tag_id)
		#print (recent_tags)

		# 4. 
		# search for the given tag
		all_recent_tags, next_ = api.tag_recent_media(count=10, max_tag_id="AQCaI3nzZh7G7_jRcBHkxjtO5bSc33R7PVsU0Dpvfh54p4AVfdfkOW2wk8_EG5o4ZJgZ589JMuwbBOKxR7aVq_dFR6WUWf0u4mE4nJZDf1uv1g", tag_name="urbandecay")
		print (all_recent_tags)
		# while next_
		# 	recent_tags,next_ = api.tag_recent_media(count=10, max_tag_id="AQCaI3nzZh7G7_jRcBHkxjtO5bSc33R7PVsU0Dpvfh54p4AVfdfkOW2wk8_EG5o4ZJgZ589JMuwbBOKxR7aVq_dFR6WUWf0u4mE4nJZDf1uv1g", tag_name="urbandecay", with_next_url=next_)
		# 	all_recent_tags.extend(recent_tags)



	
