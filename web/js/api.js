import { ENVIRONMENT } from "./Constants.js";
import ReactDOM from "react-dom";
import React from "react";
import StateBar from "./Components/StateBar.js";

// API for my backend API
export default class Api {
  constructor() {
    this.url = "http://localhost:3000";
    switch (ENVIRONMENT) {
      case "prod":
        this.url = "http://webone.johnserrano.tech:21";
      case "dev":
        this.url = "http://webone.johnserrano.tech:3333";
        break;
      case "test":
        this.url = "http://localhost:5555";
        break;
      default:
        throw ENVIRONMENT + " is not a valid environment.";
    }
  }

  // Pagination does not exist in the api currently.
  // So for future compatibility page is taken as a parameter, but for now
  //  it is ignored.
  // onComplete is the callback that will be run after getting the states.
  // TODO: use jquery somewhere else so I feel justified for importing it
  getStates(page, onComplete) {
    $.getJSON(this.url + "/states", null, onComplete);
  }

  // Populates the left column with states.
  // "leftColId" is the ID of the left column, which should be defined in
  //  Components/LeftColumn.js
  populateStateBars(leftColId) {
    this.getStates(0, function(data) {
      var leftcol = document.getElementById(leftColId);

      var states = []
      for (var i = 0; i < data["states"].length; i++) {
        states.push(<StateBar name={data["states"][i]["name"]} key={i} />);
        console.log(data["states"][i]["name"]);
      }
      // Create the StateBars in the left column
      ReactDOM.render(<div>{
        states.map(function (state, i) {
          return state;
        })
      }
        </div>, leftcol);
    })
  }
}
