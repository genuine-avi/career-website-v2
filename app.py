from flask import Flask,render_template,jsonify
app=Flask(__name__)
JOBS=[
  {
    'id':1,
    'title':'Data-Analyst',
    'location':'Bengaluru,India',
    'salary':'Rs 1,000,000',
  },
{
    'id':2,
    'title':'Data-Scientist',
    'location':'Delhi,India',
    'salary':'Rs 1,060,000',
  },
{
    'id':3,
    'title':'Front-End Engineer',
    'location':'Gurgaon,India',
    'salary':'Rs 15,000,000',
  },
{
    'id':4,
    'title':'Data-Analyst',
    'location':'Remote',
    'salary':'$ 1,000,0000',
  },
]
@app.route("/")
def hello_world():
  return render_template('home.html',jobs=JOBS,company_name='Avirals')
@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)
  

if __name__=='__main__':
 app.run(host='0.0.0.0',debug=True)