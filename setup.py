from setuptools import setup, find_packages

setup(
    name="math_quiz",
    version="0.1",
    author="Mehmet Arif Bagci",
    author_email="mehmet.a.bagc@fau.de",
    description="Welcome to the mathematic quiz game! Let's play",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/mrfbgc/dsss_homework_2",
    packages=find_packages(),
    install_requires=[
         "numpy>=1.18.0",
         "setuptools>=58.0.0 "
    ],
    classifiers=[
        "Programming Language :: Python :: 3.12.4",
        "License :: Apache-2.0 license ",
        "Operating System :: Windows 10 Pro",
    ],
    python_requires='>=3.12.4',
)
