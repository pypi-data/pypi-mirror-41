from setuptools import setup

setup(
    name='mantle',
    version='0.1.12',
    url='https://github.com/phanrahan/mantle',
    license='MIT',
    maintainer='Lenny Truong',
    maintainer_email='lenny@cs.stanford.edu',
    description='The magma standard library',
    packages=[
        "mantle",
        "mantle.common",
        "mantle.coreir",
        "mantle.lattice",
        "mantle.lattice.mantle40",
        "mantle.lattice.ice40",
        "mantle.verilog",
        "mantle.primitives",
        "mantle.util",
        "mantle.util.lfsr",
        "mantle.util.sort",
        "mantle.util.compressor",
        "mantle.util.lhca",
    ],

    install_requires=[
        "six",
        "fault>=0.20, <=0.36",
        "magma-lang>=0.1.6, <=0.1.7"
    ],
    python_requires='>=3.6'
)
