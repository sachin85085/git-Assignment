const express = require('express');
const path = require('path');
const app = express();
const port = 3000; // फ्रंटएंड पोर्ट 3000 पर चलेगा

// Public फोल्डर की फाइलें (HTML, CSS) दिखाने के लिए
app.use(express.static('public'));

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

app.listen(port, () => {
    console.log(`Frontend running at http://localhost:${port}`);
});