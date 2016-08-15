import React from "react";
import ReactDOM from "react-dom";
import Header from     "./Components/Header.js";
import LeftColumn from "./Components/LeftColumn.js";
import Content from "./Components/Content.js";
import Footer from "./Components/Footer.js"

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
