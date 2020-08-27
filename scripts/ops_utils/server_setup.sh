#!/bin/bash
sudo apt-get update
sudo apt-get install -y wget unzip software-properties-common dpkg-dev git make gcc automake build-essential zlib1g-dev libpcre3 libpcre3-dev libssl-dev libxslt1-dev libxml2-dev libgd-dev libgeoip-dev libgoogle-perftools-dev libperl-dev pkg-config autotools-dev gpac ffmpeg mediainfo mencoder lame libvorbisenc2 libvorbisfile3 libx264-dev libvo-aacenc-dev libmp3lame-dev libopus-dev unzip
sudo add-apt-repository -y ppa:nginx/stable && sudo apt-get update
sudo apt-get install -y nginx
sudo apt-get install -y libnginx-mod-rtmp

sudo echo "
rtmp {
        server {
                listen 1935;
                chunk_size 4096;
                max_streams 512;

                application live {
                        live on;
                        record off;
                }
        }
}
" | sudo tee -a /etc/nginx/nginx.conf

sudo systemctl restart nginx