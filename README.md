# OnlyPlans
## A prosocial network
An experiment in non-addictive social network that facilitates actually meeting people.

### Notes to self
To restart the server:
```PID=$(systemctl show --value -p MainPID gunicorn.service) && kill -HUP $PID