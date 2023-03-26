class PackageContents:

    def __init__(self, ea_rep):
        self.ea_rep = ea_rep

    def get_subpackages_from_package_recursively(self, input_package, pkg_list=[]):
        """Return a recursive list of packages

        Retrieve a recursive list of subpackages in the input package "package_guid"

        Args:
            self

        Returns:
            pkg_list (list of COM objects): A list containing COM objects for EA packages
        """

        package = self.ea_rep.GetPackageByGUID(input_package)
        pkg_list.append(package)
        subpackages = package.Packages
        for subpackage in subpackages:
            PackageContents.get_subpackages_from_package_recursively(self, subpackage.PackageGUID)
        return pkg_list
