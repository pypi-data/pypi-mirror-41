import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rookie-stock-crawler",
    version="0.0.3",
    author="Cheney Ni",
    author_email="ncj19991213@126.com",
    description="A light weight tool to crawl stock data from yahoo finance.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nichujie/py-stock-crawler",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['requests', 'beautifulsoup4', 'psycopg2', 'psycopg2-binary'],
)
