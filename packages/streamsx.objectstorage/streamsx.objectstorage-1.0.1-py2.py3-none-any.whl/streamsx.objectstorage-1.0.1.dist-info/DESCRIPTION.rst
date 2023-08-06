Overview
========

Provides functions to read objects from Cloud Object Storage as a stream
and submit tuples to create objects in Cloud Object Storage (COS).

`IBM Cloud Object Storage <https://www.ibm.com/cloud/object-storage>`_ makes it possible to store practically limitless amounts of data, simply and cost effectively. It is commonly used for data archiving and backup, web and mobile applications, and as scalable, persistent storage for analytics.

Sample
======

A simple hello world example of a Streams application writing string messages to
an object. Scan for created object on COS and read the content::

    from streamsx.topology.topology import *
    from streamsx.topology.schema import CommonSchema
    from streamsx.topology.context import submit
    import streamsx.objectstorage as cos

    topo = Topology('ObjectStorageHelloWorld')

    to_cos = topo.source(['Hello', 'World!'])
    to_cos = to_cos.as_string()

    # sample bucket with resiliency "regional" and location "us-south"
    bucket = 'streamsx-py-sample'
    # US-South region private endpoint
    endpoint='s3.private.us-south.cloud-object-storage.appdomain.cloud'

    # Write a stream to COS
    cos.write(to_cos, bucket, endpoint, '/sample/hw%OBJECTNUM.txt')

    scanned = cos.scan(topo, bucket=bucket, endpoint=endpoint, directory='/sample')

    # read text file line by line
    r = cos.read(scanned, bucket=bucket, endpoint=endpoint)

    # print each line (tuple)
    r.print()

    submit('STREAMING_ANALYTICS_SERVICE', topo)

Documentation
=============

* `streamsx.objectstorage package documentation <http://streamsxobjectstorage.readthedocs.io/en/pypackage/>`_


