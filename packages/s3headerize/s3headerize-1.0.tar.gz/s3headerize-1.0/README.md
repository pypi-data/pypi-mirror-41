# s3headerize

A Python package for setting HTTP headers on Amazon Web Services (AWS) S3 objects.

Header values are configured per-name extension, with an optional catch-all if the object does not match any rules.

## Prerequisites

Python 3.x is required.

## Limitations

Only `Cache-Control` and `Content-Type` headers are currently supported.

## Configuring the headers and their values

The headers to set are configured in a YAML file with a list of rules.

For example:

```yaml
- header:        Cache-Control
  when:
    - extension: .html
      then:      max-age=300, public
    - extension: .css
      then:      max-age=604800, public
  else:          max-age=31536000, public
```

The result of this will be:

- Every `.html` object will receive a `Cache-Control` header with value `max-age=300, public`.
- Every `.css` object will receive a `Cache-Control` header with value `max-age=604800, public`.
- All other objects will receive a `Cache-Control` header with value `max-age=31536000, public`.

The `else` statement is optional. For example:

```yaml
- header:        Content-Type
  when:
    - extension: .woff2
      then:      font/woff2
```

The result of this will be:

- Every `.woff2` object will receive a `Content-Type` header with value `font/woff2`.
- The `Content-Type` header (or lackthereof) on all other objects will be unchanged.

There's a sample file at [sample-header-rules.yaml](sample-header-rules.yaml).

## Usage

### Installation

```shell
pip install s3headerize
```

### Command-line

```shell
python -m s3headerize  --bucket       <bucket to update>
                       --header-rules <path to rules file>
                      [--dry-run]
                      [--key-prefix   <optional key prefix>]
                      [--log-level    <optional log level>]
```

For example:

```shell
python -m s3headerize --header-rules ./headers-rules.yaml --bucket my-website
```

### In code

To run against a bucket:

```python
from s3headerize import BucketHeaderizer

rules = [
    {
        'header': 'Cache-Control',
        'when': [
          {
            'extension': '.html',
            'then': 'max-age=300, public'
          }
        ],
        'else': 'max-age=31536000, public'
    },
    {
        'header': 'Content-Type',
        'when': [
          {
            'extension': '.woff2',
            'then': 'font/woff2'
          }
        ]
    }
]

bucket_headerizer = BucketHeaderizer(header_rules=rules)
bucket_headerizer.update(bucket='my-website')
```

To run against specific keys:

```python
from s3headerize import ObjectHeaderizer

rules = [
    {
        'header': 'Cache-Control',
        'when': [
          {
            'extension': '.html',
            'then': 'max-age=300, public'
          }
        ],
        'else': 'max-age=31536000, public'
    },
    {
        'header': 'Content-Type',
        'when': [
          {
            'extension': '.woff2',
            'then': 'font/woff2'
          }
        ]
    }
]

object_headerizer = ObjectHeaderizer(bucket='my-website',
                                     header_rules=rules,
                                     key='index.html')
object_headerizer.update()
```

## Development

### Installing dependencies

```shell
pip install -e .[dev]
```

### Running tests

```shell
python test.py
```
