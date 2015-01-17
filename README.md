ssg_reloader
============

Serves Files statically via http, detects file changes, injects js code to check for changes and forces browser to reload

##Usage
`ssgreloader -h`

###Example
`/ssgreloader -i 0.0.0.0 -p 5000 -d test/test_data/`
* `-i 0.0.0.0` accept connections on all ip addresses
* `-p 5000` run on port 5000
* `-d` enable debugging information
* `test/test_data/` root directory to serve via http

##Installation
`pip install ssg_reloader`

##todo
* ~~write basic flask app~~
* ~~detect filechanges~~
* ~~inject js~~
* rewrite injection to not use bs4 and use something faster