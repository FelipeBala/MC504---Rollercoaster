import pygame
import spritesheet_functions
import time
import threading

class grafica():

	lock = threading.Lock()
	
	def __init__(self,screen2,L,background_image2,imagem_trem2):
		self.screen4 = screen2
		self.imagem2 = []
		self.pos = []
		self.u = []
		self.L1 = L
		self.background_image = background_image2
		self.imagem_trem = imagem_trem2
		self.pos_trem = [-900,410]
		
	def imagem(self,ima,pos2,x):
		grafica.lock.acquire()
		flag = -1
		for i in range(len(self.u)):
			if self.u[i] == x :
				flag = 2
				self.imagem2[i] = ima
				self.pos[i] = pos2
				break
		if flag == -1:
			self.imagem2.append(ima)
			self.pos.append(pos2)
			self.u.append(x)
		grafica.lock.release()
			
	def deleta(self,x):
		grafica.lock.acquire()
		for i in range(len(self.u)):
			if self.u[i] == x :
				del self.imagem2[i]
				del self.pos[i]
				del self.u[i]
				break
		grafica.lock.release()

				
	def train_chega(self):
		if self.pos_trem[0] != -900:
			self.pos_trem[0] -= 2000
		for j in range(len(self.u)):
			if self.pos[j][1] > 400 and self.pos[j][1] < 570:
				self.pos[j][0] -= 2000
			
		for i in range(self.pos_trem[0],0,2):
			for j in range(len(self.u)):
				if self.pos[j][1] > 400 and self.pos[j][1] < 570:
					self.pos[j][0] += 2
			self.pos_trem[0] = i
			time.sleep(0.01)
	
	def train_parte(self):
		for i in range(self.pos_trem[0],1100,2):
			for j in range(len(self.u)):
				if self.pos[j][1] > 400 and self.pos[j][1] < 570:
					self.pos[j][0] += 2
			self.pos_trem[0] = i
			time.sleep(0.01)

	def imprime(self):
		grafica.lock.acquire()
		#self.screen4.fill([ 0, 0, 0])
		self.screen4.blit(self.background_image, [0, 0])
		self.screen4.blit(self.imagem_trem, self.pos_trem)
		for t in range(len(self.u)):
			#print("quero saber= "+repr(self.u[t]))
			#print("quero pos_0= "+repr(self.pos[t][0]))
			#print("quero pos_1= "+repr(self.pos[t][1]))
			self.screen4.blit( self.imagem2[t], self.pos[t])
			pygame.event.get()
		pygame.event.get()
		pygame.display.flip()
		grafica.lock.release()
		

class inicia_personagens():
    imagem = {}
    num_personagens = 3
    def __init__(self):
        k=0
        teste = spritesheet_functions.SpriteSheet("sheet.png")
        for i in range(0,8,1):
            for j in range(0,12,1):
                self.imagem[k] = teste.get_image(j*32,i*32,32,32)
                k+= 1
                
                
class personagem():
    x = 0
    y = 0
    estado = 0
    screen = None
    id = 0
    velocidade = 0.001
    
    def __init__(self,imagem,num,screen20,grafico2,num2):
		
        self.screen = screen20
        self.grafico = grafico2
        self.id = num2
        self.personagem = {}
		
        if num == 1 :
            self.personagem[0] = imagem[0]
            self.personagem[1] = imagem[1]
            self.personagem[2] = imagem[2]
            
            self.personagem[3] = imagem[12]
            self.personagem[4] = imagem[13]
            self.personagem[5] = imagem[14]
            
            self.personagem[6] = imagem[24]
            self.personagem[7] = imagem[25]
            self.personagem[8] = imagem[26]
		
        if num == 2 :
            self.personagem[0] = imagem[3]
            self.personagem[1] = imagem[4]
            self.personagem[2] = imagem[5]
            
            self.personagem[3] = imagem[15]
            self.personagem[4] = imagem[16]
            self.personagem[5] = imagem[17]
            
            self.personagem[6] = imagem[27]
            self.personagem[7] = imagem[28]
            self.personagem[8] = imagem[29]

        if num == 3 :
            self.personagem[0] = imagem[6]
            self.personagem[1] = imagem[7]
            self.personagem[2] = imagem[8]
            
            self.personagem[3] = imagem[18]
            self.personagem[4] = imagem[19]
            self.personagem[5] = imagem[20]
            
            self.personagem[6] = imagem[30]
            self.personagem[7] = imagem[31]
            self.personagem[8] = imagem[32]

        if num == 4 :
            self.personagem[0] = imagem[9]
            self.personagem[1] = imagem[10]
            self.personagem[2] = imagem[11]
            
            self.personagem[3] = imagem[21]
            self.personagem[4] = imagem[22]
            self.personagem[5] = imagem[23]
            
            self.personagem[6] = imagem[33]
            self.personagem[7] = imagem[34]
            self.personagem[8] = imagem[35]
		
        if num == 5 :
            self.personagem[0] = imagem[48]
            self.personagem[1] = imagem[49]
            self.personagem[2] = imagem[50]
            
            self.personagem[3] = imagem[60]
            self.personagem[4] = imagem[61]
            self.personagem[5] = imagem[62]
            
            self.personagem[6] = imagem[72]
            self.personagem[7] = imagem[73]
            self.personagem[8] = imagem[74]

        if num == 6 :
            self.personagem[0] = imagem[51]
            self.personagem[1] = imagem[52]
            self.personagem[2] = imagem[53]
            
            self.personagem[3] = imagem[63]
            self.personagem[4] = imagem[64]
            self.personagem[5] = imagem[65]
            
            self.personagem[6] = imagem[75]
            self.personagem[7] = imagem[76]
            self.personagem[8] = imagem[77]

        if num == 7 :
            self.personagem[0] = imagem[54]
            self.personagem[1] = imagem[55]
            self.personagem[2] = imagem[56]
            
            self.personagem[3] = imagem[66]
            self.personagem[4] = imagem[67]
            self.personagem[5] = imagem[68]
            
            self.personagem[6] = imagem[78]
            self.personagem[7] = imagem[79]
            self.personagem[8] = imagem[80]

        if num == 8 :
            self.personagem[0] = imagem[57]
            self.personagem[1] = imagem[58]
            self.personagem[2] = imagem[59]
            
            self.personagem[3] = imagem[69]
            self.personagem[4] = imagem[70]
            self.personagem[5] = imagem[71]
            
            self.personagem[6] = imagem[81]
            self.personagem[7] = imagem[82]
            self.personagem[8] = imagem[83]			
		
    @staticmethod
    def inicia_parametros(v):
        personagem.velocidade = v
        
    
    def desenha(self):
        self.grafico.imagem(self.personagem[self.estado],[self.x,self.y],self.id)

    
    def pos_init(self,x1,y1):
        self.x = x1
        self.y = y1
    
    def move_R(self):
        self.x += 2
        if self.estado == 6:
            self.estado = 7
        elif self.estado == 7:
            self.estado = 8 
        elif self.estado == 8:
            self.estado = 6
        else:
            self.estado = 7
        self.desenha()

    def move_L(self):
        self.x -= 2
        if self.estado == 5:
            self.estado = 4
        elif self.estado == 4:
            self.estado = 3 
        elif self.estado == 3:
            self.estado = 5
        else:
            self.estado = 4
        self.desenha()        
        
    def move_D(self):
        self.y += 2
        if self.estado == 0:
            self.estado = 1
        elif self.estado == 1:
            self.estado = 2 
        elif self.estado == 2:
            self.estado = 0
        else:
            self.estado = 1
        self.desenha()        
    
    def chegue_em(self,targ_x,targ_y):
        
        for i in range(self.y,targ_y,2):
            self.move_D()
            time.sleep(personagem.velocidade)			
            
        if (targ_x-self.x)>0:
            for i in range(self.x,targ_x,2):
                self.move_R()
                pygame.event.get()
                time.sleep(personagem.velocidade)

        else:
            for i in range(self.x,targ_x,-2):
                self.move_L()
                pygame.event.get()
                time.sleep(personagem.velocidade)
            

