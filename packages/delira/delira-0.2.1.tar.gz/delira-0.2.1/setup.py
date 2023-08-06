import os
import re
from setuptools import find_packages, setup
from setuptools.command.sdist import sdist
from setuptools.command.bdist_egg import bdist_egg
from wheel.bdist_wheel import bdist_wheel


def resolve_requirements(file):
    requirements = []
    with open(file) as f:
        req = f.read().splitlines()
        for r in req:
            if r.startswith("-r"):
                requirements += resolve_requirements(
                    os.path.join(os.path.dirname(file), r.split(" ")[1]))
            else:
                requirements.append(r)
    return requirements


def read_file(file):
    with open(file) as f:
        content = f.read()
    return content


def find_version(file):
    content = read_file(file)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", content,
                              re.M)
    if version_match:
        return version_match.group(1)


requirements = resolve_requirements(os.path.join(os.path.dirname(__file__),
                                                 'requirements.txt'))

requirements_extra_full = []

requirements_extra_torch = resolve_requirements(os.path.join(
    os.path.dirname(__file__), 'requirements_extra_torch.txt'))
requirements_extra_full += requirements_extra_torch

readme = read_file(os.path.join(os.path.dirname(__file__), "README.md"))
license = read_file(os.path.join(os.path.dirname(__file__), "LICENSE"))
delira_version = find_version(os.path.join(os.path.dirname(__file__), "delira",
                                           "__init__.py"))

setup(
    name='delira',
    version=delira_version,
    packages=find_packages(),
    url='https://git.lfb.rwth-aachen.de/Radiology/Delira/',
    test_suite="pytest",
    long_description=readme,
    long_description_content_type="text/markdown",
    license=license,
    install_requires=requirements,
    tests_require=["pytest-cov"],
    python_requires=">3.5",
    extras_require={
        "full": requirements_extra_full,
        "torch": requirements_extra_torch
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3",
        "Topic:: Scientific/Engineering",
        "Topic:: Scientific/Engineering:: Artificial Intelligence"
    ],
    keywords=['deep learning', 'medical image analysis',
              'medical image segmentation', 'pytorch', 'radiology']
)
