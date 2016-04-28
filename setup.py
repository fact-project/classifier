from setuptools import setup

setup(
    name='classifier',
    version='0.0.2',
    description='classifier -- tools to build models on FACT MC data  ',
    url='https://github.com/fact-project/erna',
    author='Kai Brügge',
    author_email='kai.bruegge@tu-dortmund.de',
    license='MIT',
    # dependency_links = ['git+https://github.com/mackaiver/gridmap.git#egg=gridmap'],
    install_requires=[
        'pandas',           # in anaconda
        'numpy',            # in anaconda
        'matplotlib>=1.4',  # in anaconda
        'python-dateutil',  # in anaconda
        'pytz',             # in anaconda
        'tables',           # needs to be installed by pip for some reason
        # 'hdf5',
        'click',
        'numexpr',
        'pytest', # also in  conda
    ],
   zip_safe=False,
   entry_points={
    'console_scripts': [
        'apply_model = apply_model:main',
        'train_model = train_model:main',
    ],
  }
)
