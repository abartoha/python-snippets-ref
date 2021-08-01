'''
Python Code Snippets #22
107-Display Module attributes and types

Tested on Python V3.6x, Window 7, Linux Mint 19.1

source:
https://code.activestate.com/recipes/
580705-get-names-and-types-of-all-attributes-of-a-python-/?in=user-4173351
'''

# you need to import the module you want to look at.
# In this example webbrowser
import webbrowser

def attrs_and_types(mod_name):
    print('Attributes and their types for module {}:'.format(mod_name))
    print()
    for num, attr in enumerate(dir(eval(mod_name))):
        print("{idx}: {nam:30}  {typ}".format(
            idx=str(num + 1).rjust(4),
            nam=(mod_name + '.' + attr).ljust(30),
            typ=type(eval(mod_name + '.' + attr))))

# 'webbrowser' is the modules name to be inspected,
# change the import and the module name here to try a different module.

attrs_and_types(webbrowser.__name__)
