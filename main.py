import glob
from typing import Any
from flask import Flask, render_template, make_response
from flask import redirect, request, jsonify, url_for
from flask import flash
from werkzeug.utils import secure_filename
import os
from datetime import datetime
import io
from PIL import Image
from PIL import ImageDraw
from PIL import ImageChops
from PIL import ImageFont
import random
import stat
import tempfile
from itertools import chain
import re
from helper import parser
from helper import pgn

UPLOAD_FOLDER = "/Users/enrique/code/new/chesstool/pgnfiles"
FILE_SYSTEM_ROOT = "/Users/enrique/code/new/chesstool/pgnfiles"
ALLOWED_EXTENSIONS = {'txt', 'pgn'}

app = Flask(__name__,static_url_path='', static_folder='static', template_folder='templates')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 's3cr3t'
app.debug = True


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index2/<filename>', methods=['GET'])
def index2(filename):
    return render_template('index2.html', filename=filename)

@app.route('/loadBoard/<filename>', methods=['GET'])
def loadb(filename):
    return render_template(filename)

@app.route('/browser', methods= ['GET'])
def browse():
    itemList = os.listdir(FILE_SYSTEM_ROOT)
    return render_template('browse.html', itemList=itemList)

@app.route('/browser/<path:urlFilePath>')
def browser(urlFilePath):
    nestedFilePath = os.path.join(FILE_SYSTEM_ROOT, urlFilePath)
    if os.path.isdir(nestedFilePath):
        itemList = os.listdir(nestedFilePath)
        fileProperties = {"filepath": nestedFilePath}
        if not urlFilePath.startswith("/"):
            urlFilePath = "/" + urlFilePath
        return render_template('browse.html', urlFilePath=urlFilePath, itemList=itemList)
    if os.path.isfile(nestedFilePath):
        fileProperties = {"filepath": nestedFilePath}
        datapgn = open(nestedFilePath, encoding="ISO-8859-1").read()
        gameName = datapgn[0:6]
        datapgn = datapgn.replace('\n',' ')
        moves_txt = re.search('Text:(.+?)Score', str(datapgn))
        if moves_txt:
            moves_txt = moves_txt.group(1)
        tags_txt = re.search('Pairs:(.+?)Move', str(datapgn))
        if tags_txt:
            tags_txt = tags_txt.group(1)
        fen_txt = re.search('Fen_file:(.+?)$', str(datapgn))
        if fen_txt:
            fen_txt = fen_txt.group(1)
        sbuf = os.fstat(os.open(nestedFilePath, os.O_RDONLY)) #Opening the file and getting metadata
        fileProperties['game'] = datapgn
        fileProperties['type'] = stat.S_IFMT(sbuf.st_mode)
        fileProperties['mode'] = stat.S_IMODE(sbuf.st_mode)
        fileProperties['mtime'] = sbuf.st_mtime
        fileProperties['size'] = sbuf.st_size
        if not urlFilePath.startswith("/"):
            urlFilePath = "/" + urlFilePath
        return render_template('file.html', currentFile=nestedFilePath, fileProperties=fileProperties,
                               gameName = gameName, moves = moves_txt, tags=tags_txt, fen =fen_txt)
    return 'something bad happened'


@app.route('/uploadDatabase', methods=['POST'])
def upload_file():
    # check if the post request has the file part
    if 'file' not in request.files:
       flash('No file part')
       return redirect(request.url)
    file = request.files['file']
    # if user does not select file, browser also
    # submit an empty part without filename
    if file.filename == '':
       flash('No selected file')
       return redirect(request.url)
    if file and allowed_file(file.filename):
       filename = secure_filename(file.filename)
       upload_filename = filename
       file.save(os.path.join(app.config['UPLOAD_FOLDER']+'/upload/', filename))
       return redirect(url_for('index2', filename=filename))

@app.route('/processDatabase/<filename>', methods=['GET'])
def results(filename):
    os.system('python3 helper/process.py '+os.path.join(app.config['UPLOAD_FOLDER']+'/upload/', filename))
    params = {'filename': filename}
    return jsonify(params)

@app.route('/loadMoves/<filename>', methods=['GET'])
def moves(filename):
   #print(filename[5:6])
   params = {'filename': filename}
   return jsonify(params)

@app.route('/loadGame/<pgnfile>', methods=['GET'])
def loadgame(pgnfile):
    title = 'Result'
    pgn = get_file_content(pgnfile).rstrip()
    return redirect(url_for('index', filename=pgn))

def get_file_content(pgnf):
    with open('pgnfiles/'+pgnf, 'r') as file:
        nfile = file.read()
        file.close()
        return nfile

def get_groups(seq, group_by):
    data = []
    for line in seq:
        # Here the `startswith()` logic can be replaced with other
        # condition(s) depending on the requirement.
        if line.startswith(group_by):
            if data:
                yield data
                data = []
        data.append(line)

    if data:
        yield data

if __name__ == '__main__':
    app.run(port=8080, debug=True)
