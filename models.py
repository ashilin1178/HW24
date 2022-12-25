from marshmallow import Schema, fields, validates_schema, ValidationError

VALID_CMD_COMMANDS = ('filter', 'map', 'unique', 'sort')


class RequestSchema(Schema):
    cmd = fields.Str(required=True)
    value = fields.Str()


    @validates_schema
    def check_all_cmd_valid(self, values: dict[str, str], *args, **kwargs):
        if values['cmd1'] not in VALID_CMD_COMMANDS or values['cmd2'] not in VALID_CMD_COMMANDS:
            raise ValidationError('"cmd" contains invalid value')


class BatchRequestSchema(Schema):
    queries = fields.Nested(RequestSchema(), many=True)
