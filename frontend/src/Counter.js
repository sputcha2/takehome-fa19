import React, { Component } from 'react'

class Counter extends Component {
  // YOUR CODE GOES BELOW
  handleDecrement = () => {
    const currentCount = this.state.count;
    this.setState({
      count: currentCount - 1;
    })
  }

  handleIncrement = () => {
    const currentCount = this.state.count;
    this.setState({
      count: currentCount + 1;
    })
  }

  render() {
    this.state = {
      count: 0
    }
    return (
      <div>
        <h> "COUNT" </h>
        <div> {this.state.count}<div/>
        <button onclick={this.handleIncrement}> Increment! </button>
        <button onclick={this.handleDecrement}> Decrement! </button>
      </div>
    )
  }
}

export default Counter
