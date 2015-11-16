#Tyler Brown and Kollin Schalhamer
#CIS-125
#Assignment Week 9- Anagrams

def sortString(aString):
	myList = list(aString)
	myList.sort()
	sortedString = ''.join(myList)
	return sortedString

def createDictionary(fileName ,aDict):
	fileName = open("wordList.txt", "r")
	for line in fileName: #loop through each line in the wordlist
		word = line.strip()
		word = line.lower()
		if word[0] == 'v': #check for v start words
			sortedWord = sortString(word)
			aDict[sortedWord] = word
	fileName.close()

def findAnagrams(filename, dictionary):
	fileName = open(filename, "r")
	for line in fileName: #loop through quizwords
		line = line.strip()
		quizword = line.lower()
		print(quizword, dictionary[sortString(quizword)]) #print anagrams and quizwords
	fileName.close()

def main():
	aDict = {}
	filename = 'wordList.txt'
	quizListName = 'quizwords.txt'
	createDictionary(filename, aDict)
	findAnagrams(quizListName, aDict)

if __name__ == "__main__":
	main()