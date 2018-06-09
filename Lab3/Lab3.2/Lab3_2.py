# Lab3_2
import io
import re
import time
time_start = time.clock()

punctuation = [',', '-', '"', "'", '*', '_', '\n']
end_of_sentence = ['.', '!', '?']

"""
Taks file number and reads the whle file. Returns it as a string.
"""
def read_file(nr):
	if nr < 10:
		f = open('0' + str(nr) + '.txt', 'r')
	else:
		f = open(str(nr) + '.txt', 'r')
	return f.read()


"""
Takes a text as a string. 
Checks every character, removes special characters and lowers letters.
Gets one sentence per row.
Returns the clean text.
"""
def clean_text(text):
	clean = ""
	sen = ""
	for i in range(0, len(text)):
		if text[i] == '.' and text[i+1].isalpha():
			pass
		elif text[i] in end_of_sentence:
			clean += '\n' + sen
			sen = ""
		elif text[i] in punctuation:
			sen += ' '
		elif text[i].isupper():
			sen += text[i].lower()
		else: # text[i] is lower and alpha or space
			sen += text[i]
	return clean


"""
Takes a text as a string.
Removes extra spaces and new lines. 
Returns the clean text.
"""
def remove_space(text):
	fixed1 = re.sub(' +', ' ', text) #Remove multiple white spaces
	fixed2 = re.sub('\n+', '\n', fixed1) #Remove multiple new lines
	fixed3 = re.sub('\n ', '\n', fixed2) #Remove white space after new line
	return fixed3 

"""
Takes a clean text as a string.
Generates a table of all sentences as key.
Returns the table.
"""
def generate_table(text):
	table = {}
	buf = io.StringIO(text)
	for line in buf:
		if line[:-1] != '':
			table[line[:-1]] = 1
		else:
			pass#print(line)
	return table

#print(generate_table(remove_space(clean_text(text))))

"""
Returns a list of tables for all files.
"""
def get_all_tables():
	tables = []
	for i in range(1,11):
		tables.append(generate_table(remove_space(clean_text(read_file(i)))))
	return tables

"""
Takes a number.
Compares that number of text with all the other texts.
"""
def compare_one_to_all(one):
	print("Comparing text nr " + str(one) + " with all other texts.")
	tables = get_all_tables() # From 0 to 9
	#print(len(tables)) # 10

	#Extract the text we want to compare 
	text = tables[one-1].keys()

	#aaa = [(i,x) for i, x in enumerate(tables) if i != one-1]
	#print(len(aaa))

	for sentence in text:
		for i, table in enumerate(tables):
			if i == one-1:
				pass
			else:
				if sentence in table.keys() and len(sentence) > 20:
					#print("\nPlagiat! Sentence:")
					print("In both text nr", i+1, "and nr", one, ":")
					print(sentence)
					
	return
	
for i in range(1,11):
	print(compare_one_to_all(i))

time_elapsed = (time.clock() - time_start)
print("Time:", time_elapsed, "seconds")


	
	
	