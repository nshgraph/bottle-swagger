# bottle-swagger
A Swagger 2.0 spec extractor for Bottle

This is based originally of flask-swagger hosted at https://github.com/gangverk/flask-swagger

Install:
```
pip install bottle-swagger
```
Bottle-swagger provides a method (swagger) that inspects the Bottle app for endpoints that contain YAML docstrings with Swagger 2.0 [Operation](https://github.com/swagger-api/swagger-spec/blob/master/versions/2.0.md#operation-object) objects.

```
@get("/userid")
def userid_get(self, team_id):
  """
  Get a list of users
  First line is the summary
  All following lines until the hyphens is added to description
  ---
  tags:
    - users
  responses:
    200:
      description: Returns a list of users
  """
  return []
```
Bottle-swagger supports the normal bottle route decorators and manually specified routes

Following YAML conventions, flask-swagger searches for `---`, everything preceding is provided as `summary` (first line) and `description` (following lines) for the endpoint while everything after is parsed as a swagger [Operation](https://github.com/swagger-api/swagger-spec/blob/master/versions/2.0.md#operation-object) object.

In order to support inline definition of [Schema ](https://github.com/swagger-api/swagger-spec/blob/master/versions/2.0.md#schemaObject) objects in [Parameter](https://github.com/swagger-api/swagger-spec/blob/master/versions/2.0.md#parameterObject)  and [Response](https://github.com/swagger-api/swagger-spec/blob/master/versions/2.0.md#responsesObject) objects, flask-swagger veers a little off from the standard. We require an `id` field for the inline Schema which is then used to correctly place the [Schema](https://github.com/swagger-api/swagger-spec/blob/master/versions/2.0.md#schemaObject) object in the [Definitions](https://github.com/swagger-api/swagger-spec/blob/master/versions/2.0.md#definitionsObject) object.


[Schema ](https://github.com/swagger-api/swagger-spec/blob/master/versions/2.0.md#schemaObject) objects can be defined in a definitions section within the docstrings (see group object above) or within responses or parameters (see user object above). We also support schema objects nested within the properties of other [Schema ](https://github.com/swagger-api/swagger-spec/blob/master/versions/2.0.md#schemaObject) objects. An example is shown above with the address property of User.


To expose your Swagger specification to the world you provide a Flask route that does something along these lines

```
from bottle import bottle, route, get
from flask_swagger import swagger

app = Flask(__name__)

@get("/spec")
def spec():
    return swagger(app)
```

Note that the Swagger specification returned by `swagger(app)` is as minimal as it can be. It's your job to override and add to the specification as you see fit.
```
@get("/spec")
def spec():
    swag = swagger(app)
    swag['info']['version'] = "1.0"
    swag['info']['title'] = "My API"
    return jsonify(swag)
```


Acknowledgements

As noted above: This is based originally of flask-swagger hosted at https://github.com/gangverk/flask-swagger. Their acknowledgments are:
Flask-swagger builds on ideas and code from [flask-sillywalk](https://github.com/hobbeswalsh/flask-sillywalk) and [flask-restful-swagger](https://github.com/rantav/flask-restful-swagger)

