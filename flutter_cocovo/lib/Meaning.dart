import 'dart:convert';
import 'dart:async';
import 'package:http/http.dart' as http;
//import 'key.dart';

main(){
  getMeaning('Trinity');
}

class Meaning{

  final String word_name;
  final String word_meaning;
  final String word_synonyms;

  Meaning.fromJson(Map jsonMap):
        word_name = jsonMap['word_name'],
        word_meaning=jsonMap['word_meaning'],
        word_synonyms=jsonMap['word_synonyms'];
  String toString() => 'Meaning: $word_name';


}

Future<Stream<Meaning>>getMeaning(String word) async{

  var url = 'http://ec2-34-244-237-146.eu-west-1.compute.amazonaws.com:8083'+
      '/question'+'?words=$word'+'&key=e205e2cd-f8f8-b95a-0997-5657ecf312e8';
  /*
  http.put(url).then(
      (res)=>print(res.body)
  );*/

  var client = new http.Client();
  var streamedRes = await client.send(

    new http.Request('put', Uri.parse(url))
  );

  return streamedRes.stream.transform(UTF8.decoder)
      .transform(JSON.decoder)
      .expand((jsonBody)=>(jsonBody as Map)['results'])
      .map((jsonMeaning)=>new Meaning.fromJson(jsonMeaning));
//      .listen((data)=>print(data))
//      .onDone(()=>client.close());


}