## 😎 Shawty url-shortening service 

This service will take a standard url, and return a much shorter url comprised of a hand-selected set of very special emoji characters.

This API is built with python, graphql, and postgresql.

__Endpoints:__

*GraphQL*

* GraphQL interface is available at  `http://localhost:3001/graphql/
* Responds to a query such as:

```
{
  shorter (url: "http://codydjango.com")
}
```

*REST*

* GET `/<shawt-url>` return a http redirect (302) if an associated url is found.
* POST `/` posting a request containing a body of `{url: <long-url>}` will result in the creation of your own short silly emoji url that you can share with your friends.

### 🙈 Caveats 

This is a small example service demonstrating flask, sqlalchemy, and graphQL. There aren't many tests,
and I'm not adhering to strict pep8. I've considered scalability, performance, and security, and
look forward to discussing my choices.

At the moment this is a backend service only, responding to GraphQL or REST requests. I might throw together a quick React frontend and add CORS support if I find spare time on Tuesday.

In all seriousness this is not a great idea for general url-shortening, as many browsers and middleware technologies still have a difficult time with emoji characters. Still fun though. 👯

### 😼 Dependencies

* docker
* docker-compose

### 🚀 Start it up

* run `./bin/start.sh` to build images and start the server on 127.0.0.1:3001
