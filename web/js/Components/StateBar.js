import React, { Component } from "react";

export default class StateBar extends Component {
  render() {
    var containStyle = {
      display: "flex",
      flexDirection: "row",
      padding: "8px",
      width: "100%"
    };
    var stateStyle = {
      fontFamily: "'Slabo 27px', serif",
    };
    var checkStyle = {
      marginRight: "7px",
    };
    var arrowStyle = {
      WebkitUserSelect: "none",
      MozUserSelect: "none",
      msUserSelect: "none",
      marginLeft: "auto",
      marginRight: "15px",
      cursor: "pointer"
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
