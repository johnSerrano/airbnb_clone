import React, { Component } from "react";
import ReactDOM from "react-dom";

export default class Header extends Component {
  render() {
    var containStyle = {
      width: "100%",
      height: "60px",
      backgroundColor: "#fc0"
    };
    return <div style={containStyle}>HEADER</div>;
  }
}
