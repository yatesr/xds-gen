#!/usr/bin/env python 
# Usage: gen-xds.py
# This will use a sample xds message at message.xml.j2 and generate the correct matching
# and unique uuids for a valid message and metadata
# Extra moudles needed: jinja2

import io
import os
import uuid
import jinja2
import time

# Functions
def randomUuid():
	return "urn:uuid:%s" % uuid.uuid4()

## Vars
datetimeStamp = time.strftime('%Y-%m-%dT%H:%M:%S')
fileName = "xdsmessage-" + datetimeStamp + ".txt"

# Matching uuid vars
matchUuid1 = randomUuid()
matchUuid2 = randomUuid()
matchUuid3 = randomUuid()

# init jinja2 message template
templateLoader = jinja2.FileSystemLoader( searchpath="." )
templateEnv = jinja2.Environment( loader=templateLoader )
TEMPLATE_FILE = "message.xml.j2"
template = templateEnv.get_template( TEMPLATE_FILE )
templateEnv.globals['randomUuid'] = randomUuid

# define template vars
templateVars = { "matchUuid1" : matchUuid1,
		 "matchUuid2" : matchUuid2,
		 "matchUuid3" : matchUuid3 }

# Render message with jinja2
messageOut = template.render(templateVars)

# Write message to file
f = io.open(fileName, 'w', encoding='utf8')
f.write(messageOut)

print ("Message output to file: " + fileName)
