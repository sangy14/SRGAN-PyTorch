from pathlib import Path
from setuptools import setup, find_packages

HERE = Path(__file__).resolve().parent
README = (HERE / "README.md").read_text(encoding="utf-8") if (HERE / "README.md").exists() else ""

# Read requirements.txt for install_requires if present
req_file = HERE / "requirements.txt"
install_requires = []
if req_file.exists():
    for line in req_file.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        install_requires.append(line)


setup(
    name="srgan_pytorch",
    version="0.1.0",
    description="SRGAN implementation in PyTorch (repository package)",
    long_description=README,
    long_description_content_type="text/markdown",
    author="sangy14",
    license="MIT",
    # Automatically find the package (assuming the source has been refactored into a directory)
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
