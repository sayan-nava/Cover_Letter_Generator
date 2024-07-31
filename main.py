
# main.py 
  
# import Template from jinja2 for passing the content 
from jinja2 import Template 
from datetime import datetime

# variables that contain placeholder data
designation = input("Please input Designation: ")
company = input("Please input Company: ")
date = datetime.now().strftime("%B %d, %Y")
  
  
# Create one external template html page and read it 
File = open('template.html', 'r')
content = File.read() 
File.close()
  
# Render the template and pass the variabless 
template = Template(content) 
rendered_form = template.render(pl_date=date, pl_company=company, pl_designation=designation) 
  
  
# save the txt file in the Cover_Letter.txt
output = open('Cover_Letter.txt', 'w') 
output.write(rendered_form) 
output.close()