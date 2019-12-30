from setuptools import find_packages, setup

with open("README.md") as f:
    long_description = f.read()

setup(
    name="pytest_anki",
    version="0.3.0",
    description="A pytest plugin for testing Anki 2.1 addons",
    author="Michal Krassowski, Aristotelis P. (Glutanimate)",
    maintainer="Aristotelis P. (Glutanimate)",
    url="https://github.com/glutanimate/pytest-anki",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Software Development :: Testing",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Framework :: Pytest",
        "Intended Audience :: Developers",
    ],
    keywords="anki development testing pytest",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires=[
        "pytest>=3.5.0",
        "pytest-forked",
        "pytest-xdist",
        "pytest-xvfb",
        "pyvirtualdisplay",
    ],
    entry_points={"pytest11": ["anki = pytest_anki"]},
)
