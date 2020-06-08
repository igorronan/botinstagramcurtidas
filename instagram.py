from selenium import webdriver
import time


class Instagram:
    def __init__(self, usuario , senha, tag ):
        self.usuario = usuario
        self.senha = senha
        self.tag = tag

        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(
            executable_path=r'./chromedriver.exe', chrome_options=options)

    def Clicar(self, tipo, nome, valor):
        driver = self.driver
        botao_enviar = driver.find_element_by_xpath(
               "//" + tipo + "[@" + nome + "='" + valor + "']")
        botao_enviar.click()

    def Preencher(self, tipo, nome, valor, dado):
        driver = self.driver
        preenche =  driver.find_element_by_xpath(
                "//" + tipo + "[@" + nome + "='" + valor + "']")
        preenche.clear()
        preenche.send_keys(dado)


    def Logar(self):
        print("Logando no Sistema " )
        self.Preencher("input", "name", "username",self.usuario)
        self.Preencher("input", "name", "password",self.senha)
        time.sleep(1)
        self.Clicar("button","class","sqdOP  L3NKy   y3zKF     ")
    
    def Iniciar(self):
        #Abrir O instagram
        self.driver.get('https://www.instagram.com/?hl=pt-br')
        time.sleep(2)
        
        self.Logar()
        
        time.sleep(4)
        self.Clicar("button","class","sqdOP yWX7d    y3zKF     ")
        time.sleep(4)
        self.Clicar("button","class","aOOlW   HoLwm ")
        self.driver.get('https://www.instagram.com/explore/tags/'+ self.tag+'/')
        self.Clicar("div","class","v1Nh3 kIKUG  _bz0w")
        time.sleep(2)

    def CurtirFoto(self):
        time.sleep(2)
        self.Clicar("span","class","fr66n")
        time.sleep(2)
        self.Clicar("a","class"," _65Bje  coreSpriteRightPaginationArrow")
        time.sleep(10)



bot = Instagram("SeuUsuario","SuaSenha","TAGaSerCurtida")
bot.Iniciar()
for i in range(1,101):
    bot.CurtirFoto()
    print(f" {i} Foto(s) curtidas")

print("Loop terminado")
