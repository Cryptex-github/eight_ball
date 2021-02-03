from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='async-8ball',
    version='0.1',
    description='Asynchronous 8ball response generator.',
    long_description=long_description,
    url='https://github.com/Cryptex-github/async-8ball',
    author='cryptex',
    license='Apache-2.0',
    requirements=requirements,
    packages=setuptools.find_packages(),
    zip_safe=False,
)
