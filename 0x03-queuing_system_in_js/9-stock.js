#!/usr/bin/yarn dev
import express from 'express';
import { promisify } from 'util';
import { createClient } from 'redis';

const listProducts = [
  { itemId: 1, itemName: 'Suitcase 250', price: 50, initialAvailableQuantity: 4 },
  { itemId: 2, itemName: 'Suitcase 450', price: 100, initialAvailableQuantity: 10 },
  { itemId: 3, itemName: 'Suitcase 650', price: 350, initialAvailableQuantity: 2 },
  { itemId: 4, itemName: 'Suitcase 1050', price: 550, initialAvailableQuantity: 5 },
];

const getItemById = (id) => listProducts.find(obj => obj.itemId === id);

const app = express();
const client = createClient();
const PORT = 1245;

const reserveStockById = async (itemId, stock) => {
  const setAsync = promisify(client.set).bind(client);
  return setAsync(`item.${itemId}`, stock);
};

const getCurrentReservedStockById = async (itemId) => {
  const getAsync = promisify(client.get).bind(client);
  return getAsync(`item.${itemId}`);
};

app.get('/list_products', (_, res) => {
  res.json(listProducts);
});

app.get('/list_products/:itemId(\\d+)', async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const productItem = getItemById(itemId);

  if (!productItem) {
    res.json({ status: 'Product not found' });
    return;
  }

  try {
    const reservedStock = parseInt(await getCurrentReservedStockById(itemId) || '0', 10);
    productItem.currentQuantity = productItem.initialAvailableQuantity - reservedStock;
    res.json(productItem);
  } catch (err) {
    res.status(500).json({ status: 'Error fetching reserved stock', error: err.toString() });
  }
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const productItem = getItemById(itemId);

  if (!productItem) {
    res.json({ status: 'Product not found' });
    return;
  }

  try {
    const reservedStock = parseInt(await getCurrentReservedStockById(itemId) || '0', 10);

    if (reservedStock >= productItem.initialAvailableQuantity) {
      res.json({ status: 'Not enough stock available', itemId });
      return;
    }

    await reserveStockById(itemId, reservedStock + 1);
    res.json({ status: 'Reservation confirmed', itemId });
  } catch (err) {
    res.status(500).json({ status: 'Error reserving product', error: err.toString() });
  }
});

const resetProductsStock = async () => {
  const setAsync = promisify(client.set).bind(client);
  const resetPromises = listProducts.map(item => setAsync(`item.${item.itemId}`, 0));
  await Promise.all(resetPromises);
};

app.listen(PORT, async () => {
  try {
    await resetProductsStock();
    console.log(`API available on localhost port ${PORT}`);
  } catch (err) {
    console.error('Error resetting product stock:', err.toString());
  }
});

export default app;
