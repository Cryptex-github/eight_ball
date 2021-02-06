from setuptools import setup

with open('README.md') as f:
    long_description = f.read()
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='async8ball',
    version='2.0.3',
    description='Asynchronous 8ball response generator.',
    long_description_content_type="text/markdown",
    long_description=long_description,
    url='https://github.com/Cryptex-github/async8ball',
    author='cryptex',
    license='Apache-2.0',
    packages=["async8ball"],
    python_requires=">=3.4",
    requirements=requirements,
    keywords=["async", "8ball", "response", "discord", "discord.py", "discord bot", "bot", "py"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3 :: Only",
        
    ],
    zip_safe=False,
)
