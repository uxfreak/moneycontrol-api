from setuptools import setup, find_packages

setup(
    name='moneycontrol_api',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests',
        'uncurl'
    ],
    description='A library to fetch data from MoneyControl API',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/moneycontrol_api',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)