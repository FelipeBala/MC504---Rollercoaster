import threading
import pygame
import caracteres
import time

entra_no_trem = threading.Lock()
sai_do_trem = threading.Lock()
ha_trem = threading.Condition()
chegou_trem = threading.Condition()
parte_trem = threading.Condition()
fila = threading.Lock()
fila2 = threading.Lock()
fila3 = threading.Lock()
LL = threading.Condition()

pessoas_sentadas = 0
pessoas_fila = 0
trem = 0

#---------Input de parametros ---------
a = int(input("Max pessoas na Fila"))
b = int(input("Max pessoas no Trem"))
c = float(input("Tempo de passeo do Trem"))
d = float(input("Tempo de Spawn das Pessoas "))
e = float(input("Velocidade das pessoas (ms)"))

e = e/1000

caracteres.rollercoaster.inicia_parametros(a,b)
caracteres.personagem.inicia_parametros(e)
lugares = threading.Semaphore(b)
#------------------------------------------

pygame.init()
screen = pygame.display.set_mode([1038, 718])
#screen = pygame.display.set_mode([800, 600])
background_image = pygame.image.load("background.jpg").convert()
imagem_trem = pygame.image.load("trem.jpg").convert()
grafico = caracteres.grafica(screen,LL,background_image,imagem_trem)
pygame.display.set_caption('Teste')
clock = pygame.time.Clock()
base = caracteres.inicia_personagens() 

def pessoa(num):
	global grafico
	global screen
	global base
	global pessoas_fila
	global pessoas_sentadas
	global b
	global trem
	
	#Inicia
	u = num % 8 +1
	personagem1 = caracteres.personagem(base.imagem,u,screen,grafico,num)
	personagem1.pos_init(120,0)
	p1 = caracteres.rollercoaster(personagem1)
	
	#vai para a fila
	fila.acquire()
	iii = p1.pega_posicao()
	fila.release()
		
	p1.vai_para_fila()
	
	if iii == -1:
		p1.remove()
		print(repr(num)+"=Fila cheia, vou embora")
		return

	
	print(repr(num)+"= já estou na fila")
	
	#Pega ticket // Ve se o trem chegou
	lugares.acquire()
	pessoas_fila+=1
	print(repr(num)+"= já peguei o ticket do trem")

	chegou_trem.acquire()
	while trem == 0:
		chegou_trem.wait(1)
	chegou_trem.release()
	
	# Vai se sentar
	fila2.acquire()
	p1.limpa_vaga()
	print(repr(num)+"= já estou sentado no trem")
	fila2.release()
	p1.vai_para_o_trem()
	
	#todos sentados
	parte_trem.acquire()
	pessoas_sentadas+=1
	if pessoas_sentadas == b:
		parte_trem.notify_all()
	parte_trem.release()
	
	#Trem partiu
	#Trem chegou
	chegou_trem.acquire()
	chegou_trem.wait()
	chegou_trem.release()
	p1.sai_do_trem()
	#vao embora
	fila3.acquire()
	p1.remove()
	fila3.release()
	lugares.release()
	
	
	print(repr(num)+"= já fui embora")
	
	
def trem(num):
	global pessoas_fila
	global pessoas_sentadas
	global grafico
	global a
	global b
	global c
	global trem
	chegou_trem.acquire()
	grafico.train_chega()
	trem = 1
	chegou_trem.notify_all()
	chegou_trem.release()
	
	while True:
		
		#aqui
		pessoas_fila=0
		print("Passageiros carregados")
		while pessoas_sentadas != b:
			parte_trem.acquire()
			parte_trem.wait(1)
			parte_trem.release()
		chegou_trem.acquire()
		grafico.train_parte()
		trem = 0
		time.sleep(c)
		grafico.train_chega()
		trem = 1
		chegou_trem.notify_all()
		chegou_trem.release()
		#sleep
		print("Passageiros descarregados")
		caracteres.rollercoaster.limpa_vagao()
		pessoas_sentadas = 0
	

def timer_grafico():

	while True:
		grafico.L1.acquire()
		grafico.imprime()
		time.sleep(0.01)
		grafico.L1.release()
		
		
		
timer = threading.Thread(target=timer_grafico)
timer.start()	
Trem = threading.Thread(target=trem,args=[999])
Trem.start()

i=0
while True:
	T = threading.Thread(target=pessoa,args=[i])
	T.start()
	i+=1
	time.sleep(d)
	

timer.join()
pygame.quit ()
