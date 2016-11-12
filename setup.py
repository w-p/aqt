from setuptools import setup, find_packages


setup(
    name='aqt',
    version='0.1',
    author='William Palmer',
    author_email='will@steelhive.com',
    url='https://www.steelhive.com',
    description='AWS Query Tool',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click',
        'boto3',
        'colorama'
    ],
    entry_points={
        'console_scripts': [
            'aqt = aqt.bin.cli:main'
        ]
    }
)
