
# Desafio de Provisionamento do Apache Airflow com Terraform e Ansible

## Objetivo
Provisionar um ambiente na AWS com:
- Infraestrutura via Terraform usando EKS.
- Instalação do Airflow via Ansible em uma EC2.

## Estrutura

### Terraform
- `vpc.tf`: Criação da VPC e subnets públicas.
- `eks.tf`: Criação do cluster EKS com auto scaling nodes.
- `providers.tf`: Providers AWS e Kubernetes.
- `outputs.tf`: Saídas úteis (nome do cluster, kubeconfig).

### Ansible
- `hosts.yml`: Inventário com o IP da EC2.
- `playbook.yml`: Playbook principal chamando o role `airflow`.
- `roles/airflow/tasks/main.yml`: Instala Docker e inicia o Airflow via Docker Compose.
- `roles/airflow/templates/docker-compose.yml.j2`: Template do serviço Airflow com webserver exposto.

### Considerações
- A imagem do Docker Hub usada é: apache/airflow:2.10.5-python3.9
- O Load Balancer é criado automaticamente pelo docker-compose ao mapear a porta 8080.
- A instalação é leve, usa sqlite e SequentialExecutor para simplificar o ambiente.

## Como executar

1. **Terraform**
```bash
cd terraform
terraform init
terraform plan
terraform apply
```

2. **Ansible**
```bash
ansible-playbook ansible/playbook.yml -u ec2-user --private-key airflow-iac2.pem -i ansible/hosts.yml
```

> Substitua `<public_ip_da_EC2>` e `airflow-iac2.pem` com os valores corretos do seu ambiente.
