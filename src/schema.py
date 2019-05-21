import graphene

from models import Url
from database import db
from sqlalchemy.schema import Sequence
from helpers import is_valid_url, to_emoji_slug


class Query(graphene.ObjectType):
    redirect_url = graphene.String(slug=graphene.String())
    urls = graphene.List(graphene.String)

    def resolve_redirect(self, info, slug):
        url_obj = Url.query.filter(Url.slug==slug).first()

        if url_obj:
            return url_obj.redirect

        return None

    def resolve_urls(self, info):
        return [url.get_full_short() for url in Url.query.all()]

schema = graphene.Schema(query=Query)

# Queries
# {
#   	redirect_url (slug: "sm-19")
#   	urls
# }
