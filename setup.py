from setuptools import setup, find_packages

setup(
    name='spacegame',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click',
        'tox',
        'nose',
    ],
    entry_points='''
        [console_scripts]
        spacegame=spacegame.main:main
    ''',
)
