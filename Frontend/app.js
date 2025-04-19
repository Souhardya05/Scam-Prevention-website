const express = require("express");
const path = require("path");

const app = express();
const port = 3000;

// Middleware
app.use(express.static("public"));
app.set("view engine", "ejs");
app.set("views", path.join(__dirname, "views"));

// Route
app.get("/", (req, res) => {
  res.render("index");
});

// Start server
app.listen(port, () => {
  console.log(`🌐 Frontend running on http://localhost:${port}`);
});
