# Customize this file for your specific configuration.
# You *must* change ACTIVATED and SECRET.
#
# The URL to use for the dump is DUMP_URL?SECRET
# If SECRET is empty, DUMP_URL is enough.
#
# *** NOTE ABOUT SECURITY ***
#
# No Zope access control is done on this URL, as it is interpreted
# before the Zope application server comes into play. That's why you
# should change the secret or filter this URL before it gets to Zope,
# for instance in Apache.

import os

SECRET = os.environ.get('ZOPE_HEALTH_WATCHER_SECRET')
ACTIVATED = bool(SECRET)
DUMP_URL = '/manage_zhw'
