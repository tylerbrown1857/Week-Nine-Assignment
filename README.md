CIS 125, Week 9 Lab
===================

Partner
-------

You will be assigned a partner in the lab to work with on this exercise.
Two people should work at one computer. Occasionally switch the person
who is typing. Talk to each other about what you are doing and why.

The Problem, really Puzzle 
---------------------------

Here is a puzzle. This is taken directly from NPR (that’s national
public radio, the public radio station) Weekend Edition Sunday Puzzle
with Will Shortz. Shortz is a famous puzzle guy and does a puzzle once a
week for NPR. Some lucky caller is selected and Shortz and Liane Hansen
(the host) do an online quiz with the person (realtime, right there,
amazing). Look at [http://www.npr.org/templates/story/story.php?columnId=4473090](http://www.npr.org/templates/story/story.php?columnId=4473090)


Here is such a puzzle. Shortz gives you a word. You find the anagram to
that word starting with the letter ‘v’. He gives about 13 words, 1 every
15 seconds or so, and you try to come up with the word. In case you
don’t remember, an anagram is the rearrangement of a word’s letters to
make a new word. For example, ‘parental’, ‘prenatal’, and ‘paternal’ are
all anagrams of one another

Your Tasks
----------

Here are 14 words. Find an anagram of those words starting with the
letter ‘v’. Included in the directory is a wordList file of about
230,000 English words. You can use it to look up anagrams.

serve, rival, lovely, caveat, devote, irving, livery, selves, latvian,
saviour, observe, octavian, dovetail, levantine

Hints, doing it in steps
------------------------

1.  We are going to use Python’s dictionary data structure. We will
    store a key-value pair in the dictionary that we can use to solve
    our problem. Consider two anagrams we know. The words are ‘serve’
    and ‘verse’. Let’s create a string of the sorted list of the letters
    in each word. Thus ‘serve’ is transformed to ‘eersv’, the sorted
    list of its letters. Now think!!! What would ‘verse’ become under
    the same transformation? How can I use that fact to find two
    anagrams in a list of words? The **sorted letters are our ke**y in
    the dictionary

2.  How do we do this conversion? We cannot sort a string, but we can
    sort a list. So we need to:  

	a.  convert a string to a list 
	
	`myList = list('serve')`

    b.  sort the list 
    
    `myList.sort()`

    c.  turn the list back into a string  
    
    `sortedString=''.join(myList)`

      NOTE:  the join method takes the elements of a list and attempts to put them together into a string with the string before the dot placed in-between each list element. So 
      
      `':'.join(['a','b','c'])` 
      
      returns 
      
      `'a:b:c'`   
      
      But joining with an empty string just yields the joined string. Thus 
      
      `''.join(aList)`   
      
      is another idiom: one for making a string from a list of strings. 
      
      Try it: type  
       
       `''.join(['a','b','c'])` 
       
       in the Python shell.)

3. Now that we have the basics, we can start our program.  Create a new python file called lab9.py. In this file, create three functions:  

`sortString(aString)`  
`fillVWords(fileName, aDict)`  
`main()`  


The function `sortString(aString)` takes a string and returns a string with the letters in alphabetical order.  

The function `fillVWords(fileName, aDict)` takes the name of a file (wordList.txt), opens the file and reads the file one line at a time.  Each line is a single word. Strip and lowercase the word. If the first letter of the word is 'v' add it to the dictionary with the sorted letters as the key, and the actual word as the value.  e.g.  `aDict['eersv'] = 'verse' `

This function does not return anything. Remember that a dictionary, like a list, is a pointer, not a value. Therefore, any changes we make to the dictionary in the function are reflected in the actual data.  

The function `main()` should create a new dictionary, and call fillVWords to fill it up. It should then open the quizwords.txt file, read through it one line (word) at a time and print out the quiz word and its anagram that starts with V.

Make sure to close all your files before exiting the program!


