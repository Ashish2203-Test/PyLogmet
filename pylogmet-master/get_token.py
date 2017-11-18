from __future__ import print_function

import argparse
import getpass
import urllib
import urllib.parse
import urllib.request
try: input = raw_input
except NameError: pass
DEFAULT_ENDPOINT = 'logmet.ng.bluemix.net'

def _parse_args():
    p = argparse.ArgumentParser()
    p.add_argument('--endpoint', '-e', default=DEFAULT_ENDPOINT)
    return p.parse_args()


def main():
    args = _parse_args()

    logmet_endpoint = args.endpoint
    if logmet_endpoint == DEFAULT_ENDPOINT:
        print('Using default endpoint [%s]. Use --endpoint to change.' %
              logmet_endpoint)

    org_name = input('Org Name: ')
    space_name = input('Space Name: ')
    username = input('Username: ')
    passwd = getpass.getpass()

    form_data = urllib.parse.urlencode(
        {'user': username,
         'passwd': passwd,
         'space': space_name,
         'organization': org_name})

    binary_data = form_data.encode('ascii')

    url = 'https://%s/login' % logmet_endpoint
    print('Authenticating with [%s] ...' % url)
    resp = urllib.request.urlopen(url=url, data=binary_data, timeout=20)

    if resp.getcode() == 200:
        print('[200 OK] Success!')
        print("Use 'logging_token' and 'space_id' from below to feed metrics/logs into Logmet.")
    else:
        print('There was an error processing your request. :(')
        print('Got HTTP %s' % resp.getcode())

    print(resp.read())

if __name__ == '__main__':
    main()
