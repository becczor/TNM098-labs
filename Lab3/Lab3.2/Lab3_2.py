# Lab3_2
import StringIO
import re

punctuation = [',', '-', '"', "'", '*', '_', '\n']
end_of_sentence = ['.', '!', '?']

def read_file(nr):
	if nr < 10:
		f = open('0' + str(nr) + '.txt', 'r')
	else:
		f = open(str(nr) + '.txt', 'r')
	return f.read()

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

def remove_space(text):
	fixed1 = re.sub(' +', ' ', text)
	fixed2 = re.sub('\n+', '\n', fixed1)
	fixed3 = re.sub('\n ', '\n', fixed2)
	return fixed3 

def generate_table(text):
	table = {}
	buf = StringIO.StringIO(text)
	for line in buf:
		table[line[:-1]] = 1
	return table

#print(generate_table(remove_space(clean_text(text))))

def get_all_tables():
	tables = []
	for i in range(1,11):
		tables.append(generate_table(remove_space(clean_text(read_file(i)))))
	return tables

"""
Input one must be a number
"""
def compare_one_to_all(one):
	print("Comparing text nr " + str(one) + " with all other texts.")
	tables = get_all_tables()
	print(len(tables))
	text = tables[one-1].keys()
	for sentence in text:
		for i, table in enumerate([x for i, x in enumerate(tables) if i != one-1]):
			if i < one:
				j = i
			elif i > one:
				j = i+1
				
			if sentence in table.keys():
				print("Plagiat! Sentence:")
				print("\n" + sentence)
				print("in text nr " + str(j+1))
	return
	
print(compare_one_to_all(2))
	
	
	
	
	
	
	
	