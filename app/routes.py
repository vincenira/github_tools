
## commented because of testing
from flask import Flask, render_template
import datetime, socket
appflask = Flask(__name__)

@appflask.route('/', methods=["GET", "POST"])
def index():
    try:

        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        return render_template('index.html', date_time=now, host_name=host_name, host_ip=host_ip)
    except:
        return render_template('404.html')




