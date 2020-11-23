#!/usr/bin/env python3

import sys
import yaml
import csv


def load_status(status_file):
    """
    Loads the juju status YAML formated file and returns it as a dictionary
    """
    with open(status_file, "r") as file:
        status = yaml.load(file.read(), Loader=yaml.Loader) or {}
    return status


def unit_allocation(applications):
    """
    Retuns a dictionary containing { machine: unit }
    """
    distr = {}
    for application in applications:
        if "units" in applications[application].keys():
            for unit in applications[application]["units"]:
                distr[
                    applications[application]["units"][unit]["machine"]] = unit
    return(distr)


def service_allocation(machines, application):
    """
    Returns the service allocation list: (host, bare_metal, container)
    """
    table = []
    for machine_id in machines:
        host = machines[machine_id]["display-name"]
        bmetal = ""
        lxd = ""
        if "containers" in machines[machine_id].keys():
            for container in machines[machine_id]["containers"]:
                lxd += "{}\r".format(application[container])
        bmetal = application[machine_id]
        table.append((host, bmetal, lxd.strip()))
    return(table)


def csv_out(data):
    """
    Outputs to STDOUT the cvs formatted service allocation mapping
    """
    fieldnames = ("Host", "Baremetal", "Container")
    writer = csv.writer(sys.stdout)

    writer.writerow(fieldnames)
    for item in data:
        writer.writerow(item)


def main():
    status = load_status(sys.argv[1])

    applications = unit_allocation(status["applications"])
    allocation = service_allocation(status["machines"], applications)

    csv_out(allocation)


if __name__ == '__main__':
    main()
