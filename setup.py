from setuptools import setup, find_packages

setup(
    name='cvalign',
    version='0.1.0',
    author='Anik Panja',
    author_email='anikpanja362@gmail.com',
    description='A GenAI-powered CV evaluator using RAG and Langchain',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/cvalign',  # Update if available
    packages=find_packages(),
    install_requires=[
        'torch>=2.0',
        'transformers>=4.36',
        'sentence-transformers>=2.2.2',
        'langchain>=0.1.14',
        'faiss-cpu>=1.7.4',
        'pypdf>=3.15.4',
        'python-docx>=1.1.0',
        'docx2txt>=0.8',
        'fastapi>=0.110.0',
        'uvicorn[standard]>=0.29.0',
        'jinja2>=3.1.3',
        'python-dotenv>=1.0.1',
        'boto3>=1.34.0',
        'pandas>=2.2.0',
        'numpy>=1.26.0',
        'scikit-learn>=1.3.0',
        'tqdm',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.9',
)
