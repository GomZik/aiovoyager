from setuptools import setup


setup(
    name='aiovoyager',
    version='0.0.1',
    description='Python 3\Asyncio based web framework with websockets',
    long_description=open('README.rst').read(),
    url='https://github.com/GomZik/aiovoyager',
    author='Aliaksiej Homza',
    author_email='aliaksei.homza@gmail.com',
    license=open('LICENSE').read(),
    packages=['aiovoyager'],
    install_requires=[
    ],
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: HTTP Servers'
    ],
    test_suite='nose.collector',
    tests_require=['nose'],
    zip_safe=False
)
