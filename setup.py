from setuptools import setup

setup(name='joke',
      version='0.1',
      description='The funniest joke in the world',
      url='http://blabla',
      author='Flying Circus',
      author_email='flyingcircus@example.com',
      license='MIT',
      packages=['funniest'],
      install_requires=[
          'markdown',
      ],
      zip_safe=False) 
