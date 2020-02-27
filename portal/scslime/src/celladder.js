import React from 'react';
import ReactDOM from 'react-dom';

class Cell extends React.Component {
    render() {
        return (
            <form>

                <input
                    type="text" style={{
                        display:'flex',
                    position:'relative',
                        top: '-360px',
                    right:'95px',
                    fontFamily: "VT323",
                    width:'144px',
                    fontSize:'36px',
                    color: 'rgb(115,38,0)',
                    opacity:'60%',
                    borderRadius: '9px',
                    height: '45px',
                    background: 'radial-gradient(rgba(196, 181, 255, .9), rgba(168,255,0,0.19)',
                    borderColor: 'rgba(255,255,255,0)'
                }}
                />
            </form>
        );
    }
}
 // ReactDOM.render(<Cell />, document.getElementById('root2'));


export default Cell