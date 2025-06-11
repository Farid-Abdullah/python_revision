
"""
Lab 10
Working with files
"""

def createRectangleHtmlEx1(fileName,width,height, color):
    if not("." in fileName and fileName.endswith("html")):
        fileName+=".html"
    filepath = "files/"+fileName
    code = """<html>
    
<head>
<style> div{width:"""+str(width)+"px; height:"+str(height)+"px; border: 2px solid "+color+"""}</style>
</head><body><div></div></body>
</html>"""
    with open(filepath,'w') as web:
        web.write(code)
    
        


#to test ex1, uncomment the following:   and check the file folder
#createRectangleHtmlEx1('myfirstwebsiteFromPython.html',500,100, 'blue')
