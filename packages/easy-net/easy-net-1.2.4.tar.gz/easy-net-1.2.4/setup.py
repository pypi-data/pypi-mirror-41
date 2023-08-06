from setuptools import setup, find_packages

setup(
    name='easy-net',
    version='1.2.4',
    install_requires=[
        'attrs>=18.2.0',
        'setuptools>=39.2.0',
        'twisted>=17.5.0',
        'werkzeug>=0.14.1',
        'autobahn[twisted]',
    ],
    packages=find_packages(),
    platforms=['any'],
    python_requires='>=3.6',
    description='This is a simple wrapper for Twisted framework',
    url='https://github.com/pufit/easy-net',
    author='pufit',
    author_email='albrustovetskiy@edu.hse.ru',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3.6',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
