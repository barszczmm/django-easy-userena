from setuptools import setup, find_packages
import sys

userena = __import__('userena')

readme_file = 'README.mkd'
try:
    long_description = open(readme_file).read()
except IOError, err:
    sys.stderr.write("[ERROR] Cannot find file specified as "
        "``long_description`` (%s)\n" % readme_file)
    sys.exit(1)

setup(name='django-easy-userena',
      version=userena.get_version(),
      description='Complete user management application for Django',
      long_description=long_description,
      zip_safe=False,
      author='Maciej Marczewski',
      author_email='maciej@marczewski.net.pl',
      url='https://github.com/barszczmm/django-easy-userena/',
      download_url='https://github.com/barszczmm/django-easy-userena/downloads',
      include_package_data=True,
      install_requires = [
        'Django>=1.2.1',
        ### Required to build documentation
        # 'sphinx',
        # 'south',
      ],
      test_suite='tests.main',
      classifiers = ['Development Status :: 4 - Beta',
                     'Environment :: Web Environment',
                     'Framework :: Django',
                     'Intended Audience :: Developers',
                     'License :: OSI Approved :: BSD License',
                     'Operating System :: OS Independent',
                     'Programming Language :: Python',
                     'Topic :: Utilities'],
      )
