import React, { Component } from 'react';
import { Text, View } from 'react-native';

export default class HelloWorldApp extends Component {
  render() {
    return (
      <View style={{ backgroundColor:'#e9ffc9',flex: 1,
       justifyContent: "center", alignItems: "center" }}>
        <Text style={{fontFamily: 'Courier' ,fontSize:26}}>Allah'u'Abha :)</Text>
      </View>
    );
  }
}
