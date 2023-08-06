import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='windpowerlib',
      version='0.1.1',
      description='Creating time series of wind power plants.',
      url='http://github.com/wind-python/windpowerlib',
      author='oemof developing group',
      author_email='windpowerlib@rl-institut.de',
      license=None,
      packages=['windpowerlib'],
      package_data={
          'windpowerlib': [os.path.join('data', '*.csv')]},
      long_description=read('README.rst'),
      zip_safe=False,
      install_requires=['pandas >= 0.19.1, < 0.25 ',
                        'requests < 3.0'])
