from setuptools import setup, find_packages

setup(
    name='movie-recommender-system',
    version='0.0.1',
    author='TAOFIQUE KHAN',
    author_email='taofiquekhan535@gmail.com',
    description='A small example package for movie recommendation',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    python_requires='>=3.7',
    install_requires=[
        'streamlit',
        # Add other specific dependencies from requirements.txt here
        # but keep '-e .' in requirements.txt
    ]
)