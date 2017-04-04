# simpletrends

A Python 3 client for tracking simple trends on Instagram

Installation
---
* Setup Python virtual environment
```
$ virtualenv venv
$ source venv/bin/activate
```
* Clone this repository https://github.com/mboyanna/simpletrends.git
* Clone python-instagram repository from https://github.com/mboyanna/python-instagram.git (Note: this a fork of the Instagram/Facebook provided client). 
* Install the python packages:
```
$ pip install -e python-instagram
$ pip install -e simpletrends
```

Requires
---
Software versions supported
* Instagram Developer API v1
* Python 3


Run example
-----
To run the examples where we retrieve all usernames for users who posted with hashtag #urbandecay in the last 90 days, and in the last 2 days:
```
$ python simpletrends/sample_app.py
```

### Using the programmatic client

Client currently supports only one API which can be used to retrieve handles for all users for a hashtag 'h' in the last 'n' days like so:
```
all_recent_posts_for_tag(days_old=n, hashtag=h)
```
Note: Depending on the client setting for 'with_debug_logging', this call will return just usernames, or usernames together with timestamps of the posts they made. sample_app.py contains example of how to use this programmatic client. This is how to make the call in your Python program: 
```
def _call_example(self):
	...
	if params.with_debug_logging:
		all_usernames, all_posts = self.all_recent_posts_for_tag(self, days_old=2, hashtag="urbandecay")
	else:
		all_usernames = self.all_recent_posts_for_tag(self, days_old=2, hashtag="urbandecay")
```
This client supports parameters which are described in the Setup section below, under "Application settings"


### Limitations

Memory:  
With debug logging option turned on, this client requires lots of memory to run. When collecting handles for a very popular hashtag, unless running on a computer with large memory, turn the debug logging off in params.py as explained under Application Settings paragraph in Setup section below. 

Speed:  
This client first collects all data and then returns results. For a very popular hashtag and with very small settings for batch sizes, this may take more than a ~sec. In the next version, this client can be developed to do a 'trickle' runs, meaning that it can keep pushing the results as they come out rather than in one fell swoop at the end. 



Setup 
-----

To use this client beyond provided examples, you'll need to use your own Instagram account and complete the steps in this section. For further explanations on concepts mentioned in this section, or how to further adjust the client please read section "Background" all the way down.

### Prerequisites
* Instagram account
* URI that can receive redirects by Instagram in the form of ```http://your-redirect-uri?code=CODE```

### Setting up new programmatic client w Instagram/Facebook
Every programmatic client has to be registered as a new client on the Instagram web site http://instagram.com/developer ("Manage Clients" gear icon in the upper right corner). The registration process requires that you also provide URI for redirect from Instagram like described in the prerequisites.

### Acquiring access token from Instagram
Current sample application is already setup with an access token for one sample account, but to use this client you'll need to setup your own. Instructions are in https://www.instagram.com/developer/authentication/

### Getting access to full Instagram firehose: sandbox and going live
There are two modes available for clients of Instagram: sandbox and live mode. A new client will automatically be put in sandbox mode which means it'll be restricted to a limited number of users and their posts. This is great for developing and testing your app. Once the client is tested in the sandbox, it needs to transition to live mode or to 'go live' to be able to see all posts. Instructions how to go live are in 'Going live on Instagram' section below.

### Sandbox limitations on Instagram
Sandbox is initially limited to only the posts made by it's own user account. It can be extended to include other user's posts to the extent that other users are invited and accept participation in the Sandbox. Instagram provides a way to set that up on the developers site, currently under "Sandbox Invites" gear in the upper right corner.

### Going live on Instagram
To go live, the programmatic client needs to get permission from Instagram. Follow the steps in "Manage Clients" section of Instagram's site for developers, usually under 'Permissions'. 

### To use this client in your python programs
Ensure all Setup steps are completed
Adjust application settings as described in 'Application settings' section

### Application settings
Programmatic client comes with some presets out of box. These are good only to run as examples. To use this client in your applications, adjust the following entries in params.py file: 
* access_token
	This is your Instagram security token tied to your unique Instagram account and client you register with instagram. Details on how to obtain it are in https://www.instagram.com/developer/authentication/
* client_secret
	This is your Instagram client specific secret key. Details on how to obtain it are in https://www.instagram.com/developer/authentication/
* batch_size
	Useful if hitting rate limiting constraints, controls number of posts per request to be retrieved at one time, currently set at 10
* burst_size
  	Useful if hitting rate limiting constraints, controls number of requests to Instagram API before sleeping 
* sleep_time
 	Useful if hitting rate limiting constraints, controls duration of sleep 
* with_debug_logging
	Determines whether you'll be seeing verbose logging output tracking progress of the program. Similar to DEBUG level of tracing used in slog4j in Java 
* instagram_api
	Dont change this parameter - it is tied to how Instagram developer api v1 works 

Background
-----

### Information available from Instagram
There are many types of data that can be retrieved from Instagram programmatically based on different criteria such as for example specific hashtags, or specific number of posts or some combination of such criteria. The types of data and criteria available to programmatic clients is defined in developer API by Instagram. 

### Need for programmatic client for Instagram
While developer API us useful, the data coming from Instagram 'out of box' is of limited use unless further combined programmatically to create information. For example, Instagram can only return data for the past n posts for the given tag together with some supporting information and if there is a need to get all posts that are newer than a certain date, a programmatic client is necessary to implement that. 

### Developer API
Instagram (and Facebook) maintain a developer API which changes from time to time. This client is tied to specific version of developer API, and needs to be changed when the developer API changes. In this implementation we support the Instagram API v1 and a few ways to retrieve information. Some of the ways are listed below. There are building blocks available for implementing many more ways.

### Security and client mode limitations
The actual concrete information retrieved by the programmatic client, will be limited by client's mode on Instagram and security policy. To be able to interact with Instagram at all the client first has to acquire security token. To be able to get all data available from all users on Instagram, the client will have to be in "live" mode.  Sections below describe how to do it.

### Rate limiting
Instagram has introduced rate limiting to prevent some clients for dominating it's full bandwidth. The programmatic client was built to handle that by allowing the user to adjust settings and restart the  client. The settings are:
* number of repetitive calls made one after another
* posts retrieved per call 
* sleep intervals in between bursts of repetitive calls
Details on how to adjust these settings are explained in the section for Application Settings


