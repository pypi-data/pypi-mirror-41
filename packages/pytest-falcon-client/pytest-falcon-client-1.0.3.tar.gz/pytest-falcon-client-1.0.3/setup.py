import os

from setuptools import setup


def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as _f:
        return _f.read()


setup(
    author='Nikita Sivakov',
    author_email='sivakov512@gmail.com',
    classifiers=[
        "Framework :: Pytest",
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Testing',
    ],
    description='Pytest `client` fixture for the Falcon Framework',
    entry_points={
        'pytest11': [
            'pytest-falcon-client = pytest_falcon_client.fixtures',
        ],
    },
    install_requires=['pytest>=3.4.0', 'falcon>=1.4.0'],
    keywords=['pytest', 'fixture', 'falcon', 'client', 'api'],
    license='MIT',
    long_description=read('README.md'),
    long_description_content_type="text/markdown",
    name='pytest-falcon-client',
    packages=['pytest_falcon_client'],
    python_requires='>=3.4',
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    url='https://github.com/sivakov512/pytest-falcon-client',
    version='1.0.3',
)
