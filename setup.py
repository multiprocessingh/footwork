from setuptools import find_packages, setup  # type: ignore

with open("./requirements.txt") as fp:
    # benchling-apispec is not included in the core requirements because of complexities around installing packages
    # from the local filesystem. The hardcoding of benchling-apispec is a short term workaround until benchling
    # implements an internal python repository (similar to artifactory/pypy).
    install_requires = fp.read().splitlines()


setup(
    name="footwork",
    install_requires=install_requires,
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)
