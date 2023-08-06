from functools import partial
from .errors import ValidationError, FormValidationError, FieldValidationError
from jsonschema import Draft4Validator
from .util import jsl_to_jsonobject, dataclass_to_jsl, dataclass_get_type
import reg
from morepath.publish import resolve_model
import urllib
import re


@reg.dispatch(reg.match_instance('model'), reg.match_instance('request'))
def get_data(model, request):
    raise NotImplementedError


def regex_validator(pattern, name):
    p = re.compile(pattern)

    def _regex_validator(value):
        if not p.match(value):
            raise FieldValidationError(
                '%s does not match %s pattern' % (value, name))

    return _regex_validator


def load(validator, schema, request):
    newreq = request.app.request_class(
        request.environ.copy(), request.app.root,
        path_info=urllib.parse.unquote(request.path))
    context = resolve_model(newreq)
    context.request = request
    if schema is None:
        dc = context.schema
    else:
        dc = schema
    jslschema = dataclass_to_jsl(dc, nullable=True)
    schema = jslschema.get_schema(ordered=True)
    form_validators = request.app.get_formvalidators(dc)
    params = {}

    validator.check_schema(schema)
    v = validator(schema)
    data = get_data(context, request)
    field_errors = sorted(v.iter_errors(data), key=lambda e: e.path)
    if field_errors:
        params['field_errors'] = field_errors
    form_errors = []
    for form_validator in form_validators:
        e = form_validator(request, request.json)
        if e:
            form_errors.append(FormValidationError(e))

    if form_errors:
        params['form_errors'] = form_errors

    if params:
        raise ValidationError(**params)

    # field errors
    for k, f in dc.__dataclass_fields__.items():
        t = dataclass_get_type(f)
        for validate in t['metadata']['validators']:
            validate(data[k])
    return request.json


def validate_schema(validator=Draft4Validator, schema=None):
    return partial(load, validator, schema)
