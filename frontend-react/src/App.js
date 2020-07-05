import React from 'react'
import axios from 'axios';

class App extends React.Component{
  constructor(props){
    super(props);
    this.state = {} 
    this.myCoolAfFunction = this.myCoolAfFunction.bind(this)
  }
  myCoolAfFunction(){
      axios.get('/api/profiles').then(result => {
        this.setState((prevState, props) => ({
          text: JSON.stringify(result.data)
      }))
    })

  
  }
  render(){
    return <div>
              <button onClick={this.myCoolAfFunction}>get all profile data and display here NOW! abhi chaayeee</button>
              <div>{this.state.text}</div>
          </div>
  }
}



export default App;