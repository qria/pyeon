from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(name='pyeon',
      version='0.0.3',
      description='''Generates some phrases when someone goes to the \
convenience store.''',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='http://github.com/qria/pyeon',
      author='MinJune Kim',
      author_email='qria' '@' 'qria.net',
      license='MIT',
      packages=['pyeon'],
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
      ],
      zip_safe=False)
