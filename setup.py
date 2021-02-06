from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(
    name='eight_ball',
    version='3.0.2',
    description='Asynchronous 8ball response generator.',
    long_description_content_type="text/markdown",
    long_description=long_description,
    url='https://github.com/Cryptex-github/eight_ball',
    author='cryptex',
    license='Apache-2.0',
    packages=["eight_ball"],
    python_requires=">=3.4",
    keywords=["sync", "8ball"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3 :: Only",
        
    ],
    zip_safe=False,
)
