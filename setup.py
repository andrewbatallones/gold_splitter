# Can look up classifiers here
# https://pypi.org/classifiers/
from setuptools import setup


with open('README.md', 'r') as fh:
	long_description = fh.read()

setup(
	name='gold_splitter',
    url='https://github.com/andrewbatallones/gold_splitter',
    author='Andrew Batallones',
    author_email='batallonesa@gmail.com',
	version='0.0.1',
	description='Split gold among party members.',
    long_description=long_description,
    long_description_content_type='text/markdown',
   	py_modules=['gold_splitter'],
	package_dir={'': 'src'},
	classifiers=[
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.8',
		'License :: OSI Approved :: MIT License',
		'Operating System :: OS Independent',
	],
    extras_require={
        'dev': [
            'pytest>=5.4'
        ],
    },
)
