# Notifier

A simple project to send email or text notifications for when another program is done.

## Usage
Running the command 
```bash
notify
```
Will send an email to the configured addresses

To send another notification that a script or another program is complete, que the `notify` command

```
python -c "import antigravity" && notify
```

Text messages can be sent to phones whose service provider have an SMS Gateway (ie. For Bell, the SMS gateway is txt.bell.ca)

```
notify -r 6133142234@txt.bell.ca
```
## Installation

```
pip install notify-altear
```

## Setup

```
notify configure
```

The configurable options are:    
- server: the smtp server. For gmail this would be `smtp.gmail.com`
- port: the smtp port. For gmail this would be `465`
- username: the username of the account used to send the emails
- password: the password of the account used to send the emails
- recipients: comma separated email addresses
- subject: the notification subject line
- content: the notification content

## License
MIT. Copyright (c) 2019, Andre Telfer