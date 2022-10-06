import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='commonutils',
    version='0.0.1',
    author='Hard Kothari',
    author_email='hardkothari1988@gmail.com',
    description='Common Utilities handy for any python code',
    url='https://github.com/hardkothari/commonutils',
    project_urls = {
        "Bug Tracker": "https://github.com/hardkothari/commonutils/issues"
    },
    license='MIT',
    packages=['commonutils'],
    install_requires=['requests','mariadb', 'colorama']
)