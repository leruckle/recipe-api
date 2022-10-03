from setuptools import setup, find_packages

setup(
    name='recipe_api',
    description='A REST API for recipes.',
    version='0.1',
    author='Leah Ruckle',
    packages=find_packages(where='src'),
    package_dir={'': 'src'}
)
