import React, { Component } from 'react';
import { Text, View , TouchableOpacity} from 'react-native';

export default class HelloWorldApp extends Component {
  render() {
    return (
      <View style={{ backgroundColor:'#e9ffc945',flex: 1,
       justifyContent: "center", alignItems: "center" }}>
        <Text style={{fontSize:26, color: "#85321b45",
        fontFamily: "Courier"}}> neighborhood net </Text>
        <TouchableOpacity
          style={{
            backgroundColor:'#a4a6fc19',
            padding: 144,
            borderRadius: 19,

          }}
        >
         <Text
           style={{
             color: "white",
             fontSize: 20
           }}
         >
           </Text>
         </TouchableOpacity>
      </View>
    );
  }
}
