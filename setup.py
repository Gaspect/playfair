from setuptools import setup

setup(
    name='playfair',
    version='0.0.1',
    packages=['playfair'],
    entry_points={
        'console_scripts': [
            'playfair = playfair.console:entrypoint',
        ]
    }
)