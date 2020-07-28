// Source: https://www.geeksforgeeks.org/socket-programming-cc/
// Two sockets to same server
// Client side C/C++ program to demonstrate Socket programming 
#include <stdio.h> 
#include <sys/socket.h> 
#include <arpa/inet.h> 
#include <unistd.h> 
#include <string.h> 
#define PORT 65432 
   
int main(int argc, char const *argv[]) 
{ 
    int sock1 = 0, valread1; 
    int sock2 = 0, valread2;
    struct sockaddr_in serv_addr; 
    char *hello = "Hello from client"; 
    char buffer[1024] = {0}; 
    if ((sock1 = socket(AF_INET, SOCK_STREAM, 0)) < 0) 
    { 
        printf("\n Socket1 creation error \n"); 
        return -1; 
    } 
    if ((sock2 = socket(AF_INET, SOCK_STREAM, 0)) < 0) 
    { 
        printf("\n Socket2 creation error \n"); 
        return -1; 
    } 

    serv_addr.sin_family = AF_INET; 
    serv_addr.sin_port = htons(PORT); 
       
    // Convert IPv4 and IPv6 addresses from text to binary form 
    if(inet_pton(AF_INET, "127.0.0.1", &serv_addr.sin_addr)<=0)  
    { 
        printf("\nInvalid address/ Address not supported \n"); 
        return -1; 
    } 
   
    if (connect(sock1, (struct sockaddr *)&serv_addr, sizeof(serv_addr)) < 0) 
    { 
        printf("\n Socket1 Connection Failed \n"); 
        return -1; 
    } 
    if (connect(sock2, (struct sockaddr *)&serv_addr, sizeof(serv_addr)) < 0) 
    { 
        printf("\n Socket2 Connection Failed \n"); 
        return -1; 
    } 
    while(1)
    {
        send(sock1 , hello , strlen(hello) , 0 ); 
        printf("Hello1 message sent\n"); 
        valread1 = read( sock1 , buffer, 1024); 
        printf("%s\n",buffer ); 
        
        send(sock2 , hello , strlen(hello) , 0 ); 
        printf("Hello2 message sent\n"); 
        valread2 = read( sock2 , buffer, 1024); 
        printf("%s\n",buffer ); 

        printf("---\n");
    }
    return 0; 
} 

