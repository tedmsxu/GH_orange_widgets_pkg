from setuptools import setup, find_packages

setup(
    name="GH_orange_widgets",
    version="0.1",
    description="Custom Orange add-on widgets",
    packages=find_packages(),  # Automatically find packages (e.g., GH_orange_widgets)
    entry_points={
        "orange.widgets": [
            "Custom Widgets = GH_orange_widgets.widgets",  # Register widgets
        ],
    },
    include_package_data=True,  # Include non-code files like icons
    zip_safe=False,
)