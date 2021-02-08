#!/usr/bin/env python

from setuptools import setup

setup(name='dfa-integration',
      version='0.0.1',
      description='Exports data from DFA to S3',
      author='Fishtown Analytics',
      url='http://fishtownanalytics.com',
      classifiers=['Programming Language :: Python :: 3 :: Only'],
      py_modules=['dfa_integration'],
      install_requires=[
          'agate==1.6.0',
          'Babel==2.5.3',
          'boto3==1.5.30',
          'botocore==1.8.44',
          'certifi==2018.1.18',
          'chardet==3.0.4',
          'croniter==0.3.20',
          'docutils==0.14',
          'future==0.16.0',
          'google-api-python-client==1.6.5',
          'httplib2==0.19.0',
          'idna==2.6',
          'isodate==0.6.0',
          'jmespath==0.9.3',
          'leather==0.3.3',
          'oauth2client==4.1.2',
          'parsedatetime==2.4',
          'pyasn1==0.4.2',
          'pyasn1-modules==0.2.1',
          'python-dateutil==2.6.1',
          'python-slugify==1.2.4',
          'pytimeparse==1.1.7',
          'pytz==2018.3',
          'requests==2.18.4',
          'rsa==3.4.2',
          's3transfer==0.1.13',
          'six==1.11.0',
          'Unidecode==1.0.22',
          'uritemplate==3.0.0',
          'urllib3==1.22'
      ],
      entry_points='''
          [console_scripts]
          dfa-integration=dfa_integration:main
      ''',
      packages=['dfa_integration']
)
