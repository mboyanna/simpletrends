from instagram.client import InstagramAPI
from instagram.helper import timestamp_to_datetime
from datetime import datetime, timedelta, date, time


class SimpleTrends(): 

	access_token = "3463673370.9d470f7.5ef8019afecd446eaf7b74c410596676"
	client_secret = "d9520b95d70249d49ac8c0539fdf030c"
	api = InstagramAPI(access_token=access_token, client_secret=client_secret)

	def __init__(self, *args, **kwargs):
		super(SimpleTrends, self).__init__(**kwargs)

	def getRecentTags():
		# 1. WORKING
		# example for searching users
		#user_search = api.user_search(q="mboyanna", count=10)
		#print(user_search)

		# 4. 
		# search for the given tag
		all_recent_tags, next_ = api.tag_recent_media(count=10, max_tag_id="AQCaI3nzZh7G7_jRcBHkxjtO5bSc33R7PVsU0Dpvfh54p4AVfdfkOW2wk8_EG5o4ZJgZ589JMuwbBOKxR7aVq_dFR6WUWf0u4mE4nJZDf1uv1g", tag_name="urbandecay")
		print (all_recent_tags)
		# while next_
		# 	recent_tags,next_ = api.tag_recent_media(count=10, max_tag_id="AQCaI3nzZh7G7_jRcBHkxjtO5bSc33R7PVsU0Dpvfh54p4AVfdfkOW2wk8_EG5o4ZJgZ589JMuwbBOKxR7aVq_dFR6WUWf0u4mE4nJZDf1uv1g", tag_name="urbandecay", with_next_url=next_)
		# 	all_recent_tags.extend(recent_tags)

		return

	access_token = "3463673370.9d470f7.5ef8019afecd446eaf7b74c410596676"
	client_secret = "d9520b95d70249d49ac8c0539fdf030c"
	cutoff_date = datetime.utcnow() - timedelta(days=2)
	print("Cutoff date [UTC]: ", cutoff_date)

	api = InstagramAPI(access_token=access_token, client_secret=client_secret)

	final=[]
	all_recent_posts, next_ = api.tag_recent_media_crawl_tag(count=2, tag_name="urbandecay", pagination_format='next_min_tag_id')
	final.extend (filter(lambda a_post, cutoff_date=cutoff_date : (a_post.created_time > cutoff_date), all_recent_posts))

	while next_:
		recent_posts,next_ = api.tag_recent_media_crawl_tag(count=2, tag_name="urbandecay", pagination_format='next_min_tag_id',max_tag_id=next_)
		all_recent_posts.extend(recent_posts[1:])
		final.extend( filter(lambda a_post, cutoff_date=cutoff_date : (a_post.created_time > cutoff_date), recent_posts[1:]) )

	print("All")
	for a_post in all_recent_posts:
		print(a_post.user.username, a_post.created_time, sep=' at ')

	print("Newer than cutoff date")
	for a_post in final:
		print(a_post.user.username, a_post.created_time, sep=' at ')


