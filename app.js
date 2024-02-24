const express = require('express');
const app = express();
const port = 3000; // You can use any port that is free on your system

// Serve static files from your current directory (assuming your HTML/CSS/JS files are here)
app.use(express.static('public'));
app.use(express.static('Challenge'));

app.listen(port, () => {
  console.log(`Server listening at http://localhost:${port}`);
});



