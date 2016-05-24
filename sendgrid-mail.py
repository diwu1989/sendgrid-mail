#!/usr/bin/env python
import argparse
import sys
from os import environ
from StringIO import StringIO

import sendgrid

parser = argparse.ArgumentParser(prog='sendgrid-mail',
                                 description='Send a mail via sendgrid.')
parser.add_argument('--username', dest='username', help='sendgrid username',
                    default=environ.get('SENDGRID_USERNAME'))
parser.add_argument('--password', dest='password', help='sendgrid password',
                    default=environ.get('SENDGRID_PASSWORD'))

parser.add_argument('--to', action='append', help='to email address')
parser.add_argument('--from', dest='from_email', help='from email address')
parser.add_argument('--cc', action='append', help='cc email address',
                    default=[])
parser.add_argument('--bcc', action='append', help='bcc email address',
                    default=[])
parser.add_argument('--subject', help='email subject', default='')
parser.add_argument('--attachment', action='append', help='attachment',
                    type=argparse.FileType('r'))
parser.add_argument('body', nargs='?', default=sys.stdin)

args = parser.parse_args()

if isinstance(args.body, basestring):
    try:
        args.body = open(args.body, 'r')
    except IOError:
        args.body = StringIO(args.body)

client = sendgrid.SendGridClient(args.username, args.password)
message = sendgrid.Mail()
message.set_from(args.from_email)
message.set_subject(args.subject)
message.set_text(args.body.read())

for to in args.to:
    message.add_to(to)

for cc in args.cc:
    message.add_cc(cc)

for bcc in args.bcc:
    message.add_bcc(bcc)

for attachment in args.attachment:
    message.add_attachment(attachment.name, attachment)

client.send(message)
