#include <sys/types.h>
#include <sys/socket.h>
#include <sys/un.h>

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>
#include <poll.h>
#include <fcntl.h>

#define LENGTH_OF_LISTEN_QUEUE  20
#define BUFFER_SIZE 1024
#define FILE_NAME_MAX_SIZE  512

int main(int argc, char** argv)
{
    int fd0 = create_socket(0);
    int fd1 = create_socket(1);

    int ret = send(fd1, "ATTACH", 6, 0);
    printf("send ret is %d. start recv,.....\n", ret);

    struct pollfd *fds = malloc(2 * sizeof(struct pollfd));
    bzero(fds, sizeof(struct pollfd) * 2);

    int poll_cnt = 2;
    fds[0].fd = fd0;
    fds[0].events = POLLIN;
    
    fds[1].fd = fd1;
    fds[1].events = POLLIN;

    while (1)
    {
        int ret = poll(fds, poll_cnt, -1);

        if (ret < 0)
        {
            perror("poll error:");
            continue;
        }

        if (fds[0].revents & POLLIN)
        {
            char buf[256];
            ret = recv(fds[0].fd, buf, sizeof(buf), 0);
            printf("0 receive ret is %d [%s].\n", ret, buf);
        }
        
        if (fds[1].revents & POLLIN)
        {
            char buf[256];
            ret = recv(fds[1].fd, buf, sizeof(buf), 0);
            printf("1 receive ret is %d [%s].\n", ret, buf);
        }

    }
}

int create_socket(int id)
{
    char name[100];
    sprintf(name, "/var/run/hostapd/wpa_ctrl_%d", id);

    struct sockaddr_un client_addr;
    bzero(&client_addr, sizeof(client_addr));
    client_addr.sun_family = AF_UNIX;
    strncpy(client_addr.sun_path, name, sizeof(client_addr.sun_path)-1);

    int client_socket = socket(PF_UNIX, SOCK_DGRAM, 0);
    if ( client_socket < 0 )
    {
        printf("create socket failed!\n");
        return -1;
    }

    if (bind(client_socket, (struct sockaddr*)&client_addr, sizeof(client_addr)) < 0)
    {
        perror("Client bind port failed:");
        return -1;
    }

    struct sockaddr_un server_addr;
    bzero(&server_addr, sizeof(server_addr));
    server_addr.sun_family = AF_UNIX;
    strncpy(server_addr.sun_path, "/var/run/hostapd/wlan0", sizeof(server_addr.sun_path)-1);

    if (connect(client_socket, (struct sockaddr*)&server_addr, sizeof server_addr) < 0)
    {
        printf("connect failed! %s\n", strerror(errno));
        return -1;
    }

    int flags = fcntl(client_socket, F_GETFL);
    if (flags >= 0)
    {
        flags |= O_NONBLOCK;
        if (fcntl(client_socket, F_SETFL, flags) < 0)
        {

            perror("fcntl(ctrl->s, O_NONBLOCK)");
        }
    }

    return client_socket;
}
