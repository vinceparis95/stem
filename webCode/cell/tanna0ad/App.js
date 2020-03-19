import React, { Component } from 'react';
import { Text, View , TouchableOpacity} from 'react-native';

export default class HelloWorldApp extends Component {
  render() {
    // AgoraRtcEngine.createEngine('8b619bc2b58e425b8f71609495e384df');
    // AgoraRtcEngine.enableVideo();
    // AgoraRtcEngine.enableAudio();
    return (
      <View style={{ backgroundColor:'#e9ffc990',flex: 1,
       justifyContent: "center", alignItems: "center" }}>
        <Text style={{fontSize:45,fontWeight:'bold',
        letterSpacing: 14,color: "#ff840045",
        fontFamily: "Electroharmonix"}}> nucleus </Text>
        <Text style={{fontSize:19, color: "#85321b60",
        fontFamily: "Electroharmonix"}}>  </Text>
        <TouchableOpacity
          style={{
            backgroundColor:'#95ff0036',
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


//8b619bc2b58e425b8f71609495e384df
