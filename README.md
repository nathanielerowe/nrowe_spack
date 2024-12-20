Error: 

 >> 1483    CMake Error at /lus/grand/projects/neutrinoGPU/spack_builds/spack/opt/spack/linux-sles15-zen3/gcc-12.3.0/cetmodules-3.25.00-ublvkzinygsrjc6f7qcxwm4zbfnutphc/Modules/CetMakeLibrary.cmake:456 (target_l 
             ink_libraries):                                                                                                                                                                                         
     1484      Target "larrecodnn_ImagePatternAlgs_Tensorflow_TF" links to:                                                                                                                                          
     1485                                                                                                                                                                                                            
     1486        TensorFlow::cc                                                                                                                                                                                      
     1487                                                                                                                                                                                                            
     1488      but the target was not found.  Possible reasons include:                                                                                                                                              
     1489                                                                                                                                                                                                            
                                                                                                                                                                                                                     
     ...                                                                                                                                                                                                             
                                                                                                                                                                                                                     
     1492        * An ALIAS target is missing.                                                                                                                                                                       
     1493                                                                                                                                                                                                            
     1494    Call Stack (most recent call first):                                                                                                                                                                    
     1495      larrecodnn/ImagePatternAlgs/Tensorflow/TF/CMakeLists.txt:1 (cet_make_library)                                                                                                                         
     1496                                                                                                                                                                                                            
     1497                                                                                                                                                                                                            
  >> 1498    CMake Error at /lus/grand/projects/neutrinoGPU/spack_builds/spack/opt/spack/linux-sles15-zen3/gcc-12.3.0/cetmodules-3.25.00-ublvkzinygsrjc6f7qcxwm4zbfnutphc/Modules/CetMakeLibrary.cmake:456 (target_l 
             ink_libraries):                                                                                                                                                                                         
     1499      Target "larrecodnn_ImagePatternAlgs_Tensorflow_PointIdAlg" links to:                                                                                                                                  
     1500                                                                                                                                                                                                            
     1501        TensorFlow::framework                                                                                                                                                                               
     1502                                                                                                                                                                                                            
     1503      but the target was not found.  Possible reasons include:                                                                                                                                              
     1504                                                                                                                                                                                                            
                                                                                                                                                                                                                     
     ...                                                                                                                                                                                                             

Solution:
Locate the py-tensorflow installation being used under spack/opt/spack and go to cp lib/python3.9/site-packages/tensorflow/libtensorflow_framework.so.2 lib/python3.9/site-packages/tensorflow/libtensorflow_framework.so

