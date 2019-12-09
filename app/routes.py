
from app import app
import datetime
import socket
@app.route('/')
@app.route('/index')

def index():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    hostname = socket.gethostname()
    return ''' 
    <html>
        <head>
            <title> Home Page - App tutorial </title>
        </head>
        <body>
            <center>
                <h1>Computer world</h1>
                </br>
                <p>              
                Hostname: ''' + hostname + '''</br>
                    Time: ''' + now + '''
                </p>
            </center>
        </body>
    </html>'''
