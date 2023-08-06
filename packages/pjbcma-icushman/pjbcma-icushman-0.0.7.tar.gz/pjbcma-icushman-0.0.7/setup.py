import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pjbcma-icushman",
    version="0.0.7",
    author="Isaiah Cushman",
    author_email="icushman@uci.edu",
    description="An assistant for using pyjags",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/icushman/pjBCM",
    packages=['pjbcma'],
    install_requires=[
	"numpy",
	"pyjags",
	"pandas",
	"matplotlib",
	"seaborn",
	"scipy",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
)

