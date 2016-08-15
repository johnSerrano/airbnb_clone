import React, { Component } from "react";
import ReactDOM from "react-dom";

export default class Header extends Component {
  render() {
    var containStyle = {
      width: "100%",
      height: "60px",
      backgroundColor: "#fe9",
      borderBottom: "2px solid #fc0",
      display: "flex",
      flexDirection: "row",
      alignItems: "center",
      justifyContent: "space-between"
    };
    var logoStyle = {
      color: "#222",
      padding: "5px",
      fontFamily: "'Quicksand', sans-serif",
      fontSize: "24px"
    }
    var rightDivStyle = {
      width: "200px"
    }
    return <div style={containStyle}><div style={logoStyle}>[ ]BNB</div><div style={rightDivStyle}>RightDiv</div></div>;
  }
}
