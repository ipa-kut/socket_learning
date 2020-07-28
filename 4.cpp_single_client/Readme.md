## !!Ensure same IP and PORTs are being used by all entities!!
1. Build the two c files :   
```
gcc client.cpp -o client
gcc server.cpp -o server
```

2. Single-client, single-transaction, C++<->C++

Start the c++ server in one :
```
./server
```
Start the c++ client in another terminal :
 ```
 ./client
 ```

3. Multi-client, single-server, streamed transaction, C++<->Python

Start the multithreaded python stream server in one terminal :
```
../3.multi_client/multi-client-server-threaded.py
```
Start the c++ multi-client in another terminal :
```
 ./multi-client
 ```