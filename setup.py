from setuptools import setup, find_packages


with open('requirements.txt') as f:
    requirements = f.read().splitlines()


setup(
    name="python-libtemplate",
    version="1.0.0",
    author="Jan Wychowaniak",
    description="A simple demonstration library and a template for Python libraries",
    license="MIT",
    license_file="LICENSE",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/janwychowaniak/python-libtemplate.git",
    packages=find_packages(where='src'),
    package_dir={"": "src"},
    install_requires=requirements,
)
