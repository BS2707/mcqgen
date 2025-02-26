#install local pkg in Virtual env
from setuptools import find_packages, setup

setup(
    name='mcqgenerator',
    version='0.0.1',
    author='bhargavi seelam',
    author_email='bhargavi.seelam27@gmail.com',
    install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)