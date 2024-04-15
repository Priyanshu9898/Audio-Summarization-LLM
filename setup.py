from setuptools import find_packages, setup

setup(
    name="Audio Summarization App",
    version="0.0.1",
    author="Priyashu",
    author_email="priyanshumalaviya9@gmail.com",
    packages=find_packages(),
    install_requires=["pipwin", "pyaudio",
                      "google-generativeai", "python-dotenv", "streamlit"]
)
