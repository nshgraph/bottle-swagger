import bottle as bottle
from bottle import get, post, hook
from bottle_swagger import swagger

app = bottle.app()

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

@post("/userid")
def userid_post(self, team_id):
  """
  Create a new user
  ---
  tags:
    - users
  parameters:
    - in: body
      name: body
      schema:
        id: User
        required:
          - email
          - name
        properties:
          email:
            type: string
            description: email for user
          name:
            type: string
            description: name for user
  responses:
    201:
      description: User created
  """
  return {}

@hook('after_request')
def after_request():
    bottle.response.headers['Access-Control-Allow-Origin'] = '*'
    bottle.response.headers['Access-Control-Allow-Headers'] = "Authorization, Content-Type"
    bottle.response.headers['Access-Control-Expose-Headers'] = "Authorization"
    bottle.response.headers['Access-Control-Allow-Methods'] = "GET, POST, PUT, DELETE, OPTIONS"
    bottle.response.headers['Access-Control-Allow-Credentials'] = "true"
    bottle.response.headers['Access-Control-Max-Age'] = 60 * 60 * 24 * 20

@app.route("/hacky")
def bla():
    """
    An endpoint that isn't using method view
    ---
    tags:
    - hacks
    responses:
      200:
        description: Hacked some hacks
        schema:
          id: Hack
          properties:
            hack:
              type: string
              description: it's a hack
            subitems:
              type: array
              items:
                schema:
                  id: SubItem
                  properties:
                    bla:
                      type: string
                      description: Bla
                    blu:
                      type: integer
                      description: Blu

    """
    return jsonify(['hacky'])

@get('/pet/<pet_id>/')
def get_pet(self, pet_id):
    """
    Get a pet.

    This is an example of how to use references and factored out definitions
    ---
    tags:
      - pets
    parameters:
      - in: path
        name: pet_id
    definitions:
      - schema:
          id: Pet
          required:
            - name
            - owner
          properties:
            name:
              type: string
              description: the pet's name
            owner:
              $ref: '#/definitions/Owner'
      - schema:
          id: Owner
          required:
            - name
          properties:
            name:
              type: string
              description: the owner's name
    responses:
      200:
        description: Returns the specified pet
        $ref: '#/definitions/Pet'
    """
    return {}


@app.route("/")
def hello():
    return "Hello World!"

@app.route("/spec")
def spec():
    results = swagger(app)
    print(results)
    return results

if __name__ == "__main__":
    results = swagger(app)
    print(results)
    # app.run(debug=True)
