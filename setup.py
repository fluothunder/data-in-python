from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f_p:
    long_description = f_p.read()

setup(
    name='psda',
    version='1.0.0',
    packages=['psda', 'psda.stats', 'psda.io_data', 'psda.process'],
    license='MIT LICENSE',
    author='Paweł Rajkiewicz',
    author_email='pr382959@students.mimuw.edu.pl',
    description='Polish School Data Analyser is a small package made as a final assignment'
                'in Data in Python course at MIMUW, Spring 20/21.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        "pandas>=1.2.5",
        "numpy>=1.21",
        "xlrd>=2.0.1"
    ],
    python_requires='>=3.8.6'
)
