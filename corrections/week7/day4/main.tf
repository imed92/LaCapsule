provider "aws" {
    # La région
    region = "eu-west-3"
    # Au cas ou je ne suis pas authentifié en tant qu'utilisateur IAM via mon aws CLI, je dois renseigner les clé suivantes
    # access_key = "valeur de la clé d'acces"
    # secret_key = "valeur de la clé secrete"
}

# Référence du groupe de sécurité existant
data "aws_security_group" "existing_sg" {
    # Ici l'id du groupe de sécurité
    # Pour autoriser le trafic HTTP et HTTPS sur l'instance
  id = "sg-0e245c96b767d0a09"
}

# Création d'une instance EC2
resource "aws_instance" "web_server" {
  # AMI de ubuntu server version 24 
  ami           = "ami-09d83d8d719da9808"
#   Le type d'instance
  instance_type = "t2.micro"

  # Utilisation du groupe de sécurité existant
  vpc_security_group_ids = [data.aws_security_group.existing_sg.id]

# Ca me permet d'executer ce script bash au démarrage de l'instance
  user_data = <<-EOF
              #!/bin/bash
              apt-get update -y
              apt-get install -y apache2 awscli
              systemctl start apache2
              systemctl enable apache2
              aws s3 cp s3://${aws_s3_bucket.my_bucket.bucket}/toto.html /var/www/html/toto.html
              chmod 644 /var/www/html/toto.html
              EOF

  tags = {
    Name = "WebServerInstance"
  }
}

# Création d'un bucket S3
resource "aws_s3_bucket" "my_bucket" {
  bucket = "tazmanie-lacapsule-12345" # Le nom du bucket doit être unique sur tout AWS

  tags = {
    Name = "MyBucket"
  }
}

# Téléchargement du fichier toto.html vers le bucket S3
resource "aws_s3_object" "toto_html" {
  bucket = aws_s3_bucket.my_bucket.bucket
  key    = "toto.html"
  source = "./toto.html" # Chemin local vers le fichier toto.html
#   acl    = "public-read"
}