import sys
from instagram.client import InstagramAPI
from instagram.helper import timestamp_to_datetime
from datetime import datetime, timedelta, date, time
import time


access_token = "3463673370.9d470f7.5ef8019afecd446eaf7b74c410596676"
client_secret = "d9520b95d70249d49ac8c0539fdf030c"
cutoff_date = datetime.utcnow() - timedelta(days=2)
print("Cutoff date [UTC]: ", cutoff_date)

api = InstagramAPI(access_token=access_token, client_secret=client_secret)

final=[]
all_recent_posts, next_ = api.tag_recent_media_crawl_tag(count=2, tag_name="urbandecay", pagination_format='next_min_tag_id', scope='public_content')
final.extend (filter(lambda a_post, cutoff_date=cutoff_date : (a_post.created_time > cutoff_date), all_recent_posts))

while next_:
	recent_posts,next_ = api.tag_recent_media_crawl_tag(count=2, tag_name="urbandecay", pagination_format='next_min_tag_id',max_tag_id=next_, scope='public_content')
	all_recent_posts.extend(recent_posts[1:])
	final.extend( filter(lambda a_post, cutoff_date=cutoff_date : (a_post.created_time > cutoff_date), recent_posts[1:]) )

print("All")
for a_post in all_recent_posts:
	print(a_post.user.username, a_post.created_time, a_post.post_text, sep=' at ')

print("Newer than cutoff date")
for a_post in final:
	print(a_post.user.username, a_post.created_time, a_post.post_text, sep=' at ')
