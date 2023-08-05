import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name='fritzremote',
    version='0.0.1',
    author="Dennis Schroeder",
    author_email="dennisschroeder@me.com",
    description="Let's you remote your Fritz!Box via selenium",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dennisschroeder/fritzremote",
    packages=setuptools.find_packages(),
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    zip_safe=False,
    install_requires=[
        'selenium',
    ],

)
