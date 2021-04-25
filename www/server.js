import express from 'express';
import pg from 'pg'
import pug from 'pug'

// database connection
const client = new pg.Client()
await client.connect()


async function handleRender(req, res) {
  const result = await client.query('SELECT * from kegweights')
  await client.end()

  var html = pug.renderFile('./views/index.pug', {rows:result.rows});

  res.send(html);
}

const app = express();
app.use(handleRender);


const port = 3000;
app.listen(port);