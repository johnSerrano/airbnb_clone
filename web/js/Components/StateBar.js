import React, { Component } from "react";

export default class StateBar extends Component {
  render() {
    var containStyle = {
      display: "flex",
      flexDirection: "row",
      padding: "5px",
      width: "100%"
    };
    var stateStyle = {
      fontFamily: "Quicksand",
    };
    var checkStyle = {
      marginRight: "7px"
    };
    var arrowStyle = {
      marginLeft: "auto",
      marginRight: "15px"
    };
    return <div id="top" style={containStyle}>
              <input type="checkbox" style={checkStyle} />
              <div style={stateStyle}>
                {this.props.name}
              </div>
              <div style={arrowStyle}>
              <i className="material-icons">add</i>
              </div>
            </div>;
  }
}
