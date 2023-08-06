import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as file:
    long_description = file.read()

setup(
    name='flake8-per-file-ignores',
    version='0.8.1',
    url='https://github.com/snoack/flake8-per-file-ignores',
    description='Ignore individual error codes per file with flake8',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Sebastian Noack',
    author_email='sebastian.noack@gmail.com',
    py_modules=['flake8_per_file_ignores'],
    install_requires=[
        'flake8>=3,<3.7',
        'pathmatch'
    ],
    entry_points={
        'flake8.extension': [
            'per-file-ignores = flake8_per_file_ignores:PerFileIgnores',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Quality Assurance',
    ]
)
