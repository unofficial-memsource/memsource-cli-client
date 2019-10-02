from setuptools import setup, find_packages

if __name__ == "__main__":

    with open('README.md') as f:
        long_description = f.read()

    setup(
        setup_requires=['pbr>=2.0.0'],
        long_description=long_description,
	long_description_content_type="text/markdown",
        url="https://github.com/unofficial-memsource/memsource-cli-client",
        pbr=True
    )
