from setuptools import setup
from setuptools.command.install import install
import os
import sys

VERSION = '0.7.1'


class VerifyVersionCommand(install):
    """Custom command to verify that the git tag matches our version"""
    description = 'Verify that the git tag matches our version'

    def run(self):
        tag = os.getenv('CIRCLE_TAG')

        if tag != VERSION:
            info = "Git tag: {0} != phial version: {1}".format(tag,
                                                               VERSION)
            sys.exit(info)


setup(
    name='phial-slack',
    version=VERSION,
    url='https://github.com/sedders123/phial/',
    license='MIT',
    author='James Seden Smith',
    author_email='sedders123@gmail.com',
    description='A Slack bot framework',
    long_description=open('README.rst').read(),
    package_data={"phial": ["py.typed"]},
    packages=['phial'],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    python_requires='>=3.4',
    keywords=['Slack', 'bot', 'Slackbot'],
    install_requires=[
        'slackclient>=1.2.1',
        'Werkzeug>=0.14.1',
        'typing>=3.6.6'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    cmdclass={
        'verify': VerifyVersionCommand,
    },
    project_urls={
        'CI: Circle': 'https://circleci.com/gh/sedders123/phial',
        'GitHub: Issues': 'https://github.com/sedders123/phial/issues',
        'Documentation': 'https://phial.readthedocs.io/en/develop/'
    },
)
