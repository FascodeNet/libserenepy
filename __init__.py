###                 GNU LESSER GENERAL PUBLIC LICENSE
###                       Version 3, 29 June 2007
### Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
### Everyone is permitted to copy and distribute verbatim copies
### of this license document, but changing it is not allowed.

# Modules importing
#from libserenepy import marker
#import asyncio

class library_info:
    LIBRARY_NAME = "libserenepy"
    BRANCH_VERSION = "Alpha"
    VERSION = "0.1.0"
    AUTHOR = "SereneTeam"
    API_VERSION = "0.1"

# Testing Code
if __name__ == "__main__":
    print("Library name: " + library_info.LIBRARY_NAME)
    print("Version: " + library_info.BRANCH_VERSION + " " +library_info.VERSION)
    print("Author: " + library_info.AUTHOR)
    print("API Version: " + library_info.API_VERSION)