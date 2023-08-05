from distutils.core import setup

setup(
    name='carta-ach',
    author='Carta, Inc.',
    author_email='jared.hobbs@carta.com',
    version='0.4.5',
    packages=[
        'ach',
    ],
    url='https://github.com/carta/python-ach',
    license='MIT License',
    description='Library to create and parse ACH files (NACHA)',
    long_description=open('README.rst').read(),
)
