import tempfile
import uuid
from argparse import ArgumentParser

import jsonpickle

from vr900connector.vaillantsystemmanager import VaillantSystemManager


def print_system(user, password, new_session, file):
    if new_session:
        manager = VaillantSystemManager(user, password, file_dir=tempfile.gettempdir() + "/" + str(uuid.uuid4()))
    else:
        manager = VaillantSystemManager(user, password)
    system = manager.get_system()

    jsonpickle.set_encoder_options('simplejson', sort_keys=True, indent=4)
    output = jsonpickle.encode(system)

    if file:
        with open(file, 'w+') as file:
            file.write(output)
    else:
        print(output)

    manager.logout()


if __name__ == '__main__':
    parser = ArgumentParser(description=__doc__)

    parser.add_argument('--username', '-u', help='Username used to connect', dest='username',
                        required=True)
    parser.add_argument('--password', '-p', help='Password used to connect', dest='password',
                        required=True)
    # parser.add_argument('--new-session', '-ns',
    #                     help='Specify if you want new session, if not provided, the connector '
    #                          'will use the default location to store cookies and serial '
    #                          'number. The connector will reuse files if they exist, '
    #                          'so username/password won\'t be used',
    #                     dest='new_session', required=False, action='store_true')
    parser.add_argument('--file', '-f', help='Specify file name where to save output', dest='file',
                        required=False)

    args = parser.parse_args()
    print_system(args.username, args.password, args.new_session, args.file)
