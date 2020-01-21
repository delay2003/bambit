#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import web
urls = ('/upload', 'Upload')
class Upload:
    def GET(self):
        web.header("Content-Type","text/html; charset=utf-8")
        return """<html><head></head><body>
<form method="POST" enctype="multipart/form-data" action="">
<input type="file" name="myfile" />
<br/>
<input type="submit" />
</form>
</body></html>"""
    def POST(self):
        x = web.input(myfile={})
        filedir = os.getcwd() # change this to the directory you want to store the file in.
        if 'myfile' in x: # to check if the file-object is created
            #filepath=x.myfile.filename.replace('\\','/') # replaces the windows-style slashes with linux ones.
            filepath=x.myfile.filename
            filename=filepath.split('/')[-1] # splits the and chooses the last part (the filename with extension)
            with open(filedir +'/'+ filename,'wb') as fout:# creates the file where the uploaded file should be stored
                fout.write(x.myfile.file.read()) # writes the uploaded file to the newly created file.
        raise web.seeother('/upload')
        # return "ok"
if __name__ == "__main__":
   app = web.application(urls, globals())
   app.run()
