# ELSPy

ELSPy is a Python utility to communicate with Electrolux Laundry System.

Utility has been tested with Electrolux Laundry System version 1.2.0.2.

## Install

`pip install ELSPy`

## Usage

```
from ELSPy.ELS import ELS

wsdl = '<YOUR_DOMAIN_AND_PATH>/Api/Mobile/VisionMobile.asmx?WSDL'
username = '<USERNAME>'
password = '<PASSWORD>'
els = ELS(wsdl, username, password)

# Get bookable items
choises = els.get_choises()

# Get bookings info for bookable item (choise) between dateranges
bookings = els.get_bookings(2, '2019-01-22', '2019-01-23')
```

### get_choises()

Get bookable items

```
choises = els.get_choises()
```

```
[{
  'Name': 'Övernattningsrum',
  'Index': 0
}, {
  'Name': 'Tvättstuga',
  'Index': 1
}]
```

### get_bookings(choise, start_date, end_date)

Returns booking info for bookable item (choise) between dateranges.

```
bookings = els.get_bookings(2, '2019-01-22', '2019-01-23')
```

```
[{
  'BookDate': '2019-01-23',
  'BookDayPassesAmount': 3,
  'BookPasses': {
    'BookDayPass': [
      {
        'PassIndex': 3,
        'StartTime': '16:00',
        'EndTime': '19:00',
        'PassAvailability': {
          'Availability': [
            {
              'IsFree': False,
              'IsBookable': True,
              'HasAnythingBooked': False
            },
            {
              'IsFree': False,
              'IsBookable': True,
              'HasAnythingBooked': False
            },
            {
              'IsFree': True,
              'IsBookable': True,
              'HasAnythingBooked': False
            }
          ]
        }
      },
      {
        'PassIndex': 4,
        'StartTime': '19:00',
        'EndTime': '22:00',
        'PassAvailability': {
          'Availability': [
            {
              'IsFree': True,
              'IsBookable': True,
              'HasAnythingBooked': False
            },
            {
              'IsFree': True,
              'IsBookable': True,
              'HasAnythingBooked': False
            },
            {
              'IsFree': True,
              'IsBookable': True,
              'HasAnythingBooked': False
            }
          ]
        }
      }
    ]
  }
}]
```