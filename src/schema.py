import graphene

from models import Url
from database import db
from sqlalchemy.schema import Sequence
from helpers import is_valid_url, to_emoji_slug


class Query(graphene.ObjectType):
    shorter = graphene.String(url=graphene.String())

    def resolve_shorter(self, info, url):
        url = url.strip()
        if not is_valid_url(url):
            return 'malformed: {}'.format(url)

        # Check if it already exists
        url_obj = Url.query.filter(Url.redirect==url).first()

        if url_obj:
            return url_obj.get_full_short()

        next_id = db.session.execute(Sequence("urls_id_seq"))
        url_obj = Url(id=next_id, redirect=url, slug=to_emoji_slug(next_id))

        db.session.add(url_obj)
        db.session.commit()

        return url_obj.get_full_short()

schema = graphene.Schema(query=Query)

