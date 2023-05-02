from sqlalchemy import create_engine, text

engine = create_engine("mysql+pymysql://root:123qwe@localhost:3306/jd_job")

def get_jobs():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        columns = result.keys()
        jobs = [dict(zip(columns, row)) for row in result.fetchall()]
        return jobs