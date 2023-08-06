.. _installation:

Installation
============

The fastest way to try Pydoop is via the `Docker <https://www.docker.com/>`_
image::

  docker pull crs4/pydoop
  export PORT_FW="-p 8020:8020 -p 8042:8042 -p 8088:8088 -p 9000:9000 -p 10020:10020 -p 19888:19888 -p 9866:9866 -p 9867:9867 -p 9870:9870 -p 9864:9864 -p 9868:9868"
  docker run ${PORT_FW} --name pydoop -d crs4/pydoop

This spins up a single-node, `pseudo-distributed
<https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/SingleCluster.html#Pseudo-Distributed_Operation>`_
Hadoop cluster with `HDFS
<https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-hdfs/HdfsDesign.html#Introduction>`_,
`YARN
<https://hadoop.apache.org/docs/stable/hadoop-yarn/hadoop-yarn-site/YARN.html>`_
and a Job History server. To check that all daemons are up and running, you
can run ``jps`` on the container. If everything is OK, you should get something
like this::

  $ docker exec -it pydoop bash -c 'jps | grep -v Jps'
  161 DataNode
  356 NodeManager
  523 JobHistoryServer
  75 NameNode
  301 ResourceManager

Read on for detailed installation instructions.


Supported Platforms
-------------------

At the moment, Pydoop is being tested on `CentOS <http://www.centos.org>`_ 7
only, although it should also work on other Linux distros and (possibly with
some tweaking) on macOS. Windows is **not** supported.


Prerequisites
-------------

* `Python <http://www.python.org>`_ 2 or 3 (tested with 2.7 and 3.6),
  including header files (e.g., ``python-devel`` on CentOS, ``python-dev`` on
  Debian);

* `setuptools <https://pypi.python.org/pypi/setuptools>`_ >= 3.3;

* Hadoop >=2. We currently run regular CI tests with the latest versions of
  `Apache Hadoop <http://hadoop.apache.org/releases.html>`_ 2.x and 3.x,
  but we expect Pydoop to also work on other Hadoop distributions. In
  particular, we have tested it on `Amazon EMR <https://aws.amazon.com/emr>`_
  (see :ref:`emr`).

These are both build time and run time requirements. At build time only, you
will also need a C++ compiler (e.g., ``yum install gcc gcc-c++``) and a JDK
(i.e., a JRE alone is not sufficient) for Pydoop's extension modules.

**Optional:**

* `Avro <https://avro.apache.org/>`_ Python implementation to enable
  :ref:`avro_io` (run time only). Note that the pip packages for Python 2 and 3
  are named differently (respectively ``avro`` and ``avro-python3``).

* Some examples have additional requirements. Check out the Dockerfile and
  ``requirements.txt`` for details.


Environment Setup
-----------------

Pydoop needs to know where the JDK and Hadoop are installed on your
system. Although it will try to guess both locations, you can help by
exporting, respectively, the ``JAVA_HOME`` and ``HADOOP_HOME`` environment
variables. For instance::

  export HADOOP_HOME="/opt/hadoop-3.0.1"
  export JAVA_HOME="/usr/lib/jvm/java-8-openjdk-amd64"

Note that Pydoop is interested in the **JDK** home (where ``include/jni.h``
can be found), not the JRE home. Depending on your Java distribution and
version, these can be different directories (usually the former being the
latter's parent).


Building and Installing
-----------------------

Install prerequisites::

  pip install --upgrade pip
  pip install --upgrade -r requirements.txt

Install Pydoop via pip::

  pip install pydoop

Or get the source code and build it locally::

  git clone -b master https://github.com/crs4/pydoop.git
  cd pydoop
  python setup.py build
  python setup.py install --skip-build

In the git repository, the ``master`` branch corresponds to the latest
release, while the ``develop`` branch contains code under active development.

Note that installing Pydoop and your MapReduce applications to all cluster
nodes (or to an NFS share) is *not* required: see :doc:`self_contained` for
additional info.


Troubleshooting
---------------

#. "java home not found" error: try setting ``JAVA_HOME`` in ``hadoop-env.sh``

#. "libjvm.so not found" error: try the following::

    export LD_LIBRARY_PATH="${JAVA_HOME}/jre/lib/amd64/server:${LD_LIBRARY_PATH}"

#. non-standard include/lib directories: the setup script looks for
   includes and libraries in standard places -- read ``setup.py`` for
   details. If some of the requirements are stored in different
   locations, you need to add them to the search path. Example::

    python setup.py build_ext -L/my/lib/path -I/my/include/path -R/my/lib/path
    python setup.py build
    python setup.py install --skip-build

   Alternatively, you can write a small ``setup.cfg`` file for distutils:

   .. code-block:: cfg

    [build_ext]
    include_dirs=/my/include/path
    library_dirs=/my/lib/path
    rpath=%(library_dirs)s

   and then run ``python setup.py install``.

   Finally, you can achieve the same result by manipulating the
   environment.  This is particularly useful in the case of automatic
   download and install with pip::

    export CPATH="/my/include/path:${CPATH}"
    export LD_LIBRARY_PATH="/my/lib/path:${LD_LIBRARY_PATH}"
    pip install pydoop

#. Hadoop version issues. The Hadoop version selected at compile time is 
   automatically detected based on the output of running ``hadoop version``.
   If this fails for any reason, you can provide the correct version string
   through the ``HADOOP_VERSION`` environment variable, e.g.::

     export HADOOP_VERSION="2.7.4"


Testing your Installation
-------------------------

After Pydoop has been successfully installed, you might want to run unit
tests and/or examples to verify that everything works fine. Here is a short
list of things that can go wrong and how to fix them. For full details on
running tests and examples, see ``.travis.yml``.

#. make sure that Pydoop is able to detect your Hadoop home and
   configuration directories.  If auto-detection fails, try setting
   the ``HADOOP_HOME`` and ``HADOOP_CONF_DIR`` environment variables
   to the appropriate locations;

#. Make sure all HDFS and YARN daemons are up (see above);

#. Wait until HDFS exits from safe mode::

     ${HADOOP_HOME}/bin/hadoop dfsadmin -safemode wait

#. HDFS tests may fail if your NameNode's hostname and port are
   non-standard. In this case, set the ``HDFS_HOST`` and ``HDFS_PORT``
   environment variables accordingly;

#. Some HDFS tests may fail if not run by the cluster superuser, in
   particular ``capacity``, ``chown`` and ``used``.  To get superuser
   privileges, you can either start the cluster with your own user account or
   set the ``dfs.permissions.superusergroup`` Hadoop property to one of your
   unix groups (type ``groups`` at the command prompt to get the list of
   groups for your current user), then restart the HDFS daemons.


.. _emr:

Using Pydoop on Amazon EMR
--------------------------

You can configure your EMR cluster to automatically install Pydoop on
all nodes via `Bootstrap Actions
<https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-bootstrap.html>`_. The
main difficulty is that Pydoop relies on Hadoop being installed and
configured, even at compile time, so the bootstrap script needs to
wait until EMR has finished setting it up:

.. code-block:: bash

  #!/bin/bash
  PYDOOP_INSTALL_SCRIPT=$(cat <<EOF
  #!/bin/bash
  NM_PID=/var/run/hadoop-yarn/yarn-yarn-nodemanager.pid
  RM_PID=/var/run/hadoop-yarn/yarn-yarn-resourcemanager.pid
  while [ ! -f \${RM_PID} ] && [ ! -f \${NM_PID} ]; do
    sleep 2
  done
  export JAVA_HOME=/etc/alternatives/java_sdk
  sudo -E pip install pydoop
  EOF
  )
  echo "${PYDOOP_INSTALL_SCRIPT}" | tee -a /tmp/pydoop_install.sh
  chmod u+x /tmp/pydoop_install.sh
  /tmp/pydoop_install.sh >/tmp/pydoop_install.out 2>/tmp/pydoop_install.err &

The bootstrap script creates the actual installation script and calls
it; the latter, in turn, waits for either the resource manager or the
node manager to be up (i.e., for YARN to be up whether we are on
the master or on a slave) before installing Pydoop. If you want to use
Python 3, install version 3.6 with yum:

.. code-block:: bash

  #!/bin/bash
  sudo yum -y install python36-devel python36-pip
  sudo alternatives --set python /usr/bin/python3.6
  PYDOOP_INSTALL_SCRIPT=$(cat <<EOF
  ...

The above instructions have been tested on ``emr-5.12.0``.
