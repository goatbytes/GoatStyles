from setuptools import setup, find_packages

setup(
    name='default_meta',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'mkdocs.plugins': [
            'default_meta = default_meta:DefaultMetaPlugin',
        ],
    }
)
