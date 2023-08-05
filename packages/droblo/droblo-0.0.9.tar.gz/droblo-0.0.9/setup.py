# coding=utf-8
import setuptools

with open("README.md") as fh:
    long_description = fh.read()
setuptools.setup(
    name="droblo",
    version="0.0.9",
    author="KurisuD",
    author_email="KurisuD@pypi.darnand.net",
    # description="A network oriented, PostgreSQL backed, filesystem duplication detection and data mirroring system.",
    description="A multi-hosts, PostgreSQL backed, filesystem duplication detection system.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/KurisuD/droblo",
    packages=setuptools.find_packages(),
    install_requires=['pap_logger', 'watchdog', 'pathlib', 'psycopg2-binary', 'SQLAlchemy'],
    python_requires='>=3.5',
    include_package_data=True,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.5",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        "Operating System :: OS Independent",
        "Topic :: Utilities",
        "Topic :: System :: Filesystems",
        # "Topic :: System :: Archiving :: Mirroring"
    ],
)
