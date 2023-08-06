# mcafee-secure-csv-tool

McAfee SECURE - CSV Creation Tool

This Python module uses the McAfee SECURE API module
and the Pandas module to generate CSV outputs from the JSON results.


This script requires two non-standard packages:

    json_normalize - a component of pandas, a data analysis package, that
        allows for the flattening of nested dictionaries found in JSON.
        
    mcafeesecure_api - a Python module for the McAfee SECURE API
    
Currently Supported API Calls:
    scan-targets, scan-target, scan-result, scan-vuln

Reports:
    full-report: Includes a listing of every found vulnerability and where it was found

Examples Uses:

    $ python3 mcafeesecure_csv.py -m scan-targets
    $ python3 mcafeesecure_csv.py -m scan-target  -t 81159
    $ python3 mcafeesecure_csv.py -m scan-result -t 81159 -s 201809072027TgDGIr3ywDIrPX1fysum
    $ python3 mcafeesecure_csv.py -m scan-vuln -v 1100894
    $ python3 mcafeesecure_csv.py -m full-report

Changelog:

    * 0.0.1- Initial release - [1/28/19]
