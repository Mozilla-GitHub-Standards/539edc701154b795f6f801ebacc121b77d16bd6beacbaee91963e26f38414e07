import os

from devmgr import __version__
from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.md')) as f:
    README = f.read()

with open(os.path.join(here, 'CHANGELOG.md')) as f:
    CHANGES = f.read()

dependency_links = [
    'https://github.com/mozilla/PyFxA/zipball/master#egg=PyFxA-0.0.6'
]

requires = [
    'boto>=2.38.0',
    'cryptography>=0.2',
    'mohawk>=0.2.2',
    'PyFxA>=0.0.6',
    'pyramid>=1.5.7',
    'sqlalchemy>=1.0.5',
    'waitress',
    'pyramid_debugtoolbar',
]

setup(name='devmgr',
      version=__version__,
      packages=find_packages(),
      description='Firefox Accounts-based device manager',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
          'Topic :: Internet :: WWW/HTTP',
          'Intended Audience :: Developers',
          'Programming Language :: Python',
      ],
      keywords='firefox accounts device manager',
      author='Mozilla Services',
      url='https://github.com/kitcambridge/fxa-device-manager-server',
      license='MPL 2.0',
      dependency_links=dependency_links,
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = devmgr.app:make_app
      """,
      )
