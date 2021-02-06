from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(
    name='async8ball',
    version='1.5',
    description='Asynchronous 8ball response generator.',
    long_description_content_type="text/markdown",
    long_description=long_description,
    url='https://github.com/Cryptex-github/async8ball',
    author='cryptex',
    license='Apache-2.0',
    packages=["async8ball"],
    zip_safe=False,
)
