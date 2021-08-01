"""Code snippets vol-45-snippet-221
https://gist.github.com/steveshambles/258732eef0ccdaae773aedb017893a7c

By Steve Shambles
March 2020
stevepython.wordpress.com

Download all snippets so far:
https://wp.me/Pa5TU8-1yg

Note: insert a 1 second delay if required,
as code can only make 1 max unique filename a second.
"""
from datetime import datetime

# Create unique filename using current date and time.
file_name = (datetime.now().strftime
             (r'%d'+('-')+'%b'+('-')+'%Y'+('-')+'%H'+('.')
              +'%M'+('-')+'%S'+'s'))+'.jpg'

# Example name.
print(file_name)

# > 17-Mar-2020-05.36-52s.jpg
