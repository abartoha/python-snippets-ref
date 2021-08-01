'''
144-Get current Windows user
https://old.reddit.com/r/learnpython/comments/cv5rfm/pulling_current_windows_user_account/
'''
import getpass
checkuser = getpass.getuser()
print("The user currently logged in is: " + checkuser)
