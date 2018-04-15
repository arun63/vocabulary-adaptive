import 'package:flutter/material.dart';
import 'Meaning.dart';

void main(){
  runApp(//new Meaning());
    new MaterialApp(
    home: new Meaning(),
  ));
}

class Meaning extends StatefulWidget {

  @override
  MeaningState createState() => new MeaningState();
}

class MeaningState extends State<Meaning>{

  List<Meaning> _meanings = <Meaning>[];

  @override
  void initState() {
    // TODO: implement initState
    super.initState();
    listenForMeanings();
    //_meanings = new List.generate(100,(i) => 'Meaning $i');
  }

  listenForMeanings() async{
    var stream = await getMeaning("medicine");
    stream.listen((meaning)=>
        setState(()=>_meanings.add(meaning)));
  }

  @override
  Widget build(BuildContext context) {
    return new Scaffold(
      appBar: new AppBar(
          title: new Text('Learning Time'),
      ),
      body: new Center(
          child: new ListView(
            children: _meanings.map((meaning)=>new Text(meaning.word_name)).toList(),
          )
      ),
    );
  }
}
