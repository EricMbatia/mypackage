from setuptools import setup, find_packages

setup(
    name= 'top_n_finder',
    version= 0.1,
    packages=find_packages(exclude=['tests*']),
    license= 'MIT',
    description= 'Finds the top n items in a list in descending order',
    long_description= open('README.MD').read(),
    install_requires= ['numpy'],
    url= 'https://github.com/EricMbatia/mypackage',
    author= 'Eric Mbatia',
    author_email= 'mbatiaeric2@gmail.com'
)