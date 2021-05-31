# SendAnyFile
These two files are used to transmit data (text file, audio file, video file) of any extension from a machine A to a machine B located on the same network. The code of the sending machine is sender.py and the receiving one is receiver.py. You must first run the receiver then the sender and inform the latter of the receiver's IP address. These two scripts must respectively be executed in the folders where the file to send is located and the folder where you want to receive it. If you are locally, specify localhost or 127.0.0.1 for the receiver address. Care should be taken when sending audio and video files. Make sure that they are not too heavy (maximum 10min) if your PC is not very powerful in capacity