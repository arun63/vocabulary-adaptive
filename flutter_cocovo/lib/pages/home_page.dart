import 'package:flutter/material.dart';

class HomePage extends StatelessWidget{

  @override
  Widget build(BuildContext context) {

    // TODO: implement build
//    return new Material(
//      color: Colors.blue,
//      child: new InkWell(
//        child: new Column(
//          crossAxisAlignment: CrossAxisAlignment.center,
//          mainAxisSize: MainAxisSize.max,
//          mainAxisAlignment: MainAxisAlignment.end,
//          children: <Widget>[
//            new Text("Upload a file:"),
//          ],
//        ),
//      ),
//    );
    return new MaterialApp(
      title: "Profiling the User",
      home: new ProfileScreen(),
    );
  }
}

class ProfileScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return new Scaffold(
      appBar: new AppBar(
          title: new Text("Profiling the User"),
      ),
    );
  }
}