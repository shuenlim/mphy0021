from setuptools import setup, find_packages

setup(
    name="Alchemist",
    version="0.1.0",
    author="Mystery Minnow",
    packages=find_packages(exclude=['*test']),
    install_requires=['argparse', 'pyyaml'],
    entry_points={
            'console_scripts': [
                    'abracadabra = alchemist.command:process'
            ]})
