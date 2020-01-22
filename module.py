from ext import db


class Comment(db.Model):
    c_id=db.Column(db.INT,primary_key=True)
    p_id=db.Column(db.VARCHAR)
    c_content=db.Column(db.VARCHAR)