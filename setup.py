import setuptools


setuptools.setup(
    name="prueba1",
    version="0.0.1",
    author="Antonio German Marquez Trujillo",
    author_email="germanoctako@gmail.com",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
    install_requires=[
        'pytest>=2.8.0,<=6.2.5',
        'Flask>=1.0,<2.0',
    ]
)
