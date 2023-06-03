#!/usr/bin/env python3
import atheris
import sys
import fuzz_helpers


with atheris.instrument_imports(include=['ioc_finder']):
    from ioc_finder import find_iocs
def TestOneInput(data):
    fdp = fuzz_helpers.EnhancedFuzzedDataProvider(data)
    find_iocs(fdp.ConsumeRemainingString())

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
