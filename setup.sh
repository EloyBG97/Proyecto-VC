#!/bin/sh

path_img_jpg="oxbuild_images"
path_img_ppm="imagenes_ppm"
path_word="word_oxc1_hesaff_sift_16M_1M"

mkdir $path_img_jpg
#mkdir $path_img_ppm 

tar -zxvf oxbuild_images.tgz -C $path_img_jpg
tar -zxvf word_oxc1_hesaff_sift_16M_1M.tgz

rm -rf $path_img_jpg/ashmolean_000214.jpg

#python convert_jpg2ppm.py $path_img_jpg $path_img_ppm
python wordBag.py $path_img_jpg $path_word/

echo "Instalación completada!!"
