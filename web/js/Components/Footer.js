import React, { Component } from "react";
import ReactDOM from "react-dom";

export default class Header extends Component {
  render() {
    var containStyle = {
      width: "100%",
      height: "40px",
      backgroundColor: "#fe9",
      borderTop: "2px solid #fc0",
      display: "flex",
      flexDirection: "row",
      alignItems: "center",
      justifyContent: "space-around"
    };
    var logoStyle = {
      color: "#222",
      fontFamily: "'Quicksand', sans-serif",
      fontSize: "12px"
    }
    var rightDivStyle = {
      width: "200px"
    }
    return <div style={containStyle}><div style={logoStyle}>[ ]BNB is for educational purposes only.</div></div>;
  }
}
