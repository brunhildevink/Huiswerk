import xmltodict
from collections import OrderedDict
import xml.etree.ElementTree as ET



infile = open("Artikelen.xml", "a")

content = (infile.content)
content2 = xmltodict.parse(content)