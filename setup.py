from setuptools import setup, find_packages

setup(
    name='package_skeleton',
    description='An example of configuring a new Python package',
    version='0.1',
    packages=find_packages(exclude=["tests"]),      # Automatically recurse this package and determine what to install
    # install_requires=[],          # Declare dependencies here
    python_requires='>=3.4.3',      # Specify minimum python version
    include_package_data=True,      # Include any files specified by MANIFEST.in
    zip_safe=False,                 # Can this project be installed and run from a zip file? Why?
    # Auto-generate platform-specific scripts that run important features of the package
    entry_points={
        'console_scripts': [
            # 'skeleton-autorattle = package_skeleton.<module>:<function>',
        ],
        'gui_scripts': [
        ],
    },
    scripts=['bin/skeleton-rattle'],                # Custom scripts

    # Metadata
    url='https://github.com/KevinWMatthews/python-package_skeleton',
    author='Kevin W Matthews',
    author_email='KevinWMatthews@gmail.com',
    license='MIT',

    #TODO
    # test_suit='',
    # tests_require=[],
    # test_loader=,

    #TODO entry_points={},
)
