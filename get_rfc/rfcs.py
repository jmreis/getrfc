# MIT License
#
# Copyright (c) 2020 Jair Reis <jmsrdebian@protonmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
"""A simple module for get RFC from site www.ietf.org.
This module use a simple request for download the RFC in
.txt format. Other functionality is the list of RFC for
get your number and descripitions.
"""

import sys
import urllib.request
from get_rfc.rfcs_list import all_rfcs

__all__ = ['rfc_help', 'list_rfc', 'get_rfc']
__version__ = '0.0.1'
__author__ = 'Jair Reis'


def rfc_help():
    """
    A function for print usage of the module.

    Usage:
    ------
            getrfc -h
            getrfc --help

    Tests:
    >>> help()

    """
    # Information for help the users
    print(
        """\033[31m
           _____      _   _____  ______ _____
          / ____|    | | |  __ \|  ____/ ____|
         | |  __  ___| |_| |__) | |__ | |
         | | |_ |/ _ \ __|  _  /|  __|| |
         | |__| |  __/ |_| | \ \| |   | |____
          \_____|\___|\__|_|  \_\_|    \_____|
        ---------------------------------------\033[m
        Usage:
        ------
            getrfc <arguments>

            Arguments:

                    -h  or --help   print help information
                    <RFC number>    print the RFC
                    -l  or --list   print the RFC list
        """
    )


def list_rfc():
    """
    A function for print the RFC list.

    Usage:
    ------
            getrfc --list or
            getrfc -l
    Tests:
    ------
    >>> list_rfc()
    """

    rfc_list = all_rfcs
    # List of RFC for users
    print(rfc_list)


def get_rfc():
    """A function for get the RFC from IETF site.

    Usage:
    ------
            getrfc <RFC number>
    Tests:
    ------
    >>> os.system('python3 rfc_download.py 8391')

    >>> os.system('python3 rfc_download.py 20')
    """
    try:
        rfc_number = int(sys.argv[1])
    except (IndexError, ValueError):
        help()
        sys.exit(2)

    url = f'https://www.ietf.org/rfc/rfc{rfc_number}.txt'
    # Getting the RFC from url
    try:
        rfc_raw = urllib.request.urlopen(url).read()
        rfc = rfc_raw.decode()
        print(rfc)
    except HTTPError as e:
        print('The server couldn\'t fulfill the request.')
        print('Error code: ', e.code)
    except URLError as e:
        print('We failed to reach a server.')
        print('Reason: ', e.reason)
