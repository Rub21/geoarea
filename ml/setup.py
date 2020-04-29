try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages
setup(
    name='ml',
    version='1.0',
    description='Python scripts for ml data cleared ',
    author='developmentseed',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'cvat_smallbox=ml_script.cvat_smallbox.__init__:main',
            'cvat_intersectionbox=ml_script.cvat_intersectionbox.__init__:main',
            'rl_schoolspoint=ml_script.rl_schoolspoint.__init__:main',

            'geo_generateid=ml_script.geo_generateid.__init__:main',

        ],
    },
)
