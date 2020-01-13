from flask import Response, Flask, render_template, request
import base64
import matplotlib.pyplot as plt
from random import *
import io
import json

def random_plot(n):
    fig, ax = plt.subplots( nrows=1, ncols=1 )
    xy = [random() for _ in range(2*n)]
    ax.plot(xy[:n], xy[n:])
    buf = io.BytesIO()
    fig.savefig(buf, format='svg')
    return buf.getvalue().decode('utf-8')


app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/data', methods=['POST'])
def mm():
    resp = json.loads(request.data.decode('utf-8'))
    n = int(resp["npoints"])
    plot = random_plot(n)
    return Response(plot)



if __name__ == "__main__":
    app.run()