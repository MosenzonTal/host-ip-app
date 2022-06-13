# display hostname and IP address
from flask import Flask
import socket

app = Flask(__name__)

@app.route("/")
def get_Host_name_IP():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        # f = open("host-{}.txt".format(host_name), "w")
        # f.write("Host Name: {}, Ip: {}".format(host_name, host_ip))
        # f.close()
        return '''
        <h1"> Host Name: '''+host_name+'''</h1>
        <br>
        <h1"> Host IP: '''+host_ip+'''</h1>
        '''
    except:
        return '<p>Unable to get Hostname and IP</p>'

@app.route("/generate")
def generate_file():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        with open('/var/hosts/data/host-{}.txt'.format(host_name), 'w+') as f:
            f.write("Host Name: {}, Ip: {}".format(host_name, host_ip))
            f.close()
            return '<p>file was saved</p>'
    except:
        return '<p>There was a problem with creating the file</p>'
