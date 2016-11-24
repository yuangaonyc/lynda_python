# Processing JSON
import urllib2
import json

def printResults(data):
	theJSON = json.loads(data)
	if "title" in theJSON["metadata"]:
		print theJSON["metadata"]["title"]

		count = theJSON["metadata"]["count"]
		print(str(count) + " events recorded")

		for i in theJSON["features"]:
			feltReports = i["properties"]["felt"]
			if (feltReports != None) & (feltReports > 0 ):
				print("%2.1f" % i["properties"]["mag"], i["properties"]["place"], "reported " + str(feltReports) + " times")

def main():
	# retrieving content
	webUrl = urllib2.urlopen("http://facebook.com")
	# print("result code: " + str(webUrl.getcode()))
	data = webUrl.read()
	# print(data)

	# JSON data
	urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
	webUrl = urllib2.urlopen(urlData)
	print(webUrl.getcode())
	if (webUrl.getcode() == 200):
		data = webUrl.read()
		printResults(data)
	else:
		print("Received an error from server, cannot retrieve results " + str(webUrl.getcode()))

if __name__ == "__main__":
	main()






# Parsing and processing HTML
from HTMLParser import HTMLParser

metacount = 0

class MyHTMLParser(HTMLParser):

	def handle_starttag(self, tag, attrs):
		global metacount
		print("Encountered a start tag: " + str(tag))
		if tag == "meta":
			metacount +=1
		pos = self.getpos()
		print("At line: " + str(pos[0]) + " position " + str(pos[1]))
		if attrs.__len__ > 0:
			print("\tAttributes:")
			for a in attrs:
				print("\t" + str(a[0]) + "=" + str(a[1]))

	def handle_endtag(self, tag):
		print("Encountered an end tag: " + str(tag))
		pos = self.getpos()
		print("At line: " + str(pos[0]) + " position " + str(pos[1]))

	def handle_data(self, data):
		print("Encountered some data: " + str(data))
		pos = self.getpos()
		print("At line: " + str(pos[0]) + " position " + str(pos[1]))

	def handle_comment(self, data):
		print("Encountered comment: " + data)
		pos = self.getpos()
		print("At line: " + str(pos[0]) + " position " + str(pos[1]))

def main():
	parser = MyHTMLParser()
	f = open("samplehtml.html")
	if f.mode == "r":
		contents = f.read()
		parser.feed(contents)
	print("%d meta tags encountered" % metacount)

if __name__ == "__main__":
	main()






# Manipulating XML
import xml.dom.minidom

def main():
	doc = xml.dom.minidom.parse("samplexml.xml")
	print(doc.nodeName)
	print(doc.firstChild.tagName)

	skills = doc.getElementsByTagName("skill")
	print("%d skills" % skills.length)
	for skill in skills:
		print skill.getAttribute("name")

	newSkill = doc.createElement("skill")
	newSkill.setAttribute("name", "jQuery")
	doc.firstChild.appendChild(newSkill)

	skills = doc.getElementsByTagName("skill")
	print("%d skills" % skills.length)
	for skill in skills:
		print skill.getAttribute("name")

if __name__ == "__main__":
	main()


















