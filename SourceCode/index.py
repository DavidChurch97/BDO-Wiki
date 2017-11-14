import ConfigParser
import logging

from logging.handlers import RotatingFileHandler
from flask import Flask, render_template, request
app = Flask(__name__)

#--------Main pages--------#

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

#--------Main pages--------#

#--------Classes--------#

@app.route("/berserker")
def Berserker():
    return render_template("berserker.html"), 200

@app.route("/dark_knight")
def Dark_Knight():
    return render_template("dark_knight.html"), 200

@app.route("/kunoichi")
def Kunoichi():
    return render_template("kunoichi.html"), 200

@app.route("/musa")
def Musa():
    return render_template("musa.html"), 200

@app.route("/maehwa")
def Maehwa():
    return render_template("maehwa.html"), 200

@app.route("/ninja")
def Ninja():
    return render_template("ninja.html"), 200

@app.route("/ranger")
def Ranger():
    return render_template("ranger.html"), 200

@app.route("/sorceress")
def Sorceress():
    return render_template("sorceress.html"), 200

@app.route("/tamer")
def Tamer():
    return render_template("tamer.html"), 200

@app.route("/warrior")
def Warrior():
    return render_template("warrior.html"), 200

@app.route("/witch")
def Witch():
    return render_template("witch.html"), 200

@app.route("/wizard")
def Wizard():
    return render_template("wizard.html"), 200

#--------Classes--------#

#--------Life skills--------#

@app.route("/alchemy")
def Alchemy():
    return render_template("alchemy.html"), 200

@app.route("/cooking")
def Cooking():
    return render_template("cooking.html"), 200

@app.route("/gathering")
def Gathering():
    return render_template("gathering.html"), 200

@app.route("/hunting")
def Hunting():
    return render_template("hunting.html"), 200

@app.route("/trading")
def Trading():
    return render_template("trading.html"), 200

#--------Life skills--------#

#--------Provinces--------#

@app.route("/balenos")
def Balenos():
    return render_template("balenos.html"), 200

@app.route("/calpheon")
def Calpheon():
    return render_template("calpheon.html"), 200

@app.route("/media")
def Media():
    return render_template("media.html"), 200

@app.route("/serendia")
def Serendia():
    return render_template("serendia.html"), 200

@app.route("/valencia")
def Valencia():
    return render_template("valencia.html"), 200

#--------Provinces--------#

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
