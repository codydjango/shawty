import graphene

from models import Url
from database import db
from sqlalchemy.schema import Sequence
from helpers import is_valid_url, to_emoji_slug


# Query
# {
#   	redirect_url (slug: "sm-19")
#   	urls
# }
class Query(graphene.ObjectType):
    redirect_for_slug = graphene.String(slug=graphene.String())
    slugs = graphene.List(graphene.String)

    def resolve_redirect_for_slug(self, info, slug):
        url_obj = Url.query.filter(Url.slug==slug).first()

        if url_obj:
            return url_obj.redirect

        return None

    def resolve_slugs(self, info):
        return [url.slug for url in Url.query.all()]


### Mutation
# mutation myFirstMutation {
#   createShortUrl(redirectUrl: "https://github.com/codydjango/shawty") {
#   	short
#     ok
#   }
# }
class CreateShortUrl(graphene.Mutation):
    class Arguments:
        redirect_url = graphene.String()

    ok = graphene.Boolean()
    short = graphene.String()

    def mutate(self, info, redirect_url):
        redirect_url = redirect_url.strip()
        if not is_valid_url(redirect_url):
            return 'Malformed URL: {}'.format(redirect_url)

        # Check if it already exists
        url_obj = Url.query.filter(Url.redirect==redirect_url).first()

        if url_obj:
            ok = False # return false because it was found, but not created
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
