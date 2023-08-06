#!/usr/bin/env python3
# Copyright (c) 2017-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree. An additional grant
# of patent rights can be found in the PATENTS file in the same directory.

import argparse
import logging
import sys

import yaml
from benchpress.cli.commands.list import ListCommand
from benchpress.cli.commands.run import RunCommand
from benchpress.lib.job import Job
from benchpress.lib.reporter import StdoutReporter
from benchpress.lib.reporter_factory import ReporterFactory


def setup_parser():
    """Setup the commands and command line parser.

    Returns:
        setup parser (argparse.ArgumentParser)
    """
    commands = [ListCommand(), RunCommand()]

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-b",
        "--benchmarks",
        default="benchmarks.yml",
        metavar="benchmarks file",
        help="path to benchmarks file",
    )
    parser.add_argument(
        "-j",
        "--jobs",
        default="jobs/jobs.yml",
        dest="jobs_file",
        metavar="job configs file",
        help="path to job configs file",
    )

    subparsers = parser.add_subparsers(dest="command", help="subcommand to run")
    for command in commands:
        command.populate_parser(subparsers)

    subparsers.required = True

    parser.add_argument("--verbose", "-v", action="count", default=0)

    return parser


# ignore sys.argv[0] because that is the name of the program
def main(args=sys.argv[1:]):
    # register reporter plugins before setting up the parser
    ReporterFactory.register("stdout", StdoutReporter)

    parser = setup_parser()
    args = parser.parse_args(args)

    # warn is 30, should default to 30 when verbose=0
    # each level below warning is 10 less than the previous
    log_level = args.verbose * (-10) + 30
    logging.basicConfig(format="%(levelname)s:%(name)s: %(message)s", level=log_level)
    logger = logging.getLogger(__name__)

    logger.info('Loading benchmarks from "{}"'.format(args.benchmarks))
    with open(args.benchmarks) as tests_file:
        benchmarks = yaml.load(tests_file)

    logger.info('Loading jobs from "{}"'.format(args.jobs_file))
    with open(args.jobs_file) as jobs_file:
        job_configs = yaml.load(jobs_file)

    jobs = [Job(j, benchmarks[j["benchmark"]]) for j in job_configs if "tests" not in j]
    jobs = {j.name: j for j in jobs}

    logger.info("Loaded {} benchmarks and {} jobs".format(len(benchmarks), len(jobs)))

    args.command.run(args, jobs)
