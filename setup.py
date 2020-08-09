from setuptools import setup

with open("README.md") as file:
    readme = file.read()
setup(
    name="angrylibs",
    description="Have a fluffy time by making some slimey choices",
    version="1.0.3",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Ben Soyka",
    author_email="bensoyka@icloud.com",
    url="https://angry-libs.readthedocs.io",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Games/Entertainment",
    ],
    license="MIT",
    packages=["angrylibs"],
    entry_points={
        "console_scripts": ["angrylibs=angrylibs:main", "libs=angrylibs:main"]
    },
    zip_safe=False,
    install_requires=["click~=7.1.2", "inflect~=4.1.0", "nltk~=3.5"],
    python_requires=">=3.7",
    include_package_data=True,
)
