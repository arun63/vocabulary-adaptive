### Adaptive Orchestration

#### Dependencies
 * Adaptive services found [here](https://gitlab.scss.tcd.ie/panthb/Elo-API-service)
 * This project will continue working without the installation of the dependency / exception handling available 

#### How to run this project
 * Ensure you have git in your machine
 * ```git clone https://gitlab.scss.tcd.ie/panthb/Orchestration-Service```
 * ```cd Orchestration-Service```
 * ```sudo pip install -r requirements.txt```
 * ```sh run.sh``` - The orchestration service will start running
 * Open Postman or any of your favourite tools
 * ```POST``` to ```localhost:4000/orchestra``` with JSON body of ```{ "player": 105, "word": 500 }```
 * Provided the dependency is running on your machine, you should be getting a response of ```{ "status": 200, "type":"hard", "word": "megalomaniac" }```

#### Contribution guidelines
 * After cloning this repository ```git checkout -b YOUR_BRANCH_NAME```
 * To obtain all branches - ```git fetch --all```
 * Kindly see to it that you make your changes in your respective branch
 * To push your changes - ```git push origin YOUR_BRANCH_NAME```