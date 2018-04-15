//import 'package:flutter/material.dart';
//import 'pages/home_page.dart';
//
//void main(){
//
//  runApp(new MaterialApp(
//      home: new HomePage(),
//  ));
//
//}

import 'package:flutter/material.dart';

//class UserProfileCreation extends StatelessWidget {
class UserProfileCreation extends StatefulWidget {

  @override
  Entry createState() => new Entry();
}

class Entry extends State<UserProfileCreation> {
  String _value = null;
  List<String> values = new List<String>();
  String text_Easy = '''            Fitness:Strongman's Fear
                      On Saturday August 5th, 40 men and 40 women 
                       competed to win an athletic event called Strongman's
                       Fear. Nearly 400,000 other athletes tried to 
                       qualify to compete in this event, but only 
                       these 80 competitors succeeded.
                       
                       Over 16,000 spectators surrounded the venue,
                       either in the stands or watching giant screens
                       set up around the Alliant Energy Center in 
                       Madison, Wisconsin. Millions more watched 
                       the event online or on CBS Sports.

                       That's a very big audience for something 
                       you probably haven't heard of. But you have 
                       heard of CrossFit. And Strongman's Fear was 
                       one of 13 events that made up the 2017 Reebok 
                       CrossFit Games.''';
  String text_Intermediate = '''         Science:Killer AI boycott row shows there is 
                                                 research we can’t accept
                                                 
                                A South Korean university has dismissed fears it would work on killer robots. The dispute reflects 
                                growing worries over autonomous weapons, says Paul Marks.
                                When artificial intelligence and death meet, a flood of headlines 
                                is rarely far behind. Last month, they were about a self-driving 
                                Uber that ran over and killed a woman as she crossed a road in 
                                Arizona. And then a Tesla, driven by its software, hit a central 
                                reservation in the US, killing the driver.                 
                                ''';
  String text_Difficult = '''     Journal of Home Science
                                                
                        International Journal of Home Science is 
                        an official journal of International Association
                        Trust (Regd. No. Registration No. 834/2014-2015/4).
                        Prime Focus of the Journal is to publish articles
                        related to the current trends of research. This
                        Journal provides platform with the aim of 
                        motivating students and personnel in home 
                        science and allied subjects research.

                        International Journal of Home Science considers
                        review and research articles related to: 
                        Child Development, Community Living, Family 
                        Resource Management, Family Health and Nutrition,
                        Food Packaging and Storage, Clothing and 
                        Textiles, Home Economics, Home Management, 
                        Human Resource Development, Home Science 
                        Extension and Education, and other topics 
                        related to Home Sciences.
                        ''';
  String text_set = "";

  @override
  void initState() {
    values.addAll(["","Easy", "Intermediate", "Difficult"]);
    _value = values.elementAt(0);

    //super.initState();
  }

  void Onchanged(String value) {
    setState(() {
      _value = value;
      //textData = value;
      if(value=="Easy"){
        text_set = text_Easy;
      }else if(value=="Intermediate"){
        text_set = text_Intermediate;
      }else if(value=="Difficult"){
        text_set = text_Difficult;
      }else
        text_set = "";
    });
  }

  Widget build(BuildContext context) {
    return new MaterialApp(
      home: new Scaffold(
        appBar: new AppBar(
          title: const Text('User Profiling'),
        ),
        body: new Container(

          padding: new EdgeInsets.all(32.0),
          child: new Column(
            children: <Widget>[
              new Text('Choose a file to generate user profile:',
                style: new TextStyle(fontWeight: FontWeight.bold),),
              new DropdownButton(
                value: _value,
                items: values.map((String value) {
                  return new DropdownMenuItem(
                    value: value,
                    child: new Row(
                      children: <Widget>[
                        new Text('${value}')
                      ],
                    ),
                  );
                }).toList(),
                onChanged: (String value) {
                  Onchanged(value);
                },
              ),
              new Expanded(
                  child: new Text('$text_set',
                    textAlign: TextAlign.center,
                    //overflow: TextOverflow.ellipsis,
                    style: new TextStyle(fontWeight: FontWeight.bold)))
            ],
          ),
        ),
      ),
    );
  }
}

                    //items: values.map(String value){
                    //  return new DropdownMenuItem(
                    //    value: value,),

                      
//    }
//}


//  @override
//  Widget build(BuildContext context) {
//    return new MaterialApp(
//      home: new Scaffold(
//        appBar: new AppBar(
//          title: const Text('User Profiling'),
//        ),
//        body: new Container(
//
//          padding: new EdgeInsets.all(32.0),
//          child: new Column(
//            children: <Widget>[
//              new Text('Choose a file to generate user profile:',
//              style: new TextStyle(fontWeight: FontWeight.bold),),
////              new Expanded(
////                  child: new ListView.builder(
////                    itemBuilder: (BuildContext context, int index) => new EntryItem(data[index]),
////                    itemCount: data.length,
////                  ),
////              ),
//              new DropdownButton(items: , onChanged: null)
//            ],
//          ),
//
//        )
//
//
//      ),
//    );
//  }
//}

//// One entry in the multilevel list displayed by this app.
//class Entry {
//  Entry(this.title, [this.children = const <Entry>[]]);
//  final String title;
//  final List<Entry> children;
//}

// The entire multilevel list displayed by this app.
//final List<Entry> data = <Entry>[
//  new Entry('',
//  <Entry>[
//  new Entry('Easy.txt'),
//  new Entry('Medium.txt'),
//  new Entry('Difficult.txt'),],),





//    <Entry>[
//      new Entry('Section A0',
//        <Entry>[
//          new Entry('Item A0.1'),
//          new Entry('Item A0.2'),
//          new Entry('Item A0.3'),
//        ],
//      ),
//      new Entry('Section A1'),
//      new Entry('Section A2'),
//    ],
//  ),
//  new Entry('Chapter B',
//    <Entry>[
//      new Entry('Section B0'),
//      new Entry('Section B1'),
//    ],
//  ),
//  new Entry('Chapter C',
//    <Entry>[
//      new Entry('Section C0'),
//      new Entry('Section C1'),
//      new Entry('Section C2',
//        <Entry>[
//          new Entry('Item C2.0'),
//          new Entry('Item C2.1'),
//          new Entry('Item C2.2'),
//          new Entry('Item C2.3'),
//        ],
//      ),
//    ],




//];



// Displays one Entry. If the entry has children then it's displayed
// with an ExpansionTile.

//class EntryItem extends StatelessWidget {
//  const EntryItem(this.entry);
//
//  final Entry entry;
//
//  Widget _buildTiles(Entry root) {
//    if (root.children.isEmpty)
//      return new ListTile(title: new Text(root.title));
//    return new ExpansionTile(
//      key: new PageStorageKey<Entry>(root),
//      title: new Text(root.title),
//      children: root.children.map(_buildTiles).toList(),
//    );
//  }
//
//  @override
//  Widget build(BuildContext context) {
//    return _buildTiles(entry);
//  }
//}

void main() {
  runApp(new UserProfileCreation());
}