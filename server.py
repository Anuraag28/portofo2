from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)
print(__name__)

@app.route('/<username>/<int:post_id>')
def hello_world2(username=None, post_id=None):
    return render_template('index.html', name = username, id = post_id)

@app.route('/blog')
def blog():
    return 'My Views On Blogs'

@app.route('/blog/2020/dogs')
def blog2():
    return 'this is my dog'

@app.route('/about.me')
def about2():
    return render_template('about.html')

#@app.route('/favicon.ico')
#def favicon():
#	return send_from_directory(os.path.join(app.root_path, 'static'),
#                               'favicon.ico', mimetype='image/vnd.microsoft.icon')
#
@app.route('/')
def my_world():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
	with open('database.txt', mode = 'a') as database:
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
	with open('database.csv', newline='', mode='a') as database2:
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		csv_writer = csv.writer(database2, delimiter = ',', quotechar = '"', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email,subject,message])

#For Contacting
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
    	data = request.form.to_dict()
    	write_to_csv(data)
    	return redirect('/duplicate.html')
    else:
    	return 'something went wrong'
