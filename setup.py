from setuptools import setup

with open('README.md') as file:
    long_description = file.read()

setup(name='tinydb-appengine',
      version='1.0.6',
      description='TinyDB Extension for AppEngine',
      long_description=long_description,
      long_description_content_type='text/markdown',
      author='Imalento',
      author_email='imalento2@gmail.com',
      url='https://github.com/imalento/tinydb-appengine',
      packages=['tinydb_appengine', ],
      # install_requires=['tinydb', ],
      license='MIT',
      keywords='database nosql tinydb appengine',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Topic :: Database',
          'Topic :: Database :: Database Engines/Servers',
          'Topic :: Utilities',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Operating System :: OS Independent'
      ],
      )
