'use strict';

const e = React.createElement;

class LikeButton extends React.Component {
  constructor(props) {
    super(props);
    this.state = { liked: false };
  }

  render() {

    if (this.state.liked) {
      return <div class="qops2" id="myQops2">
          <script src="{{ url_for('static', filename='js/qs_ops.js')}}"> </script>
              </div>
    }

    return (
        <button onClick={() => this.setState({ liked: true })}>
          Allahuabha</button>

    );

  }
}

const domContainer = document.querySelector('#like_button_container');
ReactDOM.render(e(LikeButton), domContainer);