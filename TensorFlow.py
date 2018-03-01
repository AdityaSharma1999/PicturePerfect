
(base) C:\Users\sharm>conda create -n tensorflow pip python=3.5
Solving environment: done

## Package Plan ##

  environment location: C:\Users\sharm\Anaconda3\envs\tensorflow

  added / updated specs:
    - pip
    - python=3.5


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    pip-9.0.1                  |   py35h691316f_4         2.6 MB
    python-3.5.4               |      h1357f44_23        18.6 MB
    setuptools-38.5.1          |           py35_0         548 KB
    wheel-0.30.0               |   py35h38a90bc_1          85 KB
    certifi-2018.1.18          |           py35_0         144 KB
    wincertstore-0.2           |   py35hfebbdb8_0          13 KB
    ------------------------------------------------------------
                                           Total:        22.0 MB

The following NEW packages will be INSTALLED:

    certifi:        2018.1.18-py35_0
    pip:            9.0.1-py35h691316f_4
    python:         3.5.4-h1357f44_23
    setuptools:     38.5.1-py35_0
    vc:             14-h0510ff6_3
    vs2015_runtime: 14.0.25123-3
    wheel:          0.30.0-py35h38a90bc_1
    wincertstore:   0.2-py35hfebbdb8_0

Proceed ([y]/n)? y


Downloading and Extracting Packages
pip 9.0.1: #################################################################################################### | 100%
python 3.5.4: ################################################################################################# | 100%
setuptools 38.5.1: ####################################################################################################################################################################################### | 100%
wheel 0.30.0: ############################################################################################################################################################################################ | 100%
certifi 2018.1.18: ####################################################################################################################################################################################### | 100%
wincertstore 0.2: ######################################################################################################################################################################################## | 100%
Preparing transaction: done
Verifying transaction: done
Executing transaction: done
#
# To activate this environment, use
#
#     $ conda activate tensorflow
#
# To deactivate an active environment, use
#
#     $ conda deactivate


(base) C:\Users\sharm>import tensorflow as tf
'import' is not recognized as an internal or external command,
operable program or batch file.

(base) C:\Users\sharm>print(sess.run(hello))
Unable to initialize device PRN

(base) C:\Users\sharm>pip install
You must give at least one requirement to install (see "pip help install")

(base) C:\Users\sharm>
(base) C:\Users\sharm>nnnnkk c^Zdertexit
'nnnnkk' is not recognized as an internal or external command,
operable program or batch file.

(base) C:\Users\sharm>activate tensorflow

(tensorflow) C:\Users\sharm>pip install --ignore-installed --upgrade tensorflow-gpu
Collecting tensorflow-gpu
  Downloading tensorflow_gpu-1.5.0-cp35-cp35m-win_amd64.whl (82.1MB)
    100% |################################| 82.1MB 54kB/s
Collecting numpy>=1.12.1 (from tensorflow-gpu)
  Downloading numpy-1.14.1-cp35-none-win_amd64.whl (13.4MB)
    100% |################################| 13.4MB 1.1MB/s
Collecting six>=1.10.0 (from tensorflow-gpu)
  Downloading six-1.11.0-py2.py3-none-any.whl
Collecting tensorflow-tensorboard<1.6.0,>=1.5.0 (from tensorflow-gpu)
  Downloading tensorflow_tensorboard-1.5.1-py3-none-any.whl (3.0MB)
    100% |################################| 3.0MB 1.4MB/s
Collecting absl-py>=0.1.6 (from tensorflow-gpu)
  Downloading absl-py-0.1.10.tar.gz (79kB)
    100% |################################| 81kB 1.2MB/s
Collecting protobuf>=3.4.0 (from tensorflow-gpu)
  Downloading protobuf-3.5.1-py2.py3-none-any.whl (388kB)
    100% |################################| 389kB 3.1MB/s
Collecting wheel>=0.26 (from tensorflow-gpu)
  Using cached wheel-0.30.0-py2.py3-none-any.whl
Collecting html5lib==0.9999999 (from tensorflow-tensorboard<1.6.0,>=1.5.0->tensorflow-gpu)
  Downloading html5lib-0.9999999.tar.gz (889kB)
    100% |################################| 890kB 1.5MB/s
Collecting werkzeug>=0.11.10 (from tensorflow-tensorboard<1.6.0,>=1.5.0->tensorflow-gpu)
  Downloading Werkzeug-0.14.1-py2.py3-none-any.whl (322kB)
    100% |################################| 327kB 1.6MB/s
Collecting markdown>=2.6.8 (from tensorflow-tensorboard<1.6.0,>=1.5.0->tensorflow-gpu)
  Downloading Markdown-2.6.11-py2.py3-none-any.whl (78kB)
    100% |################################| 81kB 365kB/s
Collecting bleach==1.5.0 (from tensorflow-tensorboard<1.6.0,>=1.5.0->tensorflow-gpu)
  Downloading bleach-1.5.0-py2.py3-none-any.whl
