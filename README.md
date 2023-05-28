# Stress test environment

It is to automate the stress testing of a Web app.

## Dependencies

* Python >= 3.11
* Locust

## How to use

You should check [the docs of Locust](https://locust.io/) first.

### Run it locally (with one node)

```bash
# Install dependencies (Only once)
$ pip install -r requirements.txt
  
# Set up the scenario
$ SCENARIO=sample # Scenario you want to run
$ TARGET_HOST=http://localhost:8080 # Target host you will send stress
$ SPAWN_RATE=20 # How many users you will create in a sec
$ USERS=100 # How many users you will create at max

# Run the scenario
$ locust -f scenario/${SCENARIO}/locustfile.py --host=${TARGET_HOST} --spawn-rate=${SPAWN_RATE} --users=${USERS}
```

### Run it through Docker Compose

```bash
# Set up the scenario
$ export SCENARIO=sample # Scenario you want to run
$ export TARGET_HOST=http://localhost:8080 # Target host you will send stress
$ export SPAWN_RATE=20 # How many users you will create in a sec
$ export USERS=100 # How many users you will create at max
$ export RUN_TIME=1m # How long it will send stress. E.g. (300s, 20m, 3h, 1h30m, etc.)
$ NUM_OF_WORKER=4 # Change the num of worker nodes according to your machine's CPU cores

# Run the scenario
$ docker compose up --build --scale worker=${NUM_OF_WORKER}
```