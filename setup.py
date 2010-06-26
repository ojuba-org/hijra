#! /usr/bin/python
from distutils.core import setup
from glob import *
# to install type: 
# python setup.py install --root=/

setup (name='hijra', version='0.1',
      description='Hijri Islamic Calendar',
      author='Muayyad Saleh Alsadi',
      author_email='alsadi@ojuba.org',
      url='http://hijra.ojuba.org/',
      license='Waqf',
      py_modules=['hijra','HijriCal'],
      scripts=['HijriApplet'],
      data_files=[('/usr/share/doc/hijra-python', glob('*.html') ),
                  ('/etc/xdg/autostart',['hijra-autostart.desktop']),
      ]
)

