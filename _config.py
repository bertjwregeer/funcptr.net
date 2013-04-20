# -*- coding: utf-8 -*-

## site_url -- Your site's full URL
# Your "site" is the same thing as your _site directory.
#  If you're hosting a blogofile powered site as a subdirectory of a larger
#  non-blogofile site, then you would set the site_url to the full URL
#  including that subdirectory: "http://www.yoursite.com/path/to/blogofile-dir"
site.url = "http://funcptr.net/"

site.css = "/css/"

#### Blog Settings ####
blog = controllers.blog

## blog_enabled -- Should the blog be enabled?
#  (You don't _have_ to use blogofile to build blogs)
blog.enabled = True

## blog_path -- Blog path.
#  This is the path of the blog relative to the site_url.
#  If your site_url is "http://www.yoursite.com/~ryan"
#  and you set blog_path to "/blog" your full blog URL would be
#  "http://www.yoursite.com/~ryan/blog"
#  Leave blank "" to set to the root of site_url
blog.path = ""

## blog_name -- Your Blog's name.
# This is used repeatedly in default blog templates
blog.name = "funcptr"

## blog_description -- A short one line description of the blog
# used in the RSS/Atom feeds.
blog.description = "An engineers technical notebook"

## blog_timezone -- the timezone that you normally write your blog posts from
blog.timezone = "US/Mountain"

# Disable the custom index
blog.custom_index = False

# Add another "filter"
blog.post_default_filters['md'] = 'markdown'

social = [
    {'title': "Twitter",    'alt': "Twitter: @bertjwregeer",    'url': "http://twitter.com/bertjwregeer"},
    {'title': "Flickr",     'alt': "Flickr: xistence",          'url': "http://www.flickr.com/photos/xistence/"},
    {'title': "LinkedIn",   'alt': "LinkedIn: bertjwregeer",    'url': "http://www.linkedin.com/in/bertjwregeer"},
    {'title': "Hacker News",'alt': "Hacker News: X-Istence",    'url': "http://news.ycombinator.com/user?id=X-Istence" },
    {'title': "BitBucket",  'alt': "Bitbucket: xistence",       'url': "http://code.bertjwregeer.com/" },
    {'title': "Github",     'alt': "Github: bertjwregeer",      'url': "https://github.com/bertjwregeer" },
    {'title': "Google+",    'alt': "Google+: Bert JW Regeer",   'url': "https://plus.google.com/113979921696834019350" },
]

