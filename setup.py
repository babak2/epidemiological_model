from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='epidemiological_model',
    version='1.0.3',
    packages=find_packages(),
    install_requires=[
        'matplotlib==3.5.1',
        'numpy==1.24.4',
    ],
    entry_points={
        'console_scripts': [
            'run_simulation=epidemiological_model.scripts.run_simulation:main',
            'run_simulation_direct=run_simulation:main',
        ],
    },
    author='Babak Mahdavi Ardestani',
    author_email='babak.m.ardestani@gmail.com',
    description='A Python package for epidemiological modelling',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/babak2/epidemiological_model',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
