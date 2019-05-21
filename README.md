## 😎 Shawty URl shortening service 

This service will take a standard URL, and return a much shorter URL comprised of a hand-selected set of very special emoji characters.

This API is built with `Python 3.6`, `Flask 1.0.3`, `Graphene 2.1.3`, `SQLAlchemy 1.3.3` and `PostgreSQL 9.6`.


__Endpoints:__

*GraphQL*

* GraphQL interface is available at  `http://localhost:3001/graphql/

*Query*

```
{
  	redirectForSlug (slug: "💃😕") 
  	slugs
}
```

* `slugs` returns a list of all short urls currencly registered
* `redirectForSlug` return the redirect URL for a given slug

*Mutation*

```
mutation myFirstMutation { 
  createShortUrl(redirectUrl: "https://github.com/codydjango/shawty") {
  	short
    ok
  }
}
```

*REST*

* GET `/<shawt-url>` return a http redirect (302) if an associated URL is found.
* POST `/` posting a request containing a body of `{url: <long-url>}` will result in the creation of your own short silly emoji URL that you can share with your friends.

### 🙈 Caveats 

This is a small example service demonstrating flask, sqlalchemy, and graphQL. There aren't many tests,
and I'm not adhering to strict pep8. I've considered scalability, performance, and security, and
look forward to discussing my choices.

At the moment this is a backend service only, responding to GraphQL or REST requests. I might throw together a quick React frontend and add CORS support if I find spare time on Tuesday.

In all seriousness this is not a great idea for general URL shortening, as many browsers and middleware technologies still have a difficult time with emoji characters. Still fun though. 👯

### 😼 Dependencies

* docker
* docker-compose

### 🚀 Start it up

* run `./bin/start.sh` to build images and start the server on 127.0.0.1:3001
