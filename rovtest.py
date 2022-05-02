# from inputs import devices
# from inputs import get_gamepad
import pygame
import socket
import serial
import sys

# for device in devices:
#     print(device)

pygame.init()

display = pygame.display.set_mode((600, 600))



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print(socket.gethostbyname(socket.gethostname()))

s.bind(('192.168.68.102', 5050))

print(socket.gethostbyname(socket.gethostname()))
#s.bind(('10.81.15.219', 5050))





def netcat(content):
	clientsocket.send(content.encode())

s.listen(1)

clientsocket , address = s.accept()

print("passe")


while 1:


	pressed_keys = pygame.key.get_pressed()

	for event in pygame.event.get():


		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

		if event.type == pygame.KEYDOWN:

			if event.key == pygame.K_w:
				netcat('foward')

			elif event.key == pygame.K_s:
				netcat('backward')


			if event.key == pygame.K_d:
				netcat('right')

			elif event.key == pygame.K_a:
				netcat('left')

			if event.key == pygame.K_UP:
				netcat('up')

			if event.key == pygame.K_DOWN:
				netcat('down')

			if event.key == pygame.K_RIGHT:
				netcat('up1')

			elif event.key == pygame.K_LEFT:
				netcat('up2')

			if event.key == pygame.K_SPACE:
				netcat('open')

			elif event.key == pygame.K_m:
				netcat('close')



		if event.type == pygame.KEYUP:

			if event.key == pygame.K_w and pressed_keys[pygame.K_s] == False:
				netcat('zstop')

			if event.key == pygame.K_s and pressed_keys[pygame.K_w] == False:
				netcat('zstop')

			if event.key == pygame.K_d and pressed_keys[pygame.K_a] == False:
				netcat('xstop')

			if event.key == pygame.K_a and pressed_keys[pygame.K_d] == False:
				netcat('xstop')

			if event.key == pygame.K_UP and pressed_keys[pygame.K_DOWN] == False:
				netcat('ystop')

			if event.key == pygame.K_DOWN and pressed_keys[pygame.K_UP] == False:
				netcat('ystop')

			if event.key == pygame.K_RIGHT and pressed_keys[pygame.K_LEFT] == False:
				netcat('ystop')

			if event.key == pygame.K_LEFT and pressed_keys[pygame.K_RIGHT] == False:
				netcat('ystop')









    # for event in events:
            
    #     if event.code == "ABS_Y":
 
    #         if(event.state < 20):

    #             netcat('192.168.2.2', 40000, 'foward')
                
                
    #         elif(event.state > 150):

    #             netcat('192.168.2.2', 40000, 'backward')
                    
    #         else:
                    

    #             netcat('192.168.2.2', 40000, 'zstop')


    #         if event.code == "ABS_X":

    #             if(event.state < 20):

    #                 netcat('192.168.2.2', 40000, 'left')

    #             elif(event.state > 150):

    #                 netcat('192.168.2.2', 40000, 'right')
                    
    #             else:

    #                 netcat('192.168.2.2', 40000, 'xstop')



    #         if event.code == "ABS_RZ":
                
    #             if(event.state < 20):

    #                 netcat('192.168.2.2', 40000, 'up')
                    
    #             elif(event.state > 150):

    #                 netcat('192.168.2.2', 40000, 'down')

 	# 			  else:
    # 				netcat('192.168.2.2', 40000, 'ystop')




