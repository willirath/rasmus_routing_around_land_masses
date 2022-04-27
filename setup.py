#!/usr/bin/env python

"""The setup script."""

from os.path import exists

from setuptools import find_packages, setup

if exists("README.md"):
    with open("README.md") as f:
        long_description = f.read()
else:
    long_description = ""

CLASSIFIERS = [
    "Development Status :: 3 - Alpha",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Intended Audience :: Science/Research",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Topic :: Scientific/Engineering",
]

setup(
    name="lmroute",
    description="Routing around land masses",
    long_description=long_description,
    python_requires=">=3.6",
    maintainer="Willi Rath, Elena Shchekinova",
    maintainer_email="wrath@geomar.de",
    classifiers=CLASSIFIERS,
    url="https://github.com/willirath/rasmus_routing_around_land_masses",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[
        "shapely",
    ],
    extras_require={
        "dev": ["pytest", "pytest-cov"],
    },
    license="MIT",
    zip_safe=False,
    keywords=[],
    use_scm_version={"version_scheme": "post-release", "local_scheme": "dirty-tag"},
    setup_requires=["setuptools_scm", "setuptools>=30.3.0"],
)
