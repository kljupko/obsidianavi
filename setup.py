from setuptools import setup, find_packages

setup(
    name='obsidianavi',
    version='0.1.0',
    author='Ljupko Kolak',
    description='CLI tool for intelligent Obsidian note navigation',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    entry_points={
        'console_scripts': [
            'obsidianavi=obsidianavi.cli:main',
            'onavi=obsidianavi.cli:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
