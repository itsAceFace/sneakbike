terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
    }
  }
}

provider "aws" {
  profile = "default"
  region  = "us-east-1"
}

resource "aws_key_pair" "sneakbike_key_pair" {
  key_name   = "sneakbike_key_pair"
  public_key = file("~/.ssh/terraform.pub")
}

resource "aws_security_group" "allow_rtmp" {
  name        = "allow_rtmp"
  description = "Allow RTMP inbound traffic"

  ingress {
    description = "RTMP"
    from_port   = 1935
    to_port     = 1935
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "SSH"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "allow_rtmp"
  }
}


resource "aws_instance" "sneakbike_instance" {
  key_name        = aws_key_pair.sneakbike_key_pair.key_name
  ami             = "ami-0bcc094591f354be2"
  instance_type   = "t3a.micro"
  security_groups = ["${aws_security_group.allow_rtmp.name}"]

  connection {
    type        = "ssh"
    user        = "ubuntu"
    private_key = file("~/.ssh/terraform")
    host        = self.public_ip
  }


  provisioner "remote-exec" {
    inline = [
      "sudo apt-get update",
      "sudo apt-get update",
      "sudo apt-get install -y wget unzip software-properties-common dpkg-dev git make gcc automake build-essential zlib1g-dev libpcre3 libpcre3-dev libssl-dev libxslt1-dev libxml2-dev libgd-dev libgeoip-dev libgoogle-perftools-dev libperl-dev pkg-config autotools-dev gpac ffmpeg mediainfo mencoder lame libvorbisenc2 libvorbisfile3 libx264-dev libvo-aacenc-dev libmp3lame-dev libopus-dev unzip",
      "sudo add-apt-repository -y ppa:nginx/stable && sudo apt-get update",
      "sudo apt-get install -y nginx",
      "sudo apt-get install -y libnginx-mod-rtmp",
      "sudo echo \"rtmp {\" | sudo tee -a /etc/nginx/nginx.conf",
      "sudo echo \"   server {\" | sudo tee -a /etc/nginx/nginx.conf",
      "sudo echo \"        listen 1935;\" | sudo tee -a /etc/nginx/nginx.conf",
      "sudo echo \"        chunk_size 4096;\" | sudo tee -a /etc/nginx/nginx.conf",
      "sudo echo \"        max_streams 512;\" | sudo tee -a /etc/nginx/nginx.conf",
      "sudo echo \"        application live {\" | sudo tee -a /etc/nginx/nginx.conf",
      "sudo echo \"                live on; \" | sudo tee -a /etc/nginx/nginx.conf",
      "sudo echo \"                record off;\" | sudo tee -a /etc/nginx/nginx.conf",
      "sudo echo \"        }\" | sudo tee -a /etc/nginx/nginx.conf",
      "sudo echo \"    }\" | sudo tee -a /etc/nginx/nginx.conf",
      "sudo echo \"}\" | sudo tee -a /etc/nginx/nginx.conf",
      "sudo systemctl restart nginx",
      "sudo systemctl restart nginx"
    ]

  }

  provisioner "local-exec" {
    command = "echo ${aws_instance.sneakbike_instance.public_ip}"
  }
  provisioner "local-exec" {
    command = "echo rtmp://${aws_instance.sneakbike_instance.public_ip}:1935/live"
  }
}

