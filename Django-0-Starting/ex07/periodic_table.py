import sys

f_periodic = open("periodic_table.txt")
f_html = open("periodic_table.html","w")

html_template = """<html> 
<head> 
<title>Title</title> 
</head> 
<body> 
<h2>Welcome To GFG</h2> 
  
<p>Default code has been loaded into the Editor.</p> 
  
</body> 
</html> 
"""

f_html.write(html_template)
f_html.close()