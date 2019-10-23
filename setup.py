from setuptools import setup

setup(name='QuotePuller',
      version='0.1',
      description='',
      url='http://github.com/nicholasceliano/quotepuller',
      author='Nick',
      author_email='nicholasceliano@gmail.com',
      license='MIT',
      packages=['quotepuller', 'quotepuller.services', 'quotepuller.models'],
      package_data={'quotepuller': ['config.json']},
      install_requires=[
          'mysql-connector-python',
      ],
      entry_points={"console_scripts": ["quotepuller=quotepuller.app:main"]},
      zip_safe=False)