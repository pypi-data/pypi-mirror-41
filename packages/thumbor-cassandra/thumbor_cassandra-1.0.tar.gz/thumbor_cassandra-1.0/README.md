Apache Cassandra Module for Thumbor
===================================

[![Build Status](https://travis-ci.org/glborges/thumbor-cassandra.svg?branch=master)](https://travis-ci.org/glborges/thumbor-cassandra)

Introduction
------------

[Thumbor](https://github.com/globocom/thumbor/wiki) is a smart imaging service. It enables on-demand crop, resizing and flipping of images.

  
[Apache Cassandra](https://cassandra.apache.org/) is a free and open-source, distributed, wide column store, NoSQL database management system designed to handle large amounts of data across many commodity servers, providing high availability with no single point of failure. Cassandra offers robust support for clusters spanning multiple datacenters,[1] with asynchronous masterless replication allowing low latency operations for all clients.

Installation
------------

In order to install the Apache Cassandra Module for Thumbor, you have to install Apache Cassandra ecosystem first. 

## Apache Cassandra installation

The Apache Cassandra Module for Thumbor was originally developed and tested using the Cassandra docker image [Cassandra Official Docker Image](https://hub.docker.com/_/cassandra).

## Thumbor installation

You have to install [Thumbor](https://github.com/globocom/thumbor) following the [Thumbor Installation Guide](https://github.com/globocom/thumbor/wiki/Installing)...


## Apache Cassandra Module installation

... and finally the Apache Cassandra Module :

  pip install thumbor_cassandra
  
  
Usage
-----

Using it is simple, just change your configuration in thumbor.conf:
    
     CASSANDRA_LOADER_SERVER_HOST = 'localhost'
     CASSANDRA_LOADER_SERVER_PORT = 9042
     CASSANDRA_LOADER_KEYSPACE = 'general'
     CASSANDRA_LOADER_TABLE_NAME = 'images'
     CASSANDRA_LOADER_TABLE_ID_COLUMN = 'image_id'
     CASSANDRA_LOADER_TABLE_BLOB_COLUMN = 'image_data'
     CASSANDRA_LOADER_QUERY' = 'SELECT * FROM {0} WHERE {1}=%s'

To use thumbor_cassandra for loading original images, change your thumbor.conf to read:

    LOADER = 'thumbor_cassandra.loader'

Testing
-------

In order to execute [pyvows](http://heynemann.github.com/pyvows/) tests, you have to install pyvows :

       pip install pyvows 

and run tests with :

       pyvows vows
  

License
-------

        Licensed under the MIT license:
        http://www.opensource.org/licenses/mit-license
        Copyright (c) 2019 TMG Digital - Speurders.nl
