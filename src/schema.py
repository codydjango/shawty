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


class CreateShortUrl(graphene.Mutation):
    class Arguments:
        redirect_url = graphene.String()

    ok = graphene.Boolean()
    short = graphene.String()

    def mutate(self, info, redirect_url):
        redirect_url = redirect_url.strip()
        if not is_valid_url(redirect_url):
            return 'malformed: {}'.format(redirect_url)

        # Check if it already exists
        url_obj = Url.query.filter(Url.redirect==redirect_url).first()

        if url_obj:
            ok = False
            return CreateShortUrl(short=url_obj.get_full_short(), ok=ok)

        next_id = db.session.execute(Sequence("urls_id_seq"))
        url_obj = Url(id=next_id, redirect=redirect_url, slug=to_emoji_slug(next_id))

        db.session.add(url_obj)
        db.session.commit()
        ok = True

        return CreateShortUrl(short=url_obj.get_full_short(), ok=ok)

class MyMutations(graphene.ObjectType):
    create_short_url = CreateShortUrl.Field()

schema = graphene.Schema(query=Query, mutation=MyMutations)

# Query
# {
#   	redirect_url (slug: "sm-19")
#   	urls
# }

# Mutation
# mutation myFirstMutation {
#   createShortUrl(redirectUrl: "http://codydjango.com/learning-rust10") {
#   	short
#     ok
#   }
# }
