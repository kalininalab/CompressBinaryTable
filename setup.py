from distutils.core import setup

setup(name='compressbinarytable',
      version="0.1.4",
      description='Compresses binary tables',
      author='Alper Yurtseven',
      author_email='alper.yurtseven@helmholtz-hips.de',
      license='',
      packages=['compressbinarytable'],
      scripts=['compressbinarytable/compressbinarytable.py'],
      entry_points={
        'console_scripts': [
            'compressbinarytable.compressbinarytable:main'
        ]
    }
)