import express from 'express';
import pg from 'pg'


const client = new pg.Client()
await client.connect()


async function handleRender(req, res) {
  const result = await client.query('SELECT * from kegweights')
  await client.end()
  res.send(renderFullPage(result.rows));
}

function renderFullPage(rows) {
  return `
    <!DOCTYPE html>
    <html>
      <head>
        <title>Kegerator</title>
      </head>
      <body>
        <div id="root">
          <div>
            foo
          </div>
          <div>
            bar
          </div>
          <div>
            ${JSON.stringify(rows)}
          </div>
        </div>
      </body>
    </html>
  `;
}

const app = express();
app.use(handleRender);


const port = 3000;
app.listen(port);