# Pyarks
Python API for getting wait time data from Amusement Parks

## APIs

### `getPark(parkName)`
Gets the specified park given a park name (supported parks listed later in the document). Returns a park object.

### `Park` (object)
Park object

### Supported Parks
- Universal Studios Florida
- Islands of Adventure
- Volcano Bay

#### Coming Soon
- Universal Studios Hollywood
- Universal Studios Japan

#### `UniversalPark.rides`
List of Ride objects correspondfing to all rides at a given park. 

### `Ride`
Base ride class

#### `Ride.park`
Park object that each Ride is part of

#### `Ride.name`
Name of the ride

#### `Ride.waitTime`
Wait time for the ride. Returns a negative value if the ride is closed or is a non-queueable ride

#### `Ride.closed`
Is the ride closed or open?

#### `Ride.isQueueable`
Is the ride queueable?

#### `isWalkthrough`
Is the ride a walkthrough?

#### `Ride.description`
Description for the ride

## Example Usage
```python
  import pyarks
  
  # Get all of the rides at Unicersal Studios in Orlando
  usf = pyarks.getPark("USF")
  
  # For each ride, print out the name and wait time
  for ride in usf.rides:
    print(ride.name, " has a wait time of ", ride.waitTime)
```
