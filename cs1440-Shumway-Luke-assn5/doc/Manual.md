# Recursive Web Crawler User Manual

*TODO: Your instructions go here*

This program is intended to be run from the Command Line Interface. When running the program, the following inputs will be needed:
* A root URL, which must be an absolute URL in order for the program to function properly. The difference between an absolute and a relative URL is set forth below.
* A maximum depth level for web crawling. NOTE: This parameter is optional, and if not given, will default to a value of 3.

The difference between an absolute URL and a relative url is what is present at the beginning of the url. An absolute URL is one that starts with http:// or https:// (the scheme) and then followed by the www.urllocation.com (the www. is optional).
A relative URL is one that does not contain the scheme, and may or may not have the www. ... .com part either. In order to properly run the program, both the scheme and location of the url must be provided, along with a positive, integer, depth (if supplied) are required.

If an improper URL is supplied, the program will exit and inform the user that an absolute URL is required. Likewise, if an improper depth value is supplied, the program will exit and inform the user that a positive whole number is required for the depth.

Once a proper URL and depth level are supplied, the program will inform the user that crawling will commence, beginning with the root URL supplied, and continuing to the maximum depth level, whether default or supplied by the user.
Then a list of URLs will begin to be output to the screen, with varying indentation, the less indented the URL, the closer to the root the URL was found. The further indented, the more clicks needed to reach the site.
There might be some pauses while the program attempts to access the page, and some errors may be noted if the URL was unable to be reached. These errors are not indented at all, and can be picked out as such.
Upon completion of the web crawling, the program will inform the user of the number of unique URLs visited and the time taken to do so. NOTE: for a depth of 3 levels, approximately 200-400 seconds is normal, so if you desire more depth, a significant amount of time is needed.