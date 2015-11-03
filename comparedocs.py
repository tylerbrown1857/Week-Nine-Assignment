import string

def add_word(word, word_set):
    '''Add the word to the set. No word smaller than length 3.'''
    

def process_line(line, word_set):
    '''Process the line to get lowercase words to be added to the set.'''
    # Strip the line
    
    # Split the line into word_list

	
    for word in word_list:
        # ignore the '--' that is in the file
        if word != '--':
            # strip the word 
            
            # get commas, periods and other punctuation out as well
            word = word.strip(string.punctuation)
            
            # convert the word to lower case
            
            # add the word to the word_set
            
            
def pretty_print(ga_set, doi_set):
    '''print some stats about the two sets'''
    print('Count of unique words of length 4 or greater')
    print('Gettysburg Addr: {}, Decl of Ind: {}\n'.format(len(ga_set),len(doi_set)))
    print('{:15s} {:15s}'.format('Operation', 'Count'))
    print('-'*35)
    print('{:15s} {:15d}'.format('Union', len(ga_set.union(doi_set))))
    print('{:15s} {:15d}'.format('Intersection', len(ga_set.intersection(doi_set))))
    print('{:15s} {:15d}'.format('Sym Diff', len(ga_set.symmetric_difference(doi_set))))
    print('{:15s} {:15d}'.format('GA-DoI', len(ga_set.difference(doi_set))))
    print('{:15s} {:15d}'.format('DoI-GA', len(doi_set.difference(ga_set))))
    
    # list the intersection words, 5 to a line, alphabetical order
    
    intersection_set = ga_set.intersection(doi_set)
    word_list = list(intersection_set)
    word_list.sort()
    print('\n Common words to both')
    print('-'*20)

	# Add a comment here that shows you understand what is going on with the next 6 lines
	
    count = 0
    for w in word_list:
        if count % 5 == 0:
            print()
        print('{:13s}'.format(w), end=' ')
        count += 1

def main ():
    '''Compare the Gettysburg Address and the Declaration of Independence.'''

	# Create blank sets
    gettysburg_address_set = set()
    declaration_of_independence_set = set()

	# create a gettysburg_file from gettysburg.txt
	
	# create a declaration_independence_file from declOfInd.txt
	
	# loop through each line in gettysburg_file and call process_line with the 
	# gettysburg_address_set
	
	# loop through each line in declaration_independence_file and call process_line with the
	# declaration_of_independence_set
	
	# call pretty_print, passing it the gettysburg_address_set and the declaration_of_independence_set sets
	