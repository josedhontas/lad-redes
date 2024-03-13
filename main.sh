#!/bin/bash

endereco_ip="192.0.2.100"
porta="53" 

echo "Endereco IP e porta do servico de nome: $endereco_ip:$porta"

if ping -c 1 "$endereco_ip" &> /dev/null; then
    echo "O host do servico de nome está online"
else
    echo "O host do servico de nome nao esta respondendo" 
fi



if telnet "$endereco_ip" "$porta" &> /dev/null; then
    echo "O serviço web esta respondendo corretamente"
else
    echo "O serviço web nao esta respondendo corretamente"
fi

#chmod +x nome_do_script.sh, ./nome_do_script.sh