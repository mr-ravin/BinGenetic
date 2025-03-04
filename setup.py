import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bingenetic",
    version="2.3",
    author="Ravin Kumar",
    author_email="mr.ravin_kumar@hotmail.com",
    description="BinGenetic is a lightweight Python library that enables seamless conversion between binary data and genetic sequences (DNA or RNA), facilitating research in DNA data storage and bioinformatics.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mr-ravin/BinGenetic",
    keywords=['Data Storage', 'DNA Data Storage', 'RNA Data Storage', 'Genetic Storage'],
    packages=setuptools.find_packages(),  # Ensures correct package detection
    python_requires='>=3.7',  # Specifies Python version compatibility
    install_requires=[],  # Add dependencies if needed
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)