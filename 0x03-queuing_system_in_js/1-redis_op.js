#!/usr/bin/yarn dev
import { createClient, print } from 'redis';

const client = createClient();

client.on('error', (err) => {
  console.error('Redis client not connected to the server:', err.toString());
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, print);
};

const displaySchoolValue = (schoolName) => {
  client.get(schoolName, (err, reply) => {
    if (err) {
      console.error('Error retrieving value:', err.toString());
    } else {
      console.log(`${schoolName}: ${reply}`);
    }
  });
};

// Setting and displaying school values
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('Holberton');
displaySchoolValue('HolbertonSanFrancisco');
