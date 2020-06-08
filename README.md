# Bot Para curtidas no Instagram
Este bot foi criado para realizar curtidas automaticas no Instagram atraves de uma TAG especifica.


OBS: 
  * _Bot feito para o sistema Operacional Windows._
  * _Não funciona se sua conta tiver autenticação de dois fatores_

# Pre Requisitos
  * Python: Instalar o Python atraves do Link https://www.python.org/downloads/
  * ChromeDriver: Instalar atraves do link https://chromedriver.chromium.org/downloads | Este arquivo deve ficar na mesma pasta do arquivo .py e ser compativel com a versão do google Chrome da sua maquina;
  
  
# Configuração
Para utilizar o Bot você deve realizar a troca das informações nesta linha com as suas credenciais e a Sua Tag
Instagram("SeuUsuario","SuaSenha","TAGaSerCurtida")

# Funcionamento
O Bot irá logar em sua conta e navegar até a pagina da TAG informada. Irá abrir a primeira foto, curtir, aguardar 10 Segundos, passar para a proxima foto e reiniciar o ciclo até que sejam curtidas 100 fotos.
O intervalo de 10 segundos é primordial pois caso contrario sua conta será bloqueada, já que o Instagram monitora as atividades suspeitas das contas.
Importante ressaltar que aguarde o intervalo de pelo menos 30 minutos entre as execuções do programa pois sua conta também pode ser considerada fraudulenta se forçar a execução por muitas vezes seguidas.
