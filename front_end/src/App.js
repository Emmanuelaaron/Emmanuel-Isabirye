import React from 'react';
import './App.css';

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      farmers: ""
    };
  }
  componentDidMount() {
    fetch('http://127.0.0.1:5000/', {
      method: 'GET',
      headers: {
        'Content_type': 'application/json',
      }
    })
      .then((response) => response.json())
      .then((data) => {
        this.setState({
          farmers: data
        })
        // console.log(data)
      })
}
  render() {
    console.log(this.state.farmers)
    return (
      <div className="App">
        <h1>Destribution of farmers in Uganda</h1>
        
        {Object.values(this.state.farmers).map(i => (
  <p>{i.district} ==> {i.number}</p>
        ))}
      </div>
    );


  }

}


export default App;
