const express = require('express');
const path = require('path');
const app = express();
const port = 3000; // The Frontend will run on this port

// Middleware to parse and understand JSON data
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Serve the 'public' folder as static (so index.html can be loaded)
app.use(express.static(path.join(__dirname, 'public')));

// Homepage route
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// Start the server
app.listen(port, () => {
    console.log(`Frontend App running at http://localhost:${port}`);
});