__author__ = 'mahnve'

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(description='HeadOn Blog',
      author='Marcus Ahnve',
      url='http://www.git',
      download_url='Where to download it.',
      author_email='m@hnve.org',
      version='0.1',
      install_requires=[''],
      packages=[
          'sinor',
          'test'],
      scripts=['scripts/sinor'],
      name='sinor',
      tests_require=['nosetests'],
      cmdclass={'test': })
