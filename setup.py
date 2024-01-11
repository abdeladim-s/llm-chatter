from pathlib import Path

from setuptools import setup, find_packages


# read the contents of your README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()


setup(
    name="llm_chatter",
    version="0.0.0",
    author="abdeladim-s",
    description="",
    long_description=long_description,
    ext_modules=[],
    zip_safe=False,
    python_requires=">=3.8",
    packages=find_packages('.'),
    package_dir={'': '.'},
    long_description_content_type="text/markdown",
    license='MIT',
    project_urls={
        'Documentation': 'https://abdeladim-s.github.io/llm_chatter/',
        'Source': 'https://github.com/abdeladim-s/llm_chatter',
        'Tracker': 'https://github.com/abdeladim-s/llm_chatter/issues',
    },
    install_requires=[""],
)
