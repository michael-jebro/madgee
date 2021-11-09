from marshmallow import (
    Schema, fields
)


class CloudAppSchema(Schema):
    app_id = fields.Str()
    app_name = fields.Str()
    description = fields.Str()
    license_agr = fields.Str()
    icon_uri = fields.Url()
    date_added = fields.DateTime()
    fields.Di