class rollercoaster():
	max_pessoas_fila = 6
	max_pessoas_trem = 4
	fila_pos = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	fila_pos_u = [[750,330],[710,330],[670,330],[630,330],[550,330],[510,330],[470,330],[430,330],[350,330],[310,330],[270,330],[240,330],[750,290],[710,290],[670,290],[630,290],[550,290],[510,290],[470,290],[430,290],[350,290],[310,290],[270,290],[240,290],[750,250],[710,250],[670,250],[630,250],[550,250],[510,250],[470,250],[430,250],[350,250],[310,250],[270,250],[240,250]]
	fila_trem = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	fila_trem_u = [[750,430],[710,430],[670,430],[630,430],[550,430],[510,430],[470,430],[430,430],[350,430],[310,430],[270,430],[240,430],[210,430],[170,430],[130,430],[90,430],[50,430],[10,430],[750,480],[710,480],[670,480],[630,480],[550,480],[510,480],[470,480],[430,480],[350,480],[310,480],[270,480],[240,480],[210,480],[170,480],[130,480],[90,480],[50,480],[10,480]]
	def __init__(self,personagem2):
		self.personagem = personagem2
	
	@staticmethod
	def inicia_parametros(max_fila,max_trem):
		if max_fila > 30:
			print("O numero maximo de pessoas na fila precisa ser menor que 30")
		else:
			rollercoaster.max_pessoas_fila = max_fila 
		if max_trem > 30:
			print("O numero maximo de pessoas no trem precisa ser menor que 30")
		else:
			rollercoaster.max_pessoas_trem = max_trem  

	def vai_para_fila(self):
		if self.flag1 == -1:
			self.personagem.chegue_em(110,170)
			self.personagem.chegue_em(-40,170)
			return
		self.personagem.chegue_em(rollercoaster.fila_pos_u[self.flag1][0],rollercoaster.fila_pos_u[self.flag1][1])
		return

	def pega_posicao(self):
		self.flag1=-1
		for i in range(0,rollercoaster.max_pessoas_fila,1):
			if rollercoaster.fila_pos[i] == 0:
				self.flag1 = i
				rollercoaster.fila_pos[i] = 1
				break
		if self.flag1 == -1:
			return(-1)
		return(2)

	
	def vai_para_o_trem(self):
		for i in range(0,rollercoaster.max_pessoas_trem,1):
			if rollercoaster.fila_trem[i] == 0:
				flag2 = i
				rollercoaster.fila_trem[i] = 1
				break
		self.personagem.chegue_em(rollercoaster.fila_trem_u[flag2][0],rollercoaster.fila_trem_u[flag2][1])
	
	@staticmethod
	def limpa_vagao():
		for i in range(0,30,1):
			rollercoaster.fila_trem[i] = 0
	
	
	def sai_do_trem(self):
		self.personagem.chegue_em(420,650)
		self.personagem.chegue_em(420,800)

	def remove(self):
		self.personagem.grafico.deleta(self.personagem.id)
	
	def limpa_vaga(self):
		rollercoaster.fila_pos[self.flag1] = 0
