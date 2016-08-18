import React, { Component } from "react";
import ReactDOM             from "react-dom";

export default class LeftColumn extends Component {
  render() {
    var containStyle = {
      width: "300px",
      // height: "100%",
      backgroundColor: "#ffc",
      borderRight: "2px solid #fe9",
      flex: "0 1 auto",
      display: "flex",
      flexDirection: "column",
      alignItems: "left",
    };
    return <div id="leftCol" style={containStyle}></div>;
  }
}
