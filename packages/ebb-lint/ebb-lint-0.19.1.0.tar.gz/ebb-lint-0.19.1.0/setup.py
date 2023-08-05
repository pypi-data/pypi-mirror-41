import os

import versioneer
from setuptools import setup


# required due to vboxfs not supporting hard links. this doesn't have any ill
# effects. it just means there's a bit of copying instead of hard linking.
del os.link


extras_require = {
    'dev': [
        'coverage',
        'pytest>=4<5',
        'pytest-cov',
    ],
    ':python_version < "3.4"': [
        'enum34',
    ],
}

extras_require['all'] = list({
    dep for deps in extras_require.values() for dep in deps})


install_requires = [
    'awpa >= 0.16.1.0',
    'flake8-polyfill',
    'flake8 >= 2.6.0',
    'intervaltree>=3.0.0',
    'six',
    'venusian',
]


with open('README.rst') as infile:
    long_description = infile.read()


setup(
    name='ebb-lint',
    description='lint for ensuring quality software',
    long_description=long_description,
    author='Python Grammar Authority',
    author_email='mrw@enotuniq.org',
    url='https://github.com/pyga/ebb-lint',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Quality Assurance',
    ],
    license='MIT',
    packages=[
        'ebb_lint',
        'ebb_lint.checkers',
        'ebb_lint.test',
    ],
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    install_requires=install_requires,
    extras_require=extras_require,
    entry_points={
        'flake8.extension': [
            'L = ebb_lint:EbbLint',
        ],
    },
)
