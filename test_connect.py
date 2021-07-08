#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#        Copyright (c) IRAP CNRS
#        Odile Coeur-Joly, Toulouse, France
#
from IPython.core.page import page
"""
This part tests Redmine server access.
"""
from redminelib import Redmine
redmine = Redmine('http://127.0.0.1:82/redmine', key = '5dea73303c7b0899ea3af513df628382043375f5')
p1 = redmine.project.get('test_ocj')
print(p1.issues[0])

# from redminelib import Redmine
# server = Redmine('https://127.0.0.1:444/redmine', key = '5dea73303c7b0899ea3af513df628382043375f5', requests={'verify': False})
# p1 = server.project.get('test_ocj')
# print(p1.issues[0])
# 
# from redminelib import Redmine
# server = Redmine('https://xifu-redmine.irap.omp.eu', key = '445795a91e0c88948dc333817d8e59492fc0a4bc', requests={'verify': False})
# p1 = server.project.get('DRE')
# print(p1.issues[0])

"""
This part tests howto retrieve a Redmine Wiki page.
"""
wiki_page = redmine.wiki_page.get('test_read', project_id='test_ocj', include=['attachments'])

print(wiki_page)
# To see all attributes names of the wiki_page
print(dir(wiki_page))
print(list(wiki_page))

# Attachment can be accessed only by its ID
print("len = ", len(wiki_page.attachments))
print("list = ",list(wiki_page.attachments))

# Attributes of the Attachment object
print("id = ", wiki_page.attachments[0].id)
print("filename = ", wiki_page.attachments[0].filename)
print("description = ", wiki_page.attachments[0].description)
print("content_type = ", wiki_page.attachments[0].content_type)

"""
This part tests howto retrieve an attachment file of a Redmine Wiki page.
"""
# download the attachment file
# attach_id = wiki_page.attachments[0].id
# attachment = redmine.attachment.get(attach_id)
# import os.path
# savepath = os.path.join("C:", os.sep, "Users", "Odile", "Pictures")
# filepath = attachment.download(savepath, filename='toto.png')

"""
This part tests howto create a new Redmine Wiki page with an attachment file
"""
redmine.wiki_page.create(
                        project_id='test_ocj',
                        title='test_create',
                        text='h1. Essai de création h1\r\n\nh2. Essai de création h2\r\n\nBlablabla',
                        parent_title='Wiki',
                        comments='no comment',
                        uploads=[{'path' : 'C:\\Users\\Odile\\Pictures\\REDMINE\\Wiki_sidebar1.png', 'filename' : 'Wiki_sidebar1.png', 'description' : 'image1'},
                                 {'path' : 'C:\\Users\\Odile\\Pictures\\REDMINE\\Wiki_sidebar2.png', 'filename' : 'Wiki_sidebar2.png', 'description' : 'image1'}]
                        )

"""
This part tests howto delete a Redmine Wiki page
"""
# redmine.wiki_page.delete('test_create', project_id='test_ocj')

# Check that image has been downloaded by displaying it
# from PIL import Image
# image = Image.open(filepath)
# image.show()
