from marshmallow import Schema, fields

class UserRegisterSchema(Schema):
    name = fields.String(required=True)
    email = fields.Email(required=True)
    age = fields.Int(required=True, validate = lambda x: x >= 21)

class UserSchema(Schema):
    id = fields.Function(lambda obj: str(obj['id']), dump_only=True)
    name = fields.String()
    email = fields.Email()
    age = fields.Int()



    class Meta:
        strict = True