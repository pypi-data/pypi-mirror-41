import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="anipose",
    version="0.1.0",
    author="Pierre Karashchuk",
    author_email="krchtchk@gmail.com",
    description="Framework for scalable DeepLabCut based analysis including 3D tracking",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lambdaloop/anipose",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)"
    ],
    entry_points={
        'console_scripts': ['anipose=anipose.anipose:cli']
    },
)
