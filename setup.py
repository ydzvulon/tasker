from setuptools import setup

# "hello",
setup(
    name="pytasker",
    version="0.1.5",
    description="Greet the world.",
    py_modules=["pytasker"],
    entry_points={
        "console_scripts": ["tasker_ctl=pytasker.tasker_ctl:main"]
    },
)