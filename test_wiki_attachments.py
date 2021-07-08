#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#        Copyright (c) IRAP CNRS
#        Odile Coeur-Joly, Toulouse, France
#
"""
This part tests Redmine server access.
"""
# To disable Insecure Request Warnings, in case of requests={'verify': False} is used
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# from redminelib import Redmine
# redmine = Redmine('http://127.0.0.1:82/redmine', key = '5dea73303c7b0899ea3af513df628382043375f5')
# p1 = redmine.project.get('test_ocj')
# print(p1.issues[0])


"""
This part tests howto retrieve a Redmine Wiki page.
"""
# Connect to the XIFU Redmine site in production and get one page
from redminelib import Redmine
redmine = Redmine('https://xifu-redmine.irap.omp.eu', key = '445795a91e0c88948dc333817d8e59492fc0a4bc', requests={'verify': False})

wiki_page = redmine.wiki_page.get('20200226_135406__DACBIAS-10_DACFBCK-11_pix-10_fast', project_id='DRE')    
#wiki_page = redmine.wiki_page.get('Headers', project_id='DRE')    

print("wiki = ", wiki_page)
# To see all attributes names of the wiki_page
print("dir wiki ", dir(wiki_page))
print(" list wiki ",list(wiki_page))

# Attachment can be accessed only by its ID
print("len attach = ", len(wiki_page.attachments))
print("list attach = ",list(wiki_page.attachments))

# Attributes of the Attachment object
print("id = ", wiki_page.attachments[0].id)
print("filename = ", wiki_page.attachments[0].filename)
print("description = ", wiki_page.attachments[0].description)
print("content_type = ", wiki_page.attachments[0].content_type)

# Get the Text of the Wiki page
text_xifu = wiki_page.text
# print("text = ",wiki_page.text)

# Download all the attachment files
import os.path
normpath = os.path.normpath("C:/Users/Odile/Pictures")
savepath = os.path.join(normpath, "REDMINE", "DOWNLOAD")

# Get attachment by its ID, and download all attachments
for i in range(len(wiki_page.attachments)):
    attach_id = wiki_page.attachments[i].id
    attachment = redmine.attachment.get(attach_id)
    filepath = attachment.download(savepath)
#     print(filepath)

"""
This part tests howto create a Redmine Wiki page, from the one retrieved just above
"""
# Prepare a list of attchments to join to the new Wiki page created
filelist = os.listdir(savepath)
uploadlist = []

index = 0
for fi in filelist:
    uploadict = {}
    uploadict['path'] = os.path.join(savepath, fi)
    uploadict['filename'] = fi
    uploadict['description'] = "desc"
    uploadlist.append(uploadict)

# Connect to the dummy site and create the full new Wiki page
redmine = Redmine('http://127.0.0.1:82/redmine', key = '5dea73303c7b0899ea3af513df628382043375f5')

redmine.wiki_page.create(
                        project_id='test_ocj',
                        title='20200226_135406__DACBIAS-10_DACFBCK-11_pix-10_fast',
                        text=text_xifu,
                        parent_title='05 Tools',
                        comments='no comment',
                        uploads=uploadlist
                        )

print("page created...")

"""
This part tests howto delete a Redmine Wiki page
"""
# redmine.wiki_page.delete('test_create', project_id='test_ocj')

# Check that image has been downloaded by displaying it
# from PIL import Image
# image = Image.open(filepath)
# image.show()
