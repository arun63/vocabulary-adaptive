import 'package:flutter/material.dart';

void main(){
  runApp(new MaterialApp(
    home: new QuestionPage(),
  ));
}



class QuestionPage extends StatefulWidget {

  @override
  QuestionState createState() => new QuestionState();
}

class QuestionState extends State<QuestionPage>{

  int _selected = 0;
  void onChanged(int value){
    setState((){
      _selected = value;
    });
    print('Value = $value');
  }
  List<Widget> makeRadios() {
    List<Widget> list = new List<Widget>();
    list.add(new Column(
      children: <Widget>[
        new Text('Question:',
          style: new TextStyle(fontFamily: 'Raleway',fontSize: 40.0),textAlign: TextAlign.center,),
        new Text(' ',
          style: new TextStyle(fontFamily: 'Raleway',fontSize: 25.0),textAlign: TextAlign.center,),
        new Text('Serendipity?',
          style: new TextStyle(fontFamily: 'Raleway',fontSize: 30.0),textAlign: TextAlign.left,),
        new Text(' ',
          style: new TextStyle(fontFamily: 'Raleway',fontSize: 20.0),textAlign: TextAlign.center,),
      ]
    )
    );
        for (int i = 0; i < 4; i++) {
      list.add(new Row(
                  children: <Widget>[
                    new Radio(value: i, groupValue: _selected, onChanged: (int value) {
                      onChanged(value);
                  }),
                    new Text('Option $i')
                    ],
            )
      );
    }
    return list;
  }


  @override
  Widget build(BuildContext context) {
    return new Scaffold(
      appBar: new AppBar(title: new Text('Knowledge Testing Time'),
      ),
      body: new Container(

        padding: new EdgeInsets.all(32.0),
        child: new Center(
          child: new Column(
            children: makeRadios(),
          ),
        ),
      ),
    );
  }
}