import React      from "react";
import ReactDOM   from "react-dom";
import Header     from "./Components/Header.js";
import LeftColumn from "./Components/LeftColumn.js";
import Content    from "./Components/Content.js";
import Footer     from "./Components/Footer.js";
import Api        from "./api.js"

// Style definitions
document.body.style.margin = 0;
document.body.style.height = "100%";
document.body.style.width = "100%";
document.getElementById("root").style.height = "100%";
document.getElementById("root").style.width = "100%";

var topStyle = {
  height: "100%",
  display: "flex",
  flexDirection: "Column"
}
var midStyle = {
  flex: "1 1 auto",
  display: "flex",
  flexDirection: "row",
}


// Create the document
ReactDOM.render(
  <div style={topStyle}>
    <Header />
    <div style={midStyle}>
      <LeftColumn />
      <Content />
    </div>
    <Footer />
  </div>,
  document.getElementById("root")
)

// Create the Api object for dynamic content.
var api = new Api();

// Create the states menu in the left column.
// "leftCol" is the id of the left column.
api.populateStateBars("leftCol");
