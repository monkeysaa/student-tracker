import React from 'react';
import ReactDOM from 'react-dom';

class App extends React.Component {
  // must do this every time you define constructor function inside a class-based component
  constructor(props) {
    super(props);

    this.state = { lat: null, errorMessage: '' }; // set numerical defaults to "null"
  };


  // React says we have to define render!
  // don't initialize work from the call in the render method, because its called all the dang time. 
 
  render() {
    // multiline JSX doesn't have semicolons.
    return <div> Hi! </div>
  }
}

ReactDOM.render(<App />, document.querySelector('#root'));