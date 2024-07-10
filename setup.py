from setuptools import setup, find_packages

VERSION = "0.0.1"
DESCRIPTION = "Sample Math Operations"
LONG_DESCRIPTION = "It is just demonstration of how to create python package"

# Setting up
setup(
    name="zmathplus",
    version=VERSION,
    author="Bhushan Kishore Vaiude",
    author_email="bkvaiude@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[],
    entry_points={"zmath_plugins": ["zmathplus = zmath.zmathplus"]},
    keywords=["python", "math", "divide"],
    classifiers=[
        "mathematics",
    ],
)
