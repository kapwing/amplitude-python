from setuptools import setup, find_packages

setup(
    name='amplitude-python',
    keywords='python client for amplitude.com (based on HTTP API V2)',
    version='1.0.0',
    packages=find_packages(),
    long_description=open('README.txt').read(),
    test_suite='nose.collector',
    tests_require=['nose'],
    install_requires=['requests','nose','requests-mock[fixture]','testtools','twine'],
    url='https://github.com/kapwing/amplitude-python',
    author='kapwing',
    author_email='hello@kapwing.com',
    license='Apache License 2.0',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: System :: Logging',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.6',
        ],
)
