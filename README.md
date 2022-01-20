# Flask-Forward
Forward incoming Flask requests to an external API


## Requirements

- Before setting up all the flask routes, you should set some values in the library:
  - Set a module variable in the library to the external API's url prefix.
  - Also, you can add any additional headers/fields you want to
  - set the auth headers 
- Then you can simply pass in the request to the library and it will:
  - select which request method (get, put, delete, patch, etc...) to use by looking at the method used in the flask request method
  - build the absolute url path by combining the prefix + the url used in the flask request
  - use the flask.request.args, flask.request.data, flask.request.files, etc.. to send to the external api

You could then use a wildcard suffix for the flask routes so that all incoming requests starting with `/api` will just route using this library.
