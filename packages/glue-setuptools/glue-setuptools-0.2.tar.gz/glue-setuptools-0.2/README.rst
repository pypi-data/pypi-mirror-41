glue-setuptools
===============

This project is derived from ``lambda-setuptools`` available on
`github <https://github.com/QuiNovas/lambda-setuptools>`__

####A Command extension to setuptools that builds an AWS Lambda
compatible zip file and uploads it to an S3 bucket

Simply add ``setup_requires=['glue_setuptools']`` as an attribute to
your *setup.py* file

This extension adds two new commands to setuptools:

1. **gdist**

   -  Usage:
      ``ldist --include-version=<True | true | Yes | yes | False | false | No | no>``

      -  Effect: This will build (using *bdist_wheel*) and install your
         package, along with all of the dependencies in
         *install_requires*

         -  *include-version* is optional. If not present it will
            default to *True*
         -  It is *highly* recommended that you **DO NOT** include
            *boto3* or *botocore* in your *install_requires*
            dependencies as these are provided by the AWS Glue
            environment. Include them at your own peril!
         -  The result will be in
            *dist/[your-package-name]-[version]-glue.zip* (along with
            your wheel)

All *gdist* attributes can be used in the same setup() call. It is up to
the user to ensure that you don’t step all over yourself…

Note that all other commands and attributes in setup.py will still work
the way you expect them to.

Enjoy!
