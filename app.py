
from flask import Flask , render_template, request , redirect , url_for , flash,make_response
import json
import io
import csv

app = Flask(__name__)
app.secret_key ='12345' #requrie for sessions 



def load_data():
    try:
         with open('data.json' , 'r') as f:
          return json.load(f)  
    except (FileNotFoundError , json.JSONDecodeError):
      return []
def save_data(data):
   with open('data.json', 'w') as f:
      json.dump(data, f , indent=1)




@app.route('/')
def index():
    data = load_data()
    return render_template('index.html' ,data = data)



#donwload csv route


@app.route('/download')
def download_csv():
   data = load_data()

   output = io.StringIO()
   writer = csv.DictWriter(output , fieldnames = ['id','name','email','phone'])
   writer.writeheader()
   writer.writerows(data)

   output.seek(0)
   response = make_response(output.getvalue())
   response.headers['Content-Disponstion'] = "attachment; filename= data.csv"
   response.headers['Content-type'] = 'text/csv'


   return response

# create route





@app.route('/create', methods = ['POST' , 'GET'])
def create():
   if request.method == 'POST':
     data = load_data()
     new_id = request.form['id']
     if any (record ['id']  == new_id for record in data  ):
         flash(f'Error : ID {new_id} already exist','danger')
         return render_template('index.html', data = data)

     new_record = {
         "id": new_id,
         "name" : request.form['name'],
         "email" : request.form['email'],
         "phone" : request.form['phone']
         
     }
     data.append(new_record)
     save_data(data)
     flash('Record Created Sucessfully', 'success')
     return redirect(url_for('index'))
         

   
   return render_template('create.html')


# delte data query in python


@app.route('/delete/<string:id>' , methods=['post'])
def delete(id):
   data = load_data()
   new_data = [ record for record in data if record ['id' ] !=id]

   if len(data) == len(new_data):
      flash(f"Error : no recrd found id {id}",'danger')
   else:
       save_data(new_data)
       flash('Recod Deleted Successfully','danger')   

   return redirect(url_for('index'))     

@app.route('/edit/<string:id>' , methods = ['get','post'])
def edit(id):
   data = load_data()
   record = next (( item for item in data if item['id'] == id), None)
   
   if record is None:
      flash(f"Error: no record found with ID {id}", 'warning')
      return redirect(url_for('index'))

   if request.method == 'POST':
       record['name'] = request.form['name']
       record['email'] = request.form['email']
       record['phone'] = request.form['phone']
       save_data(data)
       flash('Record Updated Successfully','success')
       return redirect(url_for('index'))


   return render_template('edit.html', record = record)


if __name__ == '__main__':
    app.run(debug=True)