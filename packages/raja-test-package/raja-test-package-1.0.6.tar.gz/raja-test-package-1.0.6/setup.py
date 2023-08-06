from setuptools import setup, find_packages;

# with open("README.md", "r") as fh:
#     long_description = fh.read()

setup(
    name="raja-test-package",
    version="1.0.6",
    author="Ganeshram Chockalingam",
    author_email="gchockalingam@paypal.com",
    description="Python Rest SDK for PayPal Checkout",
    long_description="Python Rest SDK for PayPal Checkout",
    long_description_content_type="text/markdown",
    url="https://github.com/paypal/Checkout-Python-SDK/",
    packages=find_packages(exclude=["tests","sample"]),
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["braintreehttp"],
)