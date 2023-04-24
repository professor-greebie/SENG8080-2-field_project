from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = []

setup(
    name="seng8080 Project",
    version="0.0.1",
    author="Ryan Deschamps",
    author_email="rdeschamps@conestogac.on.ca",
    description="A simple data getter and visualizer",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/professor_greebie/seng8080_1_project",
    packages=find_packages(),
    install_requires=requirements

)