from setuptools import setup

setup(
    name='jupyter_format',
    version='0.0.0',
    python_requires='>=3.4',
    author='Matthias Geier',
    author_email='Matthias.Geier@gmail.com',
    description='An Experimental New Storage Format For Jupyter Notebooks',
    long_description=open('README.rst').read(),
    license='MIT',
    url='https://jupyter-format.readthedocs.io/',
    project_urls={
        'Documentation': 'https://jupyter-format.readthedocs.io/',
        'Source Code': 'https://github.com/mgeier/jupyter-format/',
        'Bug Tracker': 'https://github.com/mgeier/jupyter-format/issues/',
    },
    platforms='any',
    classifiers=[
        'Framework :: Jupyter',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities',
    ],
)
