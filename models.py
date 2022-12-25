from marshmallow import Schema, fields, validates_schema, ValidationError

VALID_CMD_COMMANDS = ('filter', 'map', 'unique', 'sort', 'limit')
VALID_VALUES_SORT = ('desc', 'asc')


class RequestSchema(Schema):
    cmd = fields.Str(required=True)
    value = fields.Str()

    @validates_schema
    def check_all_cmd_valid(self, values: dict[str, str], *args, **kwargs):
        if values['cmd'] not in VALID_CMD_COMMANDS:
            raise ValidationError('"cmd" contains invalid value')

        if values['cmd'] == 'sort' and values['value'] not in VALID_VALUES_SORT:
            raise ValidationError('invalid sorting value')


class BatchRequestSchema(Schema):
    queries = fields.Nested(RequestSchema, many=True)
