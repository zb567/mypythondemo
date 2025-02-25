from setuptools import setup, find_packages

setup(
    name="mypythondemo",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A short description of your project",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/mypythondemo",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        # 示例依赖，根据实际需要修改
        'requests>=2.25.1',
        'numpy>=1.20.0'
    ],
    entry_points={
        'console_scripts': [
            'mypythondemo=mypythondemo.cli:main',
        ],
    },
)