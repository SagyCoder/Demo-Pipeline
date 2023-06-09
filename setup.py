from setuptools import setup, find_packages

setup(name="census-income",
      version="0.0.1",
      author="sagar",
      author_email="shinde.sagar090@gmail.com",
      packages=find_packages(),
      install_requires=["pandas","numpy","flask"]
      )