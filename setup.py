"""
Flask-XUACompatible
-------------------

This is a simple Flask extension that sets X-UA-Compatible HTTP header for
all responses.
"""

from setuptools import setup


setup(
    name='flask-xuacompatible',
    version='0.1.0',
    url='https://github.com/jpvanhal/flask-xuacompatible',
    license='BSD',
    author='Janne Vanhala',
    author_email='janne.vanhala@gmail.com',
    description='Sets X-UA-Compatible HTTP header in your Flask application.',
    long_description=__doc__,
    py_modules=['flask_xuacompatible'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=['Flask'],
    test_suite='test_xuacompatible.suite',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
