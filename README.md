## shawty url-shortening service

This API is built with python, graphql, and postgresql.

*Endpoints:*

* GET `/<shawt-url>` return a http redirect (302) if an associated url is found.
* POST `/` posting a request containing a body of `{url: <long url>}` will result in the creation of your own shawt url that you can share with your friends.

### Caveats

This is a small example application demonstrating flask, sqlalchemy, and graphQL. There aren't many tests,
and I'm not adhering to strict pep8. I've considered scalability, performance, and security, and
look forward to discussing my choices.

### Dependencies

* docker
* docker-compose

### Start it up

* run `./bin/start.sh` to build images and start the server on 127.0.0.1:3001
