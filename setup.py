from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='loducode_web3',
    packages=['loducode_web3','loducode_web3.migrations'],  # this must be the same as the name above
    version='0.1.1',
    description='Basic components for the development of loducode s.a.s. for web3',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Cristian Dulcey',
    author_email='cristian@loducode.com',
    url='https://github.com/cristdulcey/loducode_web3.git',  # use the URL to the github repo
    download_url='https://github.com/cristdulcey/loducode_web3.git/tarball/0.1.1',
    keywords=['web3', 'loducode_web3', 'loducode'],
    classifiers=[],
    install_requires=[i.strip() for i in open("requirements.txt").readlines()],
    setup_requires=['wheel'],
    include_package_data=True,
)
