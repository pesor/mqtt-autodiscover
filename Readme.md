# MQTT Autodiscover made easy

## MQTT autodiscover Homeassistant made easy



### Getting started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

1. Home Assistant (ver. 0.115.x )

2. A Python EDI editor for Windows 10, I use Eric-6 EDI, https://eric-ide.python-projects.org/, which is very easy to install and use.

3. MQTT server (I am running on a Synology NAS in docker)
   If you have a Synology NAS, I can recommend to follow [BeardedTinker](https://www.youtube.com/channel/UCuqokNoK8ZFNQdXxvlE129g) on YouTube, he makes a very intuitive explanation how to setup the whole Home Assistant environment on Synology.   

4. You will need the following in your configuration.yaml file: 

   **python_script:**

   **mqtt:**
     **broker: 192.168.1.64**
     **discovery: true**
     **discovery_prefix: homeassistant** (Default, it is the folder where you have your configuration.yaml file)

5. [](https://https://www.youtube.com/channel/UCuqokNoK8ZFNQdXxvlE129g)

   

### Installing

Below a step by step that tell you how to get a development/production environment up and running, and to make things even more easy,

IF BEARDEDTINKER makes a video, it will be referred to here: 

![BeardedTinker](https://www.youtube.com/channel/UCuqokNoK8ZFNQdXxvlE129g)  have created the tutorial on YouTube, which gives a detailed instruction how to get it all to work.

He has performed a tremendous task in doing this.

I highly recommend that your see and follow this video, as you then will have success in setting the up the Autodiscover on Home Assistant.

After seeing the videos, remember to give a "Thumbs Up" to support BeardedThinker in his work.

## Mapping the mqtt json message to the Python script:

Mapping of the JSON message, is actually very simple, just a lot of writing.

I have used an example from my Fronius Inverter, but no matter what sensor you want to map, procedure are the same.

![](https://github.com/pesor/mqtt-autodiscover/blob/main/images/Mapping-1.JPG)

This is the end of the mapping

![](https://github.com/pesor/mqtt-autodiscover/blob/main/images/Mapping-2.JPG)

Be careful when writing in the Python program, use preferably a Python EDI, as Python is build with syntaxes around "whitespaces", which is very difficult to control in a simple text editor.



## The Python Part - The Autodiscover - MAGIC

The Python script named: 

### 																																		mqtt-aut.py**

you install in the folder python_scripts in your Home Assistant config folder, If you do not have that folder already, you need to create it. 

The Home Assistant config folder, is where you also have your configuration.yaml file.

You find and execute the Python script, in the menu "Developer Tools"/"SERVICES", where you will find it named:

### 																							python_script.mqtt-aut



### **Running the Python_sscript.mqtt-aut**

You just press the "CALL SERVICE" button, and all the sensors from mqtt will be autodiscovered and added to your menu "Configuration"/"integrations", where you will find the MQTT integration, and here you can select the devices, and then select Solar_Power, and all sensors will be shown. You can use the "ADD TO LOVELACE" function, or you can add them manually to any LOVELACE card you want.

### Deployment

See instructions under **Prerequisites**

### Versioning

1.0.0 First official release

### Authors

* **Per Rose** 
* BeardedTinker (contributer)

### License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details



**If you like and use my program, then** 

​       [![BMC](https://www.buymeacoffee.com/assets/img/custom_images/white_img.png)](https://www.buymeacoffee.com/pesor)

**it will be appreciated.**



