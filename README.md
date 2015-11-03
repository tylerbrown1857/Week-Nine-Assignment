# Week-Nine-Assignment
Labs for week 9

Lab I
Earlier in class, we counted the frequency of words in a ﬁle using the
Gettysburg Address as an example. Let’s build on this work to do even more ﬁle analysis,
by comparing the words used in two different ﬁles to see what that might tell us about the
documents. We will use sets to discover properties such as the common words, the number
of unique words used by both, and the number of unique words used in each document.
For this example, we will continue to use the Gettysburg Address and compare its contents
to the Declaration of Independence.

Here is the list of functions we will use.  Some of them may be familiar from the pig latin modules:  

**add_word:**  Add each word in the document to its own set.  Also, we will limit the set to only words longer than 3 characters.  Note that this function does not return anything. This is because a set, like a list, is a reference pointer.  We can change the data inside the parameter, and it will change the data in the underlying collection.  

**process_line:**  This function takes 2 parameters, a line string and a word set.  We need to strip off the punctuation and remove the dashes -- from each line. This function does not return anything.  

**pretty_print:**  The parameters are the two sets. No return value.  

**main:**  We will use a main function along with the helper call.  We need to open each file and call *process_line* on each line.  When finished, call *pretty_print* and print the results from the two sets.

I have filled out some of the code for you. Look at the file comparedocs.py for the notes on where you need to supply the code. 

