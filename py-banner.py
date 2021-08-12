a_table = [
1,1,0,
1,1,0,
1,1,0,
1,1,0,
1,1,0,
None
]

tables = [a_table]
letter_width = 3 # Don't change this, this is how many characters are in a line before creating a new one

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
			print(line_out)
			line_out = ""
			width_counter = 0
			if y == 1:
				line_out = line_out + filled_symbol
			else:
				line_out = line_out + blank_symbol
			width_counter = width_counter + 1
		
def createBanner(content, blank_symbol, filled_symbol):
	for x in content:
		x = x.lower()

		if x == "a":
			printLetter(0, blank_symbol, filled_symbol)
		
createBanner("A",".", "#")
