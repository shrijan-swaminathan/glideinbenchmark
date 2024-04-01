<!--
SPDX-FileCopyrightText: 2023 Fermi Research Alliance, LLC
SPDX-License-Identifier: Apache-2.0
-->

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
![.github/workflows/linters.yaml](https://github.com/mambelli/planetsmath/workflows/Linters/badge.svg)
![.github/workflows/linters.yaml](https://github.com/mambelli/planetsmath/workflows/PyTest/badge.svg)

# GlideinBenchmark

Application to benchmark GlideinWMS provisioned resources.

Runner_config allws to configure the GlideinWMS Factory to automatically run benchmarks on Glideins.

Runner alloows to trigger a benchmark on a specific resource.

Benchmarks are run using images defined in the [GlideinWMS containers repo](https://github.com/glideinWMS/containers/tree/main/worker/benchmark).

Viewer provides access to the benchmarks' results.

This code is distributed under the Apache 2.0 license, see the [LICENSE](LICENSE) file.

## Getting Started with development

There is a specfic document on this at [DEVELOPMENT.md](DEVELOPMENT.md)

## To run the web application

To run the web application, you need to export pythonpath in the following format:
    export PYTHONPATH="$PYTHONPATH:{directory_to_glideinbenchmark}/glideinbenchmark/src/"
then you can run the web application with the following command:
    python3 glideinbenchmark/src/glideinbenchmark/index.py