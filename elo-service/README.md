### Setup the project

 * ```sudo pip install -r requirements.txt```
 * Run the project ```FLASK_APP=main.py flask run```
 * POST ```/elo/rating/``` with the payload ```{ "player": "100", "word": "150", "win": 0 }```
 * ```win``` parameter indicates the the winner. Set ```"win": 1``` if the player has won or ```"win": 0``` if the vocabulary wins

### Run project

 * ```sh run.sh``` 

### Request

 * ```"win" : 1``` indicates the player has won and ```"win": 0``` indicates that the player has lost 

```
{
	"player": 11,
	"word": 10,
	"win": 1
}
```

```
curl -X POST http://0.0.0.0:8080/elo/ -d '{ "player": 11, "word": 10, "win": 1 }'
```

### Remote instance

```http://ec2-34-244-237-146.eu-west-1.compute.amazonaws.com:8082/elo/```
