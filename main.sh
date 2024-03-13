#!/bin/bash

endereco_ip="192.0.2.100"
porta="53" 

echo "Endereco IP e porta do servico de nome: $endereco_ip:$porta"

timeout 1 tcpdump -i any -w captura_jose_dhonatas.pcap host "$endereco_ip and port $porta" -c 20
echo "Captura de trafego salva"

if ping -c 1 "$endereco_ip" &> /dev/null; then
    echo "O host do servico de nome esta online"
else
    echo "O host do servico de nome nao esta respondendo" 
fi


if timeout 1 telnet "$endereco_ip" "$porta" | grep -q "Connected"; then
    echo "O servico web esta respondendo corretamente"
else
    echo "O servico web nao esta respondendo corretamente"
fi

#Aluno: Jose Dhonatas Alves Sales
#Turma: 01

#chmod +x nome_do_script.sh, ./nome_do_script.sh