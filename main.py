from flask import Flask,request,render_template,redirect,url_for,session
from pandas_utils import load_csv,describe_data,head_data,no_columns,get_row,help_command
import os

app = Flask(__name__)
app.secret_key = 'kashmir'
app.config['UPLOAD_FOLDER']='uploads'

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/upload', methods=['GET','POST'])
def upload():
    if 'file' not in request.files:
        return "No file part"
    
    file = request.files['file']
    if file.filename == '':
        return "No Files Selected"
    
    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'],file.filename)
        file.save(file_path)
        session['file_path'] = file_path
        df = load_csv(file_path)
        return df.to_html()
    
    return redirect(url_for('index'))

@app.route('/command', methods=['POST','GET'])
def command():
    command = request.form['command'].strip().lower()
    file_path = session.get('file_path')
    df = load_csv(file_path)

    if not file_path:
        return 'No file Uploaded '
    if file_path:
        if command == 'describe':
            return describe_data(df)
        elif command == 'head':
            return head_data(df)
        elif command == 'columns':
            return no_columns(df)
        elif command.startswith('row'):
            try:
                row_number = int(command.split()[1])
                return get_row(df, row_number)
            except (IndexError, ValueError):
                return 'Invalid row command. Please use "row <number>". and put space between number and row number'
        elif command == 'help':
            return help_command()
    else:
        return 'Invalid command. Please use commands like "describe", "head", "columns", "row <number>", etc.'


if __name__ == "__main__":
    app.run(debug=True)
