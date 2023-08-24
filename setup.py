from setuptools import setup

setup(
    name="layerzero-scan",
    version="1.0.0",
    description="A minimal Python API for LayerZero Scan.",
    url="https://github.com/kamilgg/layerzero-scan",
    author="Kamil\' Gatin (kamgg.eth)",
    author_email="kamil.gatin2604@gmail.com",
    license="MIT",
    packages=[
        "layerzero",
        "layerzero.enums",
        "layerzero.types",
        "layerzero.wrappers",
    ],
    install_requires=["requests", "pytest"],
    include_package_data=True,
    zip_safe=False,
)
