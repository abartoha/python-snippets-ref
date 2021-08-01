""""Code snippets vol-49-snippet-244
    Clean string to use as a filename.

Download all snippets so far:
https://wp.me/Pa5TU8-1yg

Blog: stevepython.wordpress.com

requirements:None

origin:
https://gist.github.com/wassname/1393c4a57cfcbf03641dbc31886123b8
"""
import unicodedata
import string

valid_filename_chars = '-_.() %s%s' % (string.ascii_letters, string.digits)
char_limit = 255

def clean_filename(filename, whitelist=valid_filename_chars, replace=' '):
    """Clean file."""
    print('Before: ', filename) 
    # replace spaces.
    for r in replace:
        filename = filename.replace(r, '_')

    # keep only valid ascii chars.
    cleaned_filename = unicodedata.normalize('NFKD', filename).encode('ASCII', 'ignore').decode()

    # keep only whitelisted chars.
    cleaned_filename = ''.join(c for c in cleaned_filename if c in whitelist)
    if len(cleaned_filename) > char_limit:
        print('Warning, filename truncated because it was over {}. '
              'Filenames may no longer be unique'.format(char_limit))
    print('After cleaning: ', cleaned_filename)
    return cleaned_filename[:char_limit]

clean_filename('fa_/\[]}{}|~`"\':;,/? abcABC 0123 !@#$%^&*()_+ cl!zip')
