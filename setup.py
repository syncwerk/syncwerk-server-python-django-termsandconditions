from setuptools import setup, find_packages
setup(
    name='syncwerk-server-python-django-termsandconditions',
    version='20181227',
    author='Syncwerk GmbH',
    author_email='support@syncwerk.com',
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    url='https://www.syncwerk.com',
    license='BSD',
    description='Django Terms and Conditions',
    long_description='Django Terms and Conditions gives you an configurable way to send users to a T&C acceptance page before they can access the site.',
    platforms=['any'],
    include_package_data=True,
)
