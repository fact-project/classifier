from setuptools import setup

setup(
    name='klaas',
    version='0.3.0',
    description='KLAssification And regression Scripts.  yay',
    url='https://github.com/fact-project/klaas',
    author='Kai Brügge',
    author_email='kai.bruegge@tu-dortmund.de',
    license='BEER',
    packages=[
        'klaas',
        'klaas.scripts',
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    install_requires=[
        'pandas',           # in anaconda
        'numpy',            # in anaconda
        'matplotlib>=2.0',  # in anaconda
        'python-dateutil',  # in anaconda
        'pytz',             # in anaconda
        'pyyaml',             # in anaconda
        'tables',           # needs to be installed by pip for some reason
        'h5py',
        'click',
        'numexpr',
        'scikit-learn==0.18.1',
        'joblib',
        'tqdm',
        'pyfact>=0.9.2',
    ],
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'klaas_train_separation_model = klaas.scripts.train_separation_model:main',
            'klaas_apply_separation_model = klaas.scripts.apply_separation_model:main',
            'klaas_train_energy_regressor = klaas.scripts.train_energy_regressor:main',
            'klaas_apply_energy_regressor = klaas.scripts.apply_regression_model:main',
            'klaas_train_source_regressor = klaas.scripts.train_source_regressor:main',
            'klaas_apply_source_regressor = klaas.scripts.apply_source_regression_model:main',
            'klaas_split_data = klaas.scripts.split_data:main',
            'klaas_plot_separator_performance = klaas.scripts.plot_separator_performance:main',
            'klaas_plot_regressor_performance = klaas.scripts.plot_regressor_performance:main',
            'klaas_apply_cuts = klaas.scripts.apply_cuts:main',
            'klaas_convert_pandas2h5py = klaas.scripts.convert_pandas2h5py:main',
        ],
    }
)
