#######################################################
### You can ignore the following lines of code.
### It loads the contents of a CSV file for you.
### The file's name should be a2_input.csv.
### You do NOT need to know how it works.
#######################################################

import csv
import itertools
contents = []

with open("a2_input.csv", 'r') as input_file:
    for row in csv.reader(input_file):
        #contents = contents + [row]
        contents.append(row)

#######################################################
### Do your data processing below.
### The below code gives some examples
### of how to access the data.
### Print your results using the print function.
#######################################################

#print("All it can do is print out the contents of a couple of cells of the file a2_input.csv:")
#print("Cell at index 0,0:")
#print(contents[4][0])
#print("Cell at index 0,1:")
#print(contents[0][1])
#print("Cell at index 1,0:")
#print(contents[2][7])
#print(int(contents[2][6])+int(contents[2][7]))
#print(type(contents[0][1]))
print (""" 
<!DOCTYPE html>
<html>
	<head>
	<title>Assignment 2</title>
	<style>
	table {
	    font-family: arial, sans-serif;
	    border-collapse: collapse;
	    width: 100%;
		margin-top: -350px;
	}

	td, th {
	    border: 2px solid #dddddd;
	    text-align: left;
	    padding: 8px;
	}

	tr:nth-child(even) {
	    background-color: #dddddd;
	}
	ul li{
	font-size:20px;
	font-family:"arial";
	color:#222222;
	}
</style>
	</head>
	<body>
		<table>
	""")


for r,c in itertools.product(range(0,20), range(0,9)):
	if c == 0:
		print("""			<tr>""")
	print ("""    			<th>""",contents[r][c],"""</th>""")
	if c==8:
		print("""			</tr><br/>""")
#print(contents[r][c])

print("""
		</table><ul>""")
for r,c in itertools.product(range(20,24), range(0,3)):
	if c == 0:
		print("""			<li>""")
	print ("""    			""",contents[r][c],""" """)
	if c==2:
		print("""			</li><br/>""")
print ("""</ul>	

	</body>
</html>
""")