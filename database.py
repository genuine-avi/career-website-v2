from sqlalchemy import create_engine,text
import os
db_connection_string=os.environ['DB_CONNECTION_STRING']
engine = create_engine(db_connection_string,connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem" 
        }
    })


def load_jobs_from_db():
  with engine.connect() as conn:
   result = conn.execute(text("select * from jobs"))
   columns=result.keys()
   jobs=[]
   for row in result.all():
    jobs.append(dict(zip(columns,row)))
   return jobs


def get_job_from_db(id):
    with engine.connect() as conn:
        query = text("SELECT * FROM jobs WHERE id = :id").bindparams(id=id)
        result = conn.execute(query)
        row = result.all()

        if len(row)==0:
            return None
        else:
            columns = result.keys()
            return dict(zip(columns, row[0]))



def add_application_to_db(job_id, data):
    query = text("INSERT INTO application (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)")


    with engine.connect() as conn:
        conn.execute(query.bindparams(
            job_id=job_id,
            full_name=data['full_name'],
            email=data['email'],
            linkedin_url=data['linkedin_url'],
            education=data['education'],
            work_experience=data['work_experience'],
            resume_url=data['resume_url']
        ))










