# perfect-jsonschema
[![Build Status](https://travis-ci.org/manycoding/perfect-jsonschema.svg?branch=master)](https://travis-ci.org/manycoding/perfect-jsonschema)
[![codecov](https://codecov.io/gh/manycoding/perfect-jsonschema/branch/master/graph/badge.svg)](https://codecov.io/gh/manycoding/perfect-jsonschema)
---
_Because soft validation is not enough_

# Why
[JSON schema standard](https://json-schema.org/) and its implementations stand that if you have something unfamiliar in your schema, it's not an error. In particular, you won't get an error if you made a typo or used something you thought as working. For example, this one is perfectly fine and valid:

    {
        "required": ["company"],
        "type": "object",
        "propertie": {"company": {"pattern": "^(Apple)$"}, "format": "url"},
    }
    
But we want to catch those `propertie` typos and invalid `url` [formats](https://python-jsonschema.readthedocs.io/en/latest/validate/#validating-formats).

The library rely on [jsonschema](https://github.com/Julian/jsonschema) and supports additional keywords to ignore.

# Features

Derives the draft from the schema and yields a `jsonschema.SchemaError` if:
* A schema is empty
* A schema contains a keyword which is not a part of a jsonschema implementation or `extended_keywords` set
* A schema contains an invalid format value
* A schema fails with `jsonschema.check_schema()`

# Usage

    from perfect-jsonschema import check

    try:
        check(schema, extended_keywords={"tag"})
    except Exception as e:
        do_something()

An exception example:

    Traceback (most recent call last):
        f"Schema contains invalid keywords for "
    jsonschema.exceptions.SchemaError: Schema contains invalid keywords for http://json-schema.org/draft-07/schema#:
    {'propertie', 'company'}

# Local development

    pipenv install --dev
    pipenv shell
    tox

# Contribution
  
  Any contribution is welcome
  
