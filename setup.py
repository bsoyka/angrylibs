from setuptools import setup

with open("README.md") as file:
    readme = file.read()
setup(
    name="angrylibs",
    description="Have a fluffy time by making some slimy choices",
    version="2.1.2",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Ben Soyka",
    author_email="bensoyka@icloud.com",
    url="https://angry-libs.readthedocs.io",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
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
    entry_points={"console_scripts": ["angrylibs=angrylibs:cli", "libs=angrylibs:cli"]},
    zip_safe=False,
    install_requires=["click>=2.0", "inflect>=4.0.0", "rich>=5.0.0"],
    python_requires=">=3.7",
    include_package_data=True,
    project_urls={
        "Documentation": "https://angry-libs.readthedocs.io/",
        "Changelog": "https://github.com/bsoyka/angrylibs/blob/master/CHANGELOG.md",
    },
)
