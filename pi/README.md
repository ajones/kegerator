

### Developing on mac

#### Setup
```
# install mac deps
brew install postgresql

# install python deps
./py_deps.sh
```

#### Local development 
```
# start up postgres 
docker-compose up -d

# run the local harness
./dev.sh
```