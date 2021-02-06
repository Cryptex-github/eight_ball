from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(
    name='async_8ball',
    version='1.1',
    description='Asynchronous 8ball response generator.',
    long_description_content_type="text/markdown",
    long_description=long_description,
    url='https://github.com/Cryptex-github/async_8ball',
    author='cryptex',
    license='Apache-2.0',
    packages=["async_8ball"],
    zip_safe=False,
)
