from factory_translate import db


class Text(db.Model):
    __tablename__ = 'text'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    working_on = db.Column(db.Integer)
    origin_language = db.Column(db.String, nullable=False)
    requested_language = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)

    def __init__(self, text, working_on):
        self.text = text
        self.working_on = working_on

    def __repr__(self):
        return '<id {}>'.format(self.id)


class Translation(db.Model):
    __tablename__ = 'translation'

    id = db.Column(db.Integer, primary_key=True)
    translated_text = db.Column(db.Text)
    notes = db.Column(db.Text)
    text_id = db.Column(db.Integer, db.ForeignKey('text.id'))

    def __init__(self, translated_text, notes):
        self.translated_text = translated_text
        self.notes = notes

    def __repr__(self):
        return '<id {}>'.format(self.id)
