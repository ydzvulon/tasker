from setuptools import setup

# "hello",
setup(
    name="pytasker",
    version="0.0.1",
    description="Greet the world.",
    py_modules=["tasker"],
    entry_points={
        "console_scripts": ["tasker_ctl=tasker.nscm:main"]
    },
)