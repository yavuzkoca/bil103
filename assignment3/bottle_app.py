#####################################################################
### Assignment skeleton
### You can alter the below code to make your own dynamic website.
### The landing page for assignment 3 should be at /assignment3/
#####################################################################

from bottle import route, run, default_app, debug, request
import cgitb; cgitb.enable()
import cgi
import sys
import csv
import os
contents = []

def htmlify(title, content):
    page = """<!DOCTYPE html>
              <html>
                  <head>
                      <title>""" + title + """</title>
                      <meta charset="utf-8" />
                  <link rel= "stylesheet" type= "text/css" href="/static/main.css" />
                  <style>
                  body{
                  background-color:#25383C;
                  }
                  .baslik{
                  margin:auto;
                  text-align:center;
                  font-size:30px;
                  font-weight: bold;
                  padding:10px;
                  color:#cf0; 
                  }
                  .alt_baslik{
                  	text-align:center;
                  	font-size:50px;
                  	font-family:"arial";
                  	margin:auto;
                  	padding:10px;
                  	font-family:DejaVu Serif Condensed;
					color:#75888C;
                  	text-decoration:underline;
                  	}
                  .cerceve{
                  	width:3000px;
                  	height:500px;
                  	margin-top:50px;
                  	} 
                  .bolme{
                  	width:327px;
                  	margin-right:5px;
                  	margin-left:25px;   	
                  	padding:10px;
                  	height:498px;
                  	font-family:Purisa;
                  	color:#98AFC7;
                  	float:left;
                  	}
                  	.bolme h1{
                  	text-align:center;
					color:#7F525D;
					}
                  	form {
                  	background-color:#cf0;
                  	float:center;
					margin-top:45%;
                  	}
                  	form input{
                  	float:center;
                  	background-color:#cf0;
                  	margin-right:220px;
                  	margin-left:100px;
					margin-bottom:40px;
                  	}
                  	form input[type=submit]{
                  	background-color:pink;
					font-family:verdana;
					margin-left:50%;
					margin-right:50%;
                  	}
					table {
					color:#fff;}
                  </style>
                  </head>
                  <body>
                      """ + content + """
                  </body>
              </html>"""
    return page

def a3_index():
	htmlify = ("""
    	<form style=float:center; action="/assignment3/direct/" method="post">
    		Username: <input type="text" name="kadi"> </br>
  			Password: <input type="password" name="sifre"> </br>
  			<input type="SUBMIT" value="SUBMIT">
		</form>
		""")
	return htmlify

def direct():
	global kadi
	global sifre
	kadi = request.POST.get('kadi')
	sifre = request.POST.get('sifre')
	if kadi == "admin" and sifre == "esc":
		text = ("""
		<p> Click here to do programming </p>
		<form action="/assignment3/admin/" method="post">
		<input type="SUBMIT" value = "Go !">
		</form>	
		<p> Click here to do sports </p>
		<form action="/assignment3/vote_sports/" method="post">
		<input type="SUBMIT" value = "Yay !">
		</form>
		""")
		return text
	else:
		html="You have entered the wrong password. To return to the beginning, <a href='/assignment3/'>click here.</a>"
		return htmlify('Login',html)	


def sports():
	deneme = """
	<form action="/assignment3/vote_sports_result/" method="post" >
	<p>Football </p>
    <input type="checkbox" name="Football" value="Football" ></br>
	<p>Basketball </p>
	<input type="checkbox" name="Basketball" value="Basketball" ></br>
	<p>Volleyball </p>
	<input type="checkbox" name="Volleyball" value="Volleyball" ></br>
	<p>Tennis </p>
	<input type="checkbox" name="Tennis" value="Tennis" ></br>
	<input type="submit" value="Haydi !">
	</form>
	"""
	return deneme

