import React from 'react';
import './App.css';

const Score = {
  title: "circuit",
  qubits: [
    "alice teleport",
    "alice ep",
    "bob ep"
  ],
}


function createScore(slide) {

  return ( <
      div style = {
          {
            backgroundColor: 'rgba(168, 235, 52,0.00)',
            margin: '19px',
            padding:'19px',
            fontFamily: 'Courier',
            color: 'rgba(255, 136, 0,1)',
            fontSize:'19px',
            letterSpacing:'5px',
            borderRadius:'0%',

          }
        } >
        <
        h1 title = {
          Score.title
        }
      /> <
      ul > {
        Score.qubits.map(qubit => < li > {
            qubit
          } < /li>)} < /
          ul >
          <
          button style = {
            {
              height: '180px',
              width: '180px',
              backgroundColor:'#E0E5EC',
              boxShadow: '9px 9px 16px rgb(163,177,198,0.6), -9px -9px 16px    rgba(255,255,255, 0.5)',
              borderRadius: '9%',
              margin: '19px',
              padding:'19px',
              opacity: '.39',
              outline:'none',
              fontFamily: 'Courier',
              letterSpacing: '5px',
              fontSize: '27px',
              fontWeight:'bold',
              color: 'rgba(255, 136, 0,1)'
            }
          } > add qubit < /button>    < /
        div >
      )

      }
createScore(Score)

export default createScore
