import React, { Component } from 'react'

class App extends Component {
  // YOUR CODE GOES BELOW

  render() {
    this.props = {
      id,
      name,
      nickname,
      hobby
    }
    return (
      <div>
      contacts:
        <b> id: {id} </b>
        <b> name: {name} </b>
        <b> nickname: {nickname} </b>
        <b> hobby: {hobby} </b>
      </div>
    )
  }
}

export default App