def get_vote_2():
	my_dir = os.path.dirname(__file__)
	file_path = os.path.join(my_dir,'sports_vote.csv')
	open(file_path,'rb')
	
	
			
	global vote
	vote1 = request.POST.get('Football')
	vote2 = request.POST.get('Basketball')
	vote3 = request.POST.get('Volleyball')
	vote4 = request.POST.get('Tennis')
	if vote1 == 'Football':
		contents[0][1] += ' *'
	if vote2 == 'Basketball':
		contents[1][1] += ' *'
	if vote3 == 'Volleyball':
		contents[2][1] += ' *'
	if vote4 == 'Tennis':
		contents[3][1] += ' *'
	f = str(contents[0][1])
	b = str(contents[1][1])
	v = str(contents[2][1])
	t = str(contents[3][1])
	
	html = "<table>"
	html += "<tr>"
	html += "<th>" + "Sport" +"</th>"
	html += "<th>" + "Vote" +"</th>"
	html += "</tr><tr>"
	html += "<th>" + "Football" +"</th>"
	html += "<th>" + f +"</th>"
	html += "</tr><tr>"
	html += "<th>" + "Basketball" +"</th>"
	html += "<th>" + b +"</th>"
	html += "</tr><tr>"
	html += "<th>" + "Volleyball" +"</th>"
	html += "<th>" + v +"</th>"
	html += "</tr><tr>"
	html += "<th>" + "Tennis" +"</th>"
	html += "<th>" + t +"</th>"
	html += "</tr>"
	html += "</table>"
	ths = open("sports_vote.csv", "w")
	ths.write("Football," + contents[0][1])
	ths.write("\nBasketball," + contents[1][1] )
	ths.write("\nVolleyball," + contents[2][1] )
	ths.write("\nTennis," + contents[3][1] )
	return htmlify('Vote My Sport',html)

def login():
		html = '<div class="baslik">Welcome, ' + kadi + '</div>'
		html += "<br><div class='alt_baslik'>The Most Programming Languages </div>"
		html += "<br><br><p style=color:white;text-align:center;font-size: 20pt;>There are 5 popular programming languages. if you don't have enough information about these languages, you can read the following paragraphs. Choose your favourite programming language and click select.</p> "
		html += "<div class='cerceve'> "
		html += '<div class="bolme"><h1>C</h1><p>AT&T bell laboratories by Dennis Ritchie and Ken Thompson the UNIX operating system at expand, in order to improve the B language is a structured programming language that is derived from. Brian kernighan and Dennis M. Ritchie the spread and popularization of development, although the date 1972, published by "the C programming language" book, after accelerated. Nowadays, almost all operating systems (Microsoft Windows, GNU/Linux, *BSD, Minix,) the construction of u</p></div>'
		html += '<div class="bolme"><h1>Java</h1><p>It\'s being developed by James Gosling of Sun Microsystems Java engineer open source, object-oriented, ground-independent, high-efficient, multifunctional, high-level, step-by-step run (interpreted-interpreted) language. Despite this language from the syntactic derivation, many C and C, These derivatives are simpler object model and fewer low-level facilities. Depending on the computer architecture Java applications without any Java virtual machine (JVM) that ca...(line truncated)...</p></div>'
		html += '<div class="bolme"><h1>PHP</h1><p>PHP is produced for the internet, server-sided, wide-to-use, general-purpose scripting and programming language that can be embedded into HTML. The development of PHP was created by Rasmus lerdorf in 1995 PHP for the first time today by the community are maintained. When working with more than 244 million websites as of January 2013 PHP, the PHP is setup on the web server 2.1 million.<br/>PHP code is interpreted by a Web server with PHP processing module, and out...(line truncated)...</p></div>'
		html += '<div class="bolme"><h1>Python</h1><p>Python, object-oriented, interpreted, modular (modular) and interactive high-level programming language.<br/>Simple indent based on syntax, makes it easier for you to remember and learn the language. This is her with the details of programming syntax, without wasting time gives the distinction of being a language that can begin to be made.<br/>The modular structure, the string class (system) and supports input any data in the field. Can run on almost any platf...(line truncated)...</p></div>'
		html += '<div class="bolme"><h1>Ruby</h1><p>Ruby is Object-Oriented, dynamic, reflective programming language. Designed in Japan by yukihiro Matsumoto and the Ruby language have been developed.<br/>As the syntax, Ada, Perl, small talk, Lisp, Eiffel, [3] affected by a programming language such as Ruby, Python syntax with some common properties. Functional, object-oriented, dynamic, reflective, as well as supports multiple programming paradigms.<br/>Free software Ruby, which is GPL and Ruby license is licen...(line truncated)...</p></div>'
		html += "</div>"
		html += "<form action='/assignment3/vote/' method='post'>"
		html += "C<input type='radio' name='lang' value='c' />"
		html += "JAVA<input type='radio' name='lang' value='java' />"
		html += "PHP<input type='radio' name='lang' value='php' />"
		html += "PYTHON<input type='radio' name='lang' value='python' />"
		html += "RUBY<input type='radio' name='lang' value='ruby' />"
		html += "<input type='SUBMIT' value='SELECT'/>"
		html += "</form>"
		return htmlify('Login',html)
		
def get_name():
    global first_name
    first_name = request.GET.get('fname')
    last_name = request.GET.get('lname')
    html = 'your name is ' + first_name + ' and your last name is ' + last_name + '<a href="/assignment4/" >click </a>'
    return htmlify('assignment3',html)
	
def website_index():
    return htmlify('Assignment3',
                   first_name +
                   """
                   <p><a href="/assignment1/">Click for my assignment 1.</a></p>
                   <p><a href="/assignment2/">Click for my assignment 2.</a></p>
                   <p><a href="/assignment3/">Click for my assignment 3.</a></p>
                   """)
def get_vote():
	with open("a3_vote.csv", 'r') as input_file:
		for row in csv.reader(input_file):
			contents.append(row)
			
	
	global vote
	vote = request.POST.get('lang')
	if vote == 'c':
		contents[0][1] += ' *'
	elif vote == 'java':
		contents[1][1] += ' *'
	elif vote == 'php':
		contents[2][1] += ' *'
	elif vote == 'python':
		contents[3][1] += ' *'
	elif vote == 'ruby':
		contents[4][1] += ' *'

	c = str(contents[0][1])
	java = str(contents[1][1])
	php = str(contents[2][1])
	python = str(contents[3][1])
	ruby = str(contents[4][1])
	html = "<table>"
	html += "<tr>"
	html += "<th>" + "DIL" +"</th>"
	html += "<th>" + "Oy Sayısı" +"</th>"
	html += "</tr>"
	html += "<th>" + "C" +"</th>"
	html += "<th>" + c +"</th>"
	html += "<tr>"
	html += "</tr>"
	html += "<th>" + "Java" +"</th>"
	html += "<th>" + java +"</th>"
	html += "<tr>"
	html += "</tr>"
	html += "<th>" + "PHP" +"</th>"
	html += "<th>" + php +"</th>"
	html += "<tr>"
	html += "</tr>"
	html += "</tr>"
	html += "<th>" + "Python" +"</th>"
	html += "<th>" + python +"</th>"
	html += "<tr>"
	html += "</tr>"
	html += "</tr>"
	html += "<th>" + "Ruby" +"</th>"
	html += "<th>" + ruby +"</th>"
	html += "<tr>"
	html += "</tr>"
	html += "</table>"
	ths = open("a3_vote.csv", "w")
	ths.write("C," + contents[0][1])
	ths.write("\nJava," + contents[1][1] )
	ths.write("\nPHP," + contents[2][1] )
	ths.write("\nPython," + contents[3][1] )
	ths.write("\nRuby," + contents[4][1] )
	return htmlify('Vote',html)		   
				   
route('/assignment3/vote_sports/','POST',sports)
route('/assignment3/direct/','POST',direct)
route('/assignment3/', 'GET', a3_index)
route('/assignment4/', 'GET', website_index)
route('/assignment3/admin/','POST',login)
route('/assignment3/vote/','POST',get_vote)
route('/assignment3/vote_sports_result/','POST',get_vote_2)
debug(True)
# This line is necessary for running on PythonAnywhere
application = default_app()
# The below code is necessary for running this bottle app standalone on your computer.
if __name__ == "__main__":
  run()