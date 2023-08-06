glue-setuptools
===============

This project is derived from ``lambda-setuptools`` available on
`github <https://github.com/QuiNovas/lambda-setuptools>`__

##A Command extension to setuptools that builds an AWS Lambda compatible
zip file and uploads it to an S3 bucket

Simply add ``setup_requires=['glue_setuptools']`` as an attribute to
your *setup.py* file

This extension adds two new commands to setuptools:

1. **gdist**

   -  Usage:
      ``gdist --include-version=<True | true | Yes | yes | False | false | No | no>``

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

2. **gupload**

   -  Usage:
      ``gupload --access-key=<my_access_key> --secret-access-key=<my_secret> --s3-bucket=<my_S3_bucket> --kms-key-id=<my_KMS_key> --s3-prefix=<my_S3_key_prefix> --endpoint-url=<my_endpoint_url>``

      -  Effect: This will build (using *gdist*) and upload the
         resulting ZIP file to the specified S3 bucket

         -  *kms-key-id* is optional. If it is not provided, standard
            AES256 encryption will be used
         -  *s3-prefix* is optional. If it is not provided, the ZIP file
            will be uploaded to the root of the S3 bucket
         -  *endpoint_url* is optional. If it is not provided, the
            default endpoint for the accessed account will be used

This extension also adds new attributes to the setup() function:

1. **glue_entrypoint**

   -  Usage: glue_entrypoint=.:
   -  Effect: gdist will create a root-level python module named
      \_entrypoint.py where package_name is derived from the name
      attribute. This created module will simply redefine your glue
      entrypoint function at the root-level

All *gdist* attributes can be used in the same setup() call. It is up to
the user to ensure that you don’t step all over yourself…

Note that all other commands and attributes in setup.py will still work
the way you expect them to.

Enjoy!
