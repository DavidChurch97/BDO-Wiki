import ConfigParser
import logging

from logging.handlers import RotatingFileHandler
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def Home():
    return render_template("index.html"), 200

@app.route("/guides")
def Guides():
    return render_template("guides.html"), 200

@app.route("/about")
def About():
	return render_template("about.html"), 200

@app.route("/contact")
def Contact():
    return render_template("contact.html"), 200

@app.route("/berserker")
def Berserker():
    return render_template("berserker.html"), 200

def init(app):
    config = ConfigParser.ConfigParser()
    try:
        config_location = "etc/defaults.cfg"
        config.read(config_location)
        
        app.config['DEBUG'] = config.get("config", "debug")
        app.config['ip_address'] = config.get("config", "ip_address")
        app.config['port'] = config.get("config", "port")
        app.config['url'] = config.get("config", "url")
    except:
        print "Could not read configs from: ", config_location

if __name__ == '__main__':
    init(app)
    app.run(
        host=app.config['ip_address'], 
        port=int(app.config['port']))
