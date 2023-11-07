import setuptools

VERSION = "0.0.3"  # PEP-440

NAME = "st-gsheets-connection"

INSTALL_REQUIRES = [
    "streamlit>=1.22.0",
    "gspread>=5.8.0",
    "gspread-pandas>=3.2.2",
    "gspread-dataframe>=3.3.0",
    "gspread-formatting>=1.1.2",
    "pandas>=1.3.0, <2",
    "duckdb>=0.8.1",
    "sql-metadata>=2.7.0",
    "validators>=0.22.0",
]

setuptools.setup(
    name=NAME,
    version=VERSION,
    description="Streamlit Connection for Google Sheets.",
    url="https://github.com/jeespenorio/gsheet_connect.py",
    project_urls={
        "Source Code": "https://github.com/jeespenorio/gsheet_connect.py",
    },
    author="Jeriel Ivan Don Espenorio",
    author_email="jeespenorio@gmail.com",
    license="Apache License 2.0",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.10",
    ],
    # Snowpark requires Python 3.8
    python_requires=">=3.8",
    # Requirements
    install_requires=INSTALL_REQUIRES,
    packages=["streamlit_gsheets"],
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
)
