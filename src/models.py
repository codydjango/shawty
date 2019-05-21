from database import db


class Url(db.Model):
    __tablename__ = 'urls'

    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(8), unique=True, index=True, nullable=False)
    redirect = db.Column(db.String(200), unique=True, index=True, nullable=False)

    def __repr__(self):
        return '<Url slug={} redirect={}>'.format(self.slug, self.redirect)

    def get_full_short(self):
        return '{protocol}://{domain}/{slug}'.format(protocol="http", domain="localhost:3001", slug=self.slug)
