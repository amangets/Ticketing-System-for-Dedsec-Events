# Ticketing System for Dedsec Events

**Created by:** Aman Adam Louis  
**Date:** 23/07/24

## Background

As a computer science student involved in event management and planning in my off-time, my team and I faced significant challenges with ticketing. Customers always preferred having a physical ticket. Although several online solutions exist, they are prohibitively expensive for our local business.

To address this, I developed two programs:
1. **ticket_generator.py**: Generates QR codes with randomized, non-serial numbers and stores the valid keys in a file named `valid_keys.txt`.
2. **ticket_validator.py**: Validates QR codes by checking if they have been used before or if they are fake.

## File Descriptions

### 1. `ticket_generator.py`

- **Purpose**: Generates QR codes and stores the valid keys in `valid_keys.txt`.
- **Functionality**: Uses a random number generator to create unique QR codes.

### 2. `ticket_validator.py`

- **Purpose**: Validates QR codes scanned by a third-party device.
- **Functionality**:
  - Checks if the QR key is present in `used_keys` (indicating it has been used before).
  - Checks if the key is not present in `valid_keys` (indicating it is a fake).

## Note

After `ticket_generator.py` has generated a set of tickets, you can continue generating more tickets as long as the random number generator has not exhausted its range. If the `randrange` function hits its limit, a deadlock may occur.
