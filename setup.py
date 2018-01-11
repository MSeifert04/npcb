from setuptools import setup

setup(name='npcb',
      version='0.0.1',
      description='Copy NumPy arrays via the clipboard',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Text Processing :: Linguistic',
      ],
      keywords='funniest joke comedy flying circus',
      url='https://github.com/MSeifert04/npcb',
      author='Michael Seifert',
      author_email='michaelseifert04@yahoo.de',
      license='Apache License 2.0',
      packages=['npcb'],
      install_requires=[
          'numpy',
      ],
      zip_safe=False)