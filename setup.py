from distutils.core import setup

version = '0.42'

setup(
  name = 'kivyoav',
  packages = ['kivyoav'],
  version = version,
  description = 'A set of kivy utils and widgets - more details on github ...',
  author = 'Yoav Glazner',
  author_email = 'yoavglazner@gmail.com',
  url = 'https://github.com/yglazner/kivyoav', 
  download_url = 'https://github.com/yglazner/kivyoav/tarball/%s'%version, 
  keywords = ['kivy', 'widget', 'ui'], # arbitrary keywords
  classifiers = [],
)