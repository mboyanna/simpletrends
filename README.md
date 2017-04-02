# simpletrends

Client for tracking simple trends on Instagram
======

Background
-----

### Information available from Instagram
There are many types of data that can be retrieved from Instagram programmatically based on different criteria such as for example specific hashtags, or specific number of posts or some combination of such criteria. The types of data and criteria available to programmatic clients is defined in developer API by Instagram. 

### Need for programmatic client for Instagram
While developer API us useful, the data coming from Instagram 'out of box' is of limited use unless further combined programmatically to create information. For example, Instagram can only return data for the past n posts for the given tag together with some supporting information and if there is a need to get all posts that are newer than a certain date, a programmatic client is necessary to implement that. 

### Developer API
Instagram (and Facebook) maintain a developer API which changes from time to time. This client is tied to specific version of developer API, and needs to be changed when the developer API changes. In this implementation we support the Instagram API v1 and a few ways to retrieve information. Some of the ways are listed below. There are building blocks available for implementing many more ways.

### Software versions supported
This client will work only for specific versions of the components, as listed below:
* Instagram Developer API v1
* Python 3+

### Security and client mode limitations
The actual concrete information retrieved by the programmatic client, will be limited by client's mode on Instagram and security policy. To be able to interact with Instagram at all the client first has to acquire security token. To be able to get all data available from all users on Instagram, the client will have to be in "live" mode.  Sections below describe how to do it.

### Rate limiting limitations
Instagram is servicing many clients simultaneously and has a rate limiting in place to prevent some clients for dominating it's full bandwidth. The programmatic client was built to handle that by displaying appropriate message to the user and it just stops. It can be started again after such stop. 


Setup 
-----

### Prerequisites
Prerequisites for installing this client are:
* existence of a URI that can receive redirects by Instagram in the form of ```http://your-redirect-uri?code=CODE```
* python

Note: Your system needs to have the appropriate versions of software installed, see the section 'Software versions supported'

### Setting up new programmatic client w Instagram/Facebook
Every programmatic client has to be registered as a new client on the Instagram web site http://instagram.com/developer ("Manage Clients" gear icon in the upper right corner). Such registration will require that you also provide URI for redirect from Instagram that was already set up.

### Acquiring security token from Instagram
***TBD*** There are two ways to acquire it. Will well do only the ....
To get security token call the function xyz.... (which will orchestrate the whole thing)... then record security token for later.

### Getting access to full Instagram firehose: client mode and going live
There are two modes clients can be sandbox mode, and live mode. This new client will automatically be put in sandbox mode which means it'll be restricted to a limited number of users and media. This is great for developing and testing your app. 
Once the client is tested in the sandbox, it needs to acquire additional permissions to be able to see all publicly available posts. 

### Sandbox limitations on Instagram
Sandbox is initially limited to only the posts made by it's own user account. It can be extended to include other user's posts to the extent that other users are invited and accept participation in the Sandbox. Instagram provides a way to set that up on the developers site, currently under "Sandbox Invites" gear in the upper right corner.

### Going live on Instagram
To go live, the programmatic client needs to get permission from Instagram. Follow the steps in "Manage Clients" section of Instagram's site for developers, usually under 'Permissions'. 

### Installation
Clone this repository https://github.com/mboyanna/simpletrends.git
Clone python-instagram repository, it's a fork of the Instagram/Facebook provided client and it's here https://github.com/mboyanna/python-instagram.git
Install the python packages:
```
$ pip install python-instagram
$ pip install simpletrends 
```
Ensure all Setup steps are completed
Adjust application settings as described in 'Application settings' section

### Application settings
***TBD***
Programmatic client comes with some presets out of box. These are created to be able to run examples. To adjust them to run your own code, change the following entries in setup file ***TBD*** xyz 
- put security token in ...
- posts per request are to be retrieved at one time
- number of requests to Instagram API before sleeping 
- duration of sleep 

Run example
-----
***TBD***


### Using the programmatic client, api documentation

***TBD***
Get usernames of all users posts with hashtags #urbandecay from the last 30 days. 
```
    tag_recent_media_crawl_tag = bind_method(
                path="/tags/{tag_name}/media/recent",
                accepts_parameters=['count', 'max_tag_id', 'tag_name', 'max_pages'],
                root_class=Media,
                response_type='list',
                paginates=True,
                pagination_format='next_min_tag_id')
```
