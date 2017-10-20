# Parkr backend
*By [Steve](https://github.com/HandsomeJeff)*
Backend (calculations) for real-time searching for nearest five car parks around given location.

Main logic in `/parking/checkcp.py`.

## Setup
To set it up locally, just run `python manage.py runserver` on a terminal/cmd.
The default url:port is `127.0.0.1:8000`.


To expose the local server to the world: 
1. Download and install [*ngrok*](https://ngrok.com/download).
2. Make sure *ngrok* is accesible via your *PATH*.
3. On a terminal/cmd, run `ngrok http 8000`.

## Requests
Send a `GET` request to URL`?lat=123&lon=456`.
- For local servers, default URL is `127.0.0.1:8000`.
- For exposed servers on ngrok, URL is a *random string* folloed by `.ngrok.io`.
- @param lat is latitude (float)
- @param lon is longitude (float)

## Response
Upon receiving a `GET` request with the appropriate parameters, the server will respond with a `json` package in the following format: 

```python
{"result": [{
  "short_term_parking": "WHOLE DAY", 
  "night_parking": "YES", 
  "address": "BLK 909/911 JURONG WEST STREET 91", 
  "lat": 1.341772923, 
  "total_lots_available": 153, 
  "lots_available": 27, 
  "free_parking": "SUN & PH FR 7AM-10.30PM", 
  "carpark no.": "J63", 
  "car_park_type": "SURFACE CAR PARK", 
  "lon": 103.6864428, 
  "type_of_parking": "ELECTRONIC PARKING", 
  "lots_type": "C"
  }, 
  {
  "short_term_parking": ..., 
  ...
  }
]}
```
## That is all
If you want to reach out, do send me an [email](yefan0072001@gmail.com).