Collecting setuptools (from protobuf>=3.4.0->tensorflow-gpu)
  Using cached setuptools-38.5.1-py2.py3-none-any.whl
Building wheels for collected packages: absl-py, html5lib
  Running setup.py bdist_wheel for absl-py ... done
  Stored in directory: C:\Users\sharm\AppData\Local\pip\Cache\wheels\45\07\0e\6880381ca521796cf6cc18ba4ab502c2232e5777099b4df4ae
  Running setup.py bdist_wheel for html5lib ... done
  Stored in directory: C:\Users\sharm\AppData\Local\pip\Cache\wheels\6f\85\6c\56b8e1292c6214c4eb73b9dda50f53e8e977bf65989373c962
Successfully built absl-py html5lib
Installing collected packages: numpy, six, html5lib, werkzeug, markdown, setuptools, protobuf, wheel, bleach, tensorflow-tensorboard, absl-py, tensorflow-gpu
Successfully installed absl-py-0.1.10 bleach-1.5.0 html5lib-0.9999999 markdown-2.6.11 numpy-1.14.1 protobuf-3.5.1 setuptools-38.5.1 six-1.11.0 tensorflow-gpu-1.5.0 tensorflow-tensorboard-1.5.1 werkzeug-0.14.1 wheel-0.30.0

(tensorflow) C:\Users\sharm>python
Python 3.5.4 |Anaconda, Inc.| (default, Nov  8 2017, 14:34:30) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import tensorflow as tf
Traceback (most recent call last):
  File "C:\Users\sharm\Anaconda3\envs\tensorflow\lib\site-packages\tensorflow\python\platform\self_check.py", line 75, in preload_check
    ctypes.WinDLL(build_info.cudart_dll_name)
  File "C:\Users\sharm\Anaconda3\envs\tensorflow\lib\ctypes\__init__.py", line 351, in __init__
    self._handle = _dlopen(self._name, mode)
OSError: [WinError 126] The specified module could not be found

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Users\sharm\Anaconda3\envs\tensorflow\lib\site-packages\tensorflow\__init__.py", line 24, in <module>
    from tensorflow.python import *
  File "C:\Users\sharm\Anaconda3\envs\tensorflow\lib\site-packages\tensorflow\python\__init__.py", line 49, in <module>
    from tensorflow.python import pywrap_tensorflow
  File "C:\Users\sharm\Anaconda3\envs\tensorflow\lib\site-packages\tensorflow\python\pywrap_tensorflow.py", line 30, in <module>
    self_check.preload_check()
  File "C:\Users\sharm\Anaconda3\envs\tensorflow\lib\site-packages\tensorflow\python\platform\self_check.py", line 82, in preload_check
    % (build_info.cudart_dll_name, build_info.cuda_version_number))
ImportError: Could not find 'cudart64_90.dll'. TensorFlow requires that this DLL be installed in a directory that is named in your %PATH% environment variable. Download and install CUDA 9.0 from this URL: https://developer.nvidia.com/cuda-toolkit
>>> hello=tf.constant('Hello, TensorFlow!')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'tf' is not defined
>>> impor tensorflow as tf
  File "<stdin>", line 1
    impor tensorflow as tf
                   ^
SyntaxError: invalid syntax
>>> import tensorflow as tf
Traceback (most recent call last):
  File "C:\Users\sharm\Anaconda3\envs\tensorflow\lib\site-packages\tensorflow\python\platform\self_check.py", line 75, in preload_check
    ctypes.WinDLL(build_info.cudart_dll_name)
  File "C:\Users\sharm\Anaconda3\envs\tensorflow\lib\ctypes\__init__.py", line 351, in __init__
    self._handle = _dlopen(self._name, mode)
OSError: [WinError 126] The specified module could not be found

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Users\sharm\Anaconda3\envs\tensorflow\lib\site-packages\tensorflow\__init__.py", line 24, in <module>
    from tensorflow.python import *
  File "C:\Users\sharm\Anaconda3\envs\tensorflow\lib\site-packages\tensorflow\python\__init__.py", line 49, in <module>
    from tensorflow.python import pywrap_tensorflow
  File "C:\Users\sharm\Anaconda3\envs\tensorflow\lib\site-packages\tensorflow\python\pywrap_tensorflow.py", line 30, in <module>
    self_check.preload_check()
  File "C:\Users\sharm\Anaconda3\envs\tensorflow\lib\site-packages\tensorflow\python\platform\self_check.py", line 82, in preload_check
    % (build_info.cudart_dll_name, build_info.cuda_version_number))
ImportError: Could not find 'cudart64_90.dll'. TensorFlow requires that this DLL be installed in a directory that is named in your %PATH% environment variable. Download and install CUDA 9.0 from this URL: https://developer.nvidia.com/cuda-toolkit
>>>
