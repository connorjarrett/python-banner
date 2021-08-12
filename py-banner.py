a_table = [
0,0,1,1,1,1,0,0,
0,0,1,1,1,1,0,0,
1,1,0,0,0,0,1,1,
1,1,0,0,0,0,1,1,
1,1,1,1,1,1,1,1,
1,1,1,1,1,1,1,1,
1,1,0,0,0,0,1,1,
1,1,0,0,0,0,1,1,
1,1,0,0,0,0,1,1,
1,1,0,0,0,0,1,1,
None
]

b_table = [
1,1,1,1,1,1,0,0,
1,1,1,1,1,1,0,0,
1,1,0,0,0,0,1,1,
1,1,0,0,0,0,1,1,
1,1,1,1,1,1,0,0,
1,1,1,1,1,1,0,0,
1,1,0,0,0,0,1,1,
1,1,0,0,0,0,1,1,
1,1,1,1,1,1,0,0,
1,1,1,1,1,1,0,0,
None
]

c_table = [
0,0,1,1,1,1,1,1,
0,0,1,1,1,1,1,1,
1,1,0,0,0,0,0,0,
1,1,0,0,0,0,0,0,
1,1,0,0,0,0,0,0,
1,1,0,0,0,0,0,0,
1,1,0,0,0,0,0,0,
1,1,0,0,0,0,0,0,
0,0,1,1,1,1,1,1,
0,0,1,1,1,1,1,1,
None
]

d_table = [
1,1,1,1,1,1,0,0,
1,1,1,1,1,1,0,0,
1,1,0,0,0,0,1,1,
1,1,0,0,0,0,1,1,
1,1,0,0,0,0,1,1,
1,1,0,0,0,0,1,1,
1,1,0,0,0,0,1,1,
1,1,0,0,0,0,1,1,
1,1,1,1,1,1,0,0,
1,1,1,1,1,1,0,0,
None,
]

final_print = []

tables = [a_table, b_table, c_table, d_table]
letter_width = 8 # Don't change this, this is how many characters are in a line before creating a new one

def outputPrint(table, out_len, blank_symbol):
	line_out = ""
	for x in range(10):
		for y in range(out_len): 
			line_out = line_out + (table[(y*10)+x]) + blank_symbol*3
		print(line_out)
		line_out = ""
			

def printLetter(letter_position, blank_symbol, filled_symbol):
	table = tables[letter_position]
	width_counter = 0 # Don't change this, this counts how wide a letter is so far
	line_out = ""
	print(len(table))
	for y in table:
		if width_counter < letter_width:
			if y == 1:
				line_out = line_out + filled_symbol
			else:
				line_out = line_out + blank_symbol
			width_counter = width_counter + 1
		else:
			final_print.append(line_out)
			line_out = ""
			width_counter = 0
			if y == 1:
				line_out = line_out + filled_symbol
			else:
				line_out = line_out + blank_symbol
			width_counter = width_counter + 1
	print("-------------")
	
	
def createBanner(content, blank_symbol, filled_symbol):
	for x in content:
		x = x.lower()
		if x == "a":
			printLetter(0, blank_symbol, filled_symbol)
		elif x == "b":
			printLetter(1, blank_symbol, filled_symbol)
		elif x == "c":
			printLetter(2, blank_symbol, filled_symbol)
		elif x == "d":
			printLetter(3, blank_symbol, filled_symbol)
	outputPrint(final_print, len(content), blank_symbol)
		
createBanner("ABCD",".", "#")
