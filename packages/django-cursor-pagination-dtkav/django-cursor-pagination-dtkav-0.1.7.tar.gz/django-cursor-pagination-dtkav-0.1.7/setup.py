from setuptools import setup


with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name='django-cursor-pagination-dtkav',
    py_modules=['cursor_pagination'],
    version='0.1.7',
    description='Cursor based pagination for Django',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Photocrowd, dtkav',
    author_email='me@danielgk.com',
    url='https://github.com/dtkav/django-cursor-pagination',
    license='BSD',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
