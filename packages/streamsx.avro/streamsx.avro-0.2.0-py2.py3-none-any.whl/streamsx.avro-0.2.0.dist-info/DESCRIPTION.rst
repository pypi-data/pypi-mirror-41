Overview
========

Provides functions for serialization and deserialization of messages in an Apache Avro format.
This package exposes the `com.ibm.streamsx.avro` toolkit as Python methods.

This package is compatible with Streaming Analytics service on IBM Cloud:

* `IBM Streaming Analytics <https://www.ibm.com/cloud/streaming-analytics>`_


Sample
======

A simple example of a Streams application that serializes and deserializes messages::

    from streamsx.topology.topology import *
    from streamsx.topology.schema import CommonSchema, StreamSchema
    from streamsx.topology.context import submit
    import streamsx.avro as avro

    topo = Topology()

    avro_schema = '{"type" : "record", "name" : "hw_schema", "fields" : [{"name" : "a", "type" : "string"}]}'
    s = topo.source([{'a': 'Hello'}, {'a': 'World'}, {'a': '!'}]).as_json()

    # convert json to avro blob
    o = avro.json_to_avro(s, avro_schema)
    # convert avro blob to json
    res = avro.avro_to_json(o, avro_schema)
    res.print()

    submit('STREAMING_ANALYTICS_SERVICE', topo)


Documentation
=============

* `streamsx.avro package documentation <http://streamsxavro.readthedocs.io/en/pypackage/>`_


