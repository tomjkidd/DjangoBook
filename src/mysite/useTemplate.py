'''
Created on Mar 26, 2012

@author: tkidd
'''
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

from django import template
def simple():
    t = template.Template("My name is {{ name }}")
    c = template.Context({'name':'Tom'})
    c2 = template.Context({'name':'Optimus Prime'})
    print t.render(c)
    print t.render(c2)

def testIf():
    t = template.Template("Did you eat my cookie, {{name}}? {% if ate %}Bastard!{% else %}I'm on to you...{% endif %}")
    c = template.Context({"name":"Fred","ate":True})
    c2 = template.Context({"name":"Allen","ate":False})
    print t.render(c)
    print t.render(c2)
    
if __name__=="__main__":
    simple()
    testIf()