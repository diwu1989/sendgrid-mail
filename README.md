## sendgrid-mail
Send emails from the command line via Sendgrid.

Install via `pip install sendgrid-mail`

## usage
```sh
» ./sendgrid-mail --help
usage: sendgrid-mail [-h] [--username USERNAME] [--password PASSWORD] --to TO
                     [--from FROM] [--cc CC] [--bcc BCC] --subject SUBJECT
                     [--attachment ATTACHMENT] [--html]
                     [text]

Send an email via Sendgrid.

positional arguments:
  text

optional arguments:
  -h, --help            show this help message and exit
  --username USERNAME   sendgrid username, defaults to $SENDGRID_USERNAME
  --password PASSWORD   sendgrid password, defaults to $SENDGRID_PASSWORD
  --to TO               to email address
  --from FROM           from email address, defaults to local
  --cc CC               cc email address
  --bcc BCC             bcc email address
  --subject SUBJECT     email subject
  --attachment ATTACHMENT
                        attachment
  --html                send text as html
```

##### utilizing credentials from the environment
```sh
export SENDGRID_USERNAME=...
export SENDGRID_PASSWORD=...
echo "email content" | sendgrid-mail --to hello@world.com --subject test
```

##### sending text email
```sh
echo "Hello World" > myfile
sendgrid-mail --to hello@world.com --subject test myfile
```

##### sending attachment with html content
```sh
echo "Attachment 1" > attachment1
echo "<b>hello world</b>" > content
sendgrid-mail --to hello@world.com --subject test --attachment attachment1 content --html
```
