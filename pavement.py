from paver.easy import *
from paver.setuputils import setup

setup(
    name="LawrenceCreatesBlog",
    packages=['lawrencecreatesblog'],
    version="1.0",
    url="http://blog.lawrencecreates.thefr33.com/",
    author="James Michael DuPont",
    author_email="jamesmikedupont@gmail.com",
    install_requires=[
        "django >= 1.4.10, != 1.6.0, < 1.7",
        "future == 0.9.0",
        'Mezzanine==1.4.14',
        'bleach',
        'filebrowser_safe >= 0.2.27',
        'grappelli_safe >= 0.2.22',
        'html5lib == 0.95',
        'pytz >= 2013b',
        'requests-oauthlib > 0.3.2, < 0.4',
        'requests==1.2.3',
    ],
)


