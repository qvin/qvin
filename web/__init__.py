from flask import Flask
import settings

app=Flask(__name__)
app.config.from_object('web.settings')

#This import has to appear after instantiating the app and reading the settings
import views