from setuptools import setup

import sys

if sys.version_info[0] != 3:
    sys.stderr.write("pintail requires python 3\n")
    sys.exit(1)

try:
    import lxml.etree
    lxml.etree.XSLT
except:
    sys.stderr.write("pintail requires lxml.etree.XSLT\n")
    sys.exit(1)

setup(
    name='pintail',
    version='0.5',
    description='Build complete web site from Mallard sources.',
    packages=['pintail'],
    namespace_packages=['pintail'],
    scripts=['bin/pintail'],
    package_data={
        'pintail': ['sample.cfg', 'pintail-atom.xsl', 'pintail-html.xsl'],
    },
    author='Shaun McCance',
    author_email='shaunm@gnome.org',
    license='GPLv2+',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
        'Topic :: Text Processing :: Markup',
        'Topic :: Text Processing :: Markup :: XML',
        'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)'
    ],
)
