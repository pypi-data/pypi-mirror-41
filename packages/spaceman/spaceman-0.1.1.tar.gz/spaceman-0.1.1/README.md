# Spaceman
Spaceman is the checkpoint library for funguana's internal systems. We use it to save models and internal states for later use.

## Installation

### On linux

### On Windows

### On Mac

## Usage

```python
from spaceman import Spaceman

# Declare a class to use contextually
space_man = Spaceman()

with space_man as space:
    info = space.store([{}, 1, 2]) # Returns all information pertaining the storage (location,)
    unserialized_information = space.load()

```