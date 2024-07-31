#!/usr/bin/yarn dev
import { createClient } from 'redis';

const client = createClient();

client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

const publishMessage = (message, delay) => {
  setTimeout(() => {
    console.log(`About to send: ${message}`);
    client.publish('holberton school channel', message, (err) => {
      if (err) {
        console.error(`Failed to publish message: ${message}`, err.toString());
      }
    });
  }, delay);
};

// Schedule messages to be published
publishMessage('Holberton Student #1 starts course', 100);
publishMessage('Holberton Student #2 starts course', 200);
publishMessage('KILL_SERVER', 300);
publishMessage('Holberton Student #3 starts course', 400);
