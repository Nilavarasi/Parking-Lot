# Parking-Lot
This is python with flask application which is used to park and unpark the car and also check the slot.

HOW TO RUN THE APPLICATION

## Create a virtual environment
    python -m venv parking_lot  
## Activate that environment 
    source parking_lot/bin/activate
## Install requirement.txt
    pip install -r requirements.txt
## Run the application
    flask run


## Check the Routes

1. http://127.0.0.1:5000/slots?slot=5 - Slots[GET]
2. http://127.0.0.1:5000/park - Park[POST]
    postdata - {
    "vechicle_number": "AS-9531XZ"
    }
3. http://127.0.0.1:5000/unpark - unpark[POST]
    postdata - {
    "vechicle_number": "AS-9531XZ"
    }


## TEST The application
    Run the below command to test the application
        python -m pytest