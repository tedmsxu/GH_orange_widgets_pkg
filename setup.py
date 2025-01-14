from setuptools import setup, find_packages

setup(
    name="GH_orange_widgets",  # Name of your package
    version="0.1",
    packages=find_packages(),   # Automatically discover all packages
    install_requires=["orange3"],  # Ensure Orange is installed
    # entry_points={
    #     "orange.widgets": [
    #         "GH_orange_custom_widgets = GH_orange_custom_widgets.widgets",  # Register widgets
    #     ],
    # },
    include_package_data=True,  # Include icons and other files
    zip_safe=False,             # Do not zip the package
)