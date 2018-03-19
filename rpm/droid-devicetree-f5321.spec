# General details
%define device f5321

# Device Tree Source to pre-process and compile
%define master_dts "dts/msm8956-v1.1-loire-kugo_generic.dts"

# Final file
%define final_dtb "msm8956-loire-kugo_generic.dtb"

# Includes directory
%define includes_directory "include"

%include droid-devicetree-device/droid-devicetree-device.inc
