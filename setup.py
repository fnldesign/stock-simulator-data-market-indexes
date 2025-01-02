from setuptools import setup, find_packages

# Lê o arquivo requirements.txt
def parse_requirements(filename):
    with open(filename, encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip() and not line.startswith("#")]

setup(
    name="data_market_index_fetcher",
    version="0.1.6",
    packages=find_packages(),
    install_requires=parse_requirements("requirements.txt"),
    author="Flavio Lopes",
    author_email="fnldesign@hotmail.com",
    description="Um módulo para obter dados atualizados de índices de mercado financeiro, como IBOV, CDI, S&P 500, Dow Jones, e outros.",
    long_description=open("README.MD", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/fnldesign/stock-simulator-data-market-indexes",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "License :: Other/Proprietary License",
        "Operating System :: Microsoft :: Windows",
    ],
    python_requires=">=3.10",
)
