import requests

"""
https://mines-coding-comp.free.mockoapp.net/infiltrateTheSystem/DeclarationofIndependence
  {"Username": "BenjaminFranklinGates",
  "Password": "c78c3829-a616-485e-a394-7d3770fb6bfc"
  }
"""

if __name__ == '__main__':

    r = requests.get("https://mines-coding-comp.free.mockoapp.net/infiltrateTheSystem/AdminAccess", headers={"Username": "BenjaminFranklinGates", "Password": "c78c3829-a616-485e-a394-7d3770fb6bfc"})
    print(r.text)