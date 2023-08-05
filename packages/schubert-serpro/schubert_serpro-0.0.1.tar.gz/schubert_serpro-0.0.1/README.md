# SERPRO

Integração para consultas no servidor da `SERPRO` Brasil

Link para documentação https://schubert.gitbook.io/serpro/

### Como instalar
Em breve você poderá baixar via pip
```shell
pip install schubert_serpro
```

### Compatibilidade
Python3

### Dependências

Este pacote usa um validador de `CPF` e `CNPJ` a fim de evitar mandar para consulta na `SERPRO` qualquer dado inválido, evitando pagamento de valores desnecessários.

```txt
requests==2.19.1
pycpfcnpj==1.5
```