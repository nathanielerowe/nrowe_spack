Error: 

  >> 1498    CMake Error at /lus/grand/projects/neutrinoGPU/spack_builds/spack/opt/spack/linux-sles15-zen3/gcc-12.3.0/cetmodules-3.25.00-ublvkzinygsrjc6f7qcxwm4zbfnutphc/Modules/CetMakeLibrary.cmake:456 (target_l 
             ink_libraries):                                                                                                                                                                                         
     1499      Target "larrecodnn_ImagePatternAlgs_Tensorflow_PointIdAlg" links to:                                                                                                                                  
     1500                                                                                                                                                                                                            
     1501        TensorFlow::framework                                                                                                                                                                               
     1502                                                                                                                                                                                                            
     1503      but the target was not found.  Possible reasons include:                                                                                                                                              
     1504                                                                                                                                                                                                                                                                                                                                                                                                                     

Solution:
Locate the py-tensorflow installation being used under spack/opt/spack and go to cp lib/python3.9/site-packages/tensorflow/libtensorflow_framework.so.2 lib/python3.9/site-packages/tensorflow/libtensorflow_framework.so. Similar procedure with libtensorflow_cc.so.2
