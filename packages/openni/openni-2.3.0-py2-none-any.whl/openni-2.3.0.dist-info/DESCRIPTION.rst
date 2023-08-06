Python-bindings for `OpenNI2 <https://github.com/OpenNI/OpenNI2>`_
and `NiTE2 <http://openni.ru/files/nite/>`_.

This package provides only the Python bindings; be sure to install OpenNI2 (and optionally NiTE2) first.

Example::

    from openni import openni2

    openni2.initialize()     # can also accept the path of the OpenNI redistribution

    dev = openni2.Device.open_any()
    print dev.get_device_info()

    depth_stream = dev.create_depth_stream()
    depth_stream.start()
    frame = depth_stream.read_frame()
    frame_data = frame.get_buffer_as_uint16()
    depth_stream.stop()

    openni2.unload()


.. note:: Refer to the OpenNI2/NiTE2 C API for complete documentation



