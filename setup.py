from setuptools import setup, find_packages


def readme():
  with open('README.md', 'r') as f:
    return f.read()


setup(
  name='BaseKit',
  version='1.0.2',
  author='Fedor Tyulpin',
  author_email='f.tyulpin@gmail.com',
  description='A Python module for converting numbers between numeral systems (2-36) and evaluating cross-base mathematical expressions.',
  long_description=readme(),
  long_description_content_type='text/markdown',
  packages=find_packages(),
  install_requires=[],
  classifiers=[
    'Programming Language :: Python :: 3.13',
    'Operating System :: OS Independent'
  ],
  keywords='converting numbers numeral systems',
  python_requires='>=3.6'
)