from setuptools import setup, find_packages

setup(
    name="astro-crypto-analyzer",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'numpy>=1.24.0',
        'pandas>=2.0.0',
        'requests>=2.28.2',
        'ephem>=4.1.4',
        'scikit-learn>=1.2.2',
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A framework for analyzing cryptocurrency markets using astrological patterns",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/astro-crypto-analyzer",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)