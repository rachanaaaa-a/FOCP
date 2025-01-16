#1Using command-line arguments involves the sys module. Review the docs for thismodule and using the information in there write a short program that when run
#from the command-line reports what operating system platform is being used.
import sys
platform = sys.platform
print(f"Operating system platform: {platform}")
