
const express = require('express');
const bodyParser = require('body-parser');
const { MongoClient, ObjectId } = require('mongodb'); // Make sure ObjectId is imported

const app = express();
const port = 5003;

// Middleware
app.use(bodyParser.urlencoded({ extended: true }));

// MongoDB connection URI
//const uri = "mongodb+srv://naveen:12345@ticket.mohyl.mongodb.net/?retryWrites=true&w=majority&appName=ticket";
const uri = 'mongodb+srv://kvignesh1:<your-password-no special character>@cluster0.ecb9p.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
// MongoDB client
const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true });

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/index.html');
});

// Route to add a new plant
app.post('/add-plant', async (req, res) => {
  try {
    const { PlantName, Variety, Price } = req.body;

    await client.connect();
    const database = client.db('Plant');
    const collection = database.collection('Bazzar');

    const newPlant = {
      PlantName,
      Variety,
      Price: parseInt(Price),
    };

    const result = await collection.insertOne(newPlant);
    res.send(`Plant "${PlantName}" added successfully!`);
  } catch (err) {
    res.status(500).send(`Error: ${err.message}`);
  } finally {
    await client.close();
  }
});

// Route to delete a plant by name
app.post('/delete-plant', async (req, res) => {
  try {
    const { PlantName } = req.body;

    await client.connect();
    const database = client.db('Plant');
    const collection = database.collection('Bazzar');

    const result = await collection.deleteOne({ PlantName });

    if (result.deletedCount > 0) {
      res.send(`Plant "${PlantName}" deleted successfully!`);
    } else {
      res.send(`Plant "${PlantName}" not found.`);
    }
  } catch (err) {
    res.status(500).send(`Error: ${err.message}`);
  } finally {
    await client.close();
  }
});

// Route to update the price of a plant by name
app.post('/update-plant', async (req, res) => {
  try {
    const { PlantName, NewPrice } = req.body;

    await client.connect();
    const database = client.db('Plant');
    const collection = database.collection('Bazzar');

    const result = await collection.updateOne(
      { PlantName },
      { $set: { Price: parseInt(NewPrice) } }
    );

    if (result.matchedCount > 0) {
      res.send(`Plant "${PlantName}" updated with new price: ${NewPrice}`);
    } else {
      res.send(`Plant "${PlantName}" not found.`);
    }
  } catch (err) {
    res.status(500).send(`Error: ${err.message}`);
  } finally {
    await client.close();
  }
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
 
});


