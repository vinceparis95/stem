'use strict';

const e = React.createElement;

const App = () => (
    <div class={'container2'}>
        <button onClick={'newFunct()'}>haddy</button>
        <div className={'qops'} id={'myQops'}>h</div>

    </div>
);



class butter extends React.Component {
  constructor(props) {
    super(props);
    this.state = { pushed: false };
  }

  render() {

    if (this.state.pushed) {
      return App()



    }

    return (
        <button onClick={() => this.setState({ pushed: true })}>
          Allahuabha</button>

    );

  }
}

const domContainer = document.querySelector('#like_button_container');
ReactDOM.render(e(butter), domContainer);