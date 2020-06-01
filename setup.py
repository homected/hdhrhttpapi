import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hdhrhttpapi", 
    version="0.0.1",
    author="Jose Luis Galindo",
    author_email="support@homected.com",
    description="HDHomeRun HTTP API interface library for Python 3.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/homected/hdhrhttpapi",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Natural Language :: English',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Multimedia :: Video :: Capture'
    ],
    python_requires='>=3.8',
    keywords='tv television tuner tvtuner hdhomerun',
)
