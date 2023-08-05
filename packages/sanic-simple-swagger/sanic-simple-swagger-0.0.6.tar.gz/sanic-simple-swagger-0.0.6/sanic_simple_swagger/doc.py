from collections import defaultdict
from datetime import date, datetime


class Field:
    def __init__(self, description=None, required=None, name=None, choices=None):
        self.name = name
        self.description = description
        self.required = required
        self.choices = choices

    def serialize(self):
        output = {}
        if self.name:
            output['name'] = self.name
        if self.description:
            output['description'] = self.description
        if self.required is not None:
            output['required'] = self.required
        if self.choices is not None:
            output['enum'] = self.choices
        return output


class Integer(Field):
    def serialize(self):
        return {
            "type": "integer",
            "format": "int64",
            **super().serialize()
        }


class Float(Field):
    def serialize(self):
        return {
            "type": "number",
            "format": "double",
            **super().serialize()
        }


class String(Field):
    def serialize(self):
        return {
            "type": "string",
            **super().serialize()
        }


class Boolean(Field):
    def serialize(self):
        return {
            "type": "boolean",
            **super().serialize()
        }


class Tuple(Field):
    def __init__(self, fields=None, **kwargs):
        self.fields = fields
        super().__init__(**kwargs)
    
    def serialize(self):
        return {
            "type": "object",
            "properties": {obj: serialize_schema(str) for obj in self.fields},
            **super().serialize()
        }

class Date(Field):
    def serialize(self):
        return {
            "type": "string",
            "format": "date",
            **super().serialize()
        }


class DateTime(Field):
    def serialize(self):
        return {
            "type": "string",
            "format": "date-time",
            **super().serialize()
        }


class Dictionary(Field):
    def __init__(self, fields=None, **kwargs):
        self.fields = fields or {}
        super().__init__(**kwargs)

    def serialize(self):
        return {
            "type": "object",
            "properties": {key: serialize_schema(schema) for key, schema in self.fields.items()},
            **super().serialize()
        }


class List(Field):
    def __init__(self, items=None, *args, **kwargs):
        self.items = items or []
        if type(self.items) is not list:
            self.items = [self.items]
        super().__init__(*args, **kwargs)

    def serialize(self):
        if len(self.items) == 0:
            items = String().serialize()
        elif len(self.items) > 1:
            items = Tuple(self.items).serialize()

        return {
            "type": "array",
            "items": items
        }

definitions = {}

class Object(Field):
    def __init__(self, cls, *args, object_name=None, **kwargs):
        super().__init__(*args, **kwargs)

        self.cls = cls
        self.object_name = object_name or cls.__name__
        if self.cls not in definitions:
            definitions[self.cls] = (self, self.definition)

    @property
    def definition(self):
        return {
            "type": "object",
            "properties": {
                key: serialize_schema(schema)
                for key, schema in self.cls.__dict__.items()
                if not key.startswith("_")
                },
            **super().serialize()
        }

    def serialize(self):
        return {
            "type": "object",
            "$ref": "#/definitions/{}".format(self.object_name),
            **super().serialize()
        }


def serialize_schema(schema):
    schema_type = type(schema)

    # --------------------------------------------------------------- #
    # Class
    # --------------------------------------------------------------- #
    if schema_type is type:
        if issubclass(schema, Field):
            return schema().serialize()
        elif schema is dict:
            return Dictionary().serialize()
        elif schema is list:
            return List().serialize()
        elif schema is int:
            return Integer().serialize()
        elif schema is float:
            return Float().serialize()
        elif schema is str:
            return String().serialize()
        elif schema is bool:
            return Boolean().serialize()
        elif schema is date:
            return Date().serialize()
        elif schema is datetime:
            return DateTime().serialize()
        else:
            return Object(schema).serialize()

    # --------------------------------------------------------------- #
    # Object
    # --------------------------------------------------------------- #
    else:
        if issubclass(schema_type, Field):
            return schema.serialize()
        elif schema_type is dict:
            return Dictionary(schema).serialize()
        elif schema_type is list:
            return List(schema).serialize()

    return {}


# --------------------------------------------------------------- #
# Route Documenters
# --------------------------------------------------------------- #


class RouteSpec(object):
    consumes = None
    response_status = None
    response_description = None
    consumes_content_type = None
    produces = None
    produces_content_type = None
    summary = None
    description = None
    operation = None
    blueprint = None
    tags = None
    exclude = None
    deprecated = None

    def __init__(self):
        self.tags = []
        self.consumes = []
        super().__init__()


class RouteField(object):
    field = None
    example = None
    description = None
    location = None
    required = None

    def __init__(self, field, description=None, example=None, location=None, required=False):
        self.field = field
        self.description = description
        self.example = example
        self.location = location
        self.required = required


route_specs = defaultdict(RouteSpec)


def route(summary=None, description=None, consumes=None, produces=None, example=None,
          consumes_content_type=None, produces_content_type=None,
          exclude=None, deprecated=None):
    def inner(func):
        route_spec = route_specs[func]

        if summary is not None:
            route_spec.summary = summary
        if description is not None:
            route_spec.description = description
        if consumes is not None:
            route_spec.consumes = consumes
        if produces is not None:
            route_spec.produces = produces
        if consumes_content_type is not None:
            route_spec.consumes_content_type = consumes_content_type
        if produces_content_type is not None:
            route_spec.produces_content_type = produces_content_type
        if exclude is not None:
            route_spec.exclude = exclude
        if deprecated is not None:
            route_spec.deprecated = deprecated
        if example is not None:
            route_spec.example = example

        return func
    return inner

def exclude(boolean):
    def inner(func):
        route_specs[func].exclude = boolean
        return func
    return inner

def deprecated(boolean):
    def inner(func):
        route_specs[func].deprecated = boolean
        return func
    return inner

def summary(text):
    def inner(func):
        route_specs[func].summary = text
        return func
    return inner

def example(text):
    def inner(func):
        route_specs[func].example = text
        return func
    return inner

def description(text):
    def inner(func):
        route_specs[func].description = text
        return func
    return inner

def consumes(*args, content_type='application/json', description=None, example=None, location='query', required=False):
    def inner(func):
        if args:
            for arg in args:
                field = RouteField(arg, description, example, location, required)
                route_specs[func].consumes.append(field)
                route_specs[func].consumes_content_type = content_type

        return func
    return inner

def response_success(status=200, description='Successful operation'):
    def inner(func):
        route_specs[func].response_status = status
        route_specs[func].response_description = description
        return func
    return inner

def produces(*args, content_type=None):
    def inner(func):
        if args:
            field = RouteField(args[0])
            route_specs[func].produces = field
            route_specs[func].produces_content_type = content_type
        return func
    return inner


def tag(name):
    def inner(func):
        route_specs[func].tags.append(name)
        return func
    return inner
