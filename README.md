# Svelte University Session

## Server
Create a virtual environment and install the required python packages:
```
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r ./test_requirements.txt
```

## Client
Install the dependencies.

```bash
cd client
yarn install
```
then start webpack:
```bash
yarn dev
```
Navigate to [localhost:3000](http://localhost:3000).

To build a production bundle:
```bash
yarn build
```

## Curl
```
curl -X POST -d '{"description":"Buy Milk", "done":false}' -H "Content-Type: application/json" "http://localhost:8080/api/todo"
curl  -H "Content-Type: application/json" "http://localhost:8080/api/todo"
```# svelte-university-session-webpack-app
