# -*- coding: utf-8 -*-
"""
    :copyright: (c) 2008-2013 Sigasi
    :license: BSD, see LICENSE for more details.
"""

from string import Template
import os

class LibraryMappingFileCreator:
    """A Library Mapping File Creator helps you to easily create a Sigasi Library Mapping file.

    You can add library mappings by calling the add_mapping method.
    To create the .library_mapping file content, simply call str() of your LibraryMappingFileCreator instance.

    Typical example:
        creator = LibraryMappingFileCreator()
        creator.add_mapping(test.vhd, "myLib")
        creator.add_mapping(Copy of test.vhd, "not mapped")
        return str(creator)

    """
    __LIBRARIES_TEMPLATE = Template(
        '''<?xml version="1.0" encoding="UTF-8"?>
<com.sigasi.hdt.vhdl.scoping.librarymapping.model:LibraryMappings xmlns:com.sigasi.hdt.vhdl.scoping.librarymapping.model="com.sigasi.hdt.vhdl.scoping.librarymapping" Version="2">
$mappings</com.sigasi.hdt.vhdl.scoping.librarymapping.model:LibraryMappings>
''')

    __MAPPING_TEMPLATE = Template('''  <Mappings Location="$path" Library="$library"/>
''')

    __DEFAULT_MAPPINGS = {
        "Common Libraries/IEEE":"ieee",
        "Common Libraries/IEEE Synopsys":"ieee",
        "Common Libraries":"not mapped",
        "Common Libraries/STD":"std"
    }

    def __init__(self):
        self.__entries = dict()
        self.__add_default_mappings()

    def __add_default_mappings(self):
        for path, library in self.__DEFAULT_MAPPINGS.items():
            self.add_mapping(path, library)

    def __str__(self):
        mappings = ""
        for (path, library) in sorted(self.__entries.items()):
            mappings += self.__MAPPING_TEMPLATE.substitute(
                    path=path,
                    library=library)
        return self.__LIBRARIES_TEMPLATE.substitute(mappings=mappings)

    def add_mapping(self, path, library):
        self.__entries[path] = library

    def unmap(self, path):
        self.__entries[path] = "not mapped"

    def write(self, destination):
        library_mapping_file = os.path.join(destination, ".library_mapping.xml")
        f = open(library_mapping_file, 'wb')
        try:
            f.write(str(self))
        finally:
            f.close()

from string import Template
import os


class ProjectFileCreator():
    """A Project File Creator helps you to easily create a Sigasi Project file.

    You can specify the VHDL version (93,2002 or 2008) in the constructor.

    You can add linked resources to your project by calling the add_link method.
    To create the .project file, simply call str() of your ProjectFileCreator instance.

    Typical example:
        creator = ProjectFileCreator(project_name)
        creator.add_link("test.vhd", "/home/heeckhau/shared/test.vhd")
        creator.write("/home/heeckhau/test/")

    """

    __LINK_TEMPLATE = Template(
'''\t\t<link>
\t\t\t<name>$name</name>
\t\t\t<type>$link_type</type>
\t\t\t<$loc_type>$location</$loc_type>
\t\t</link>
''')

    __PROJECT_FILE_TEMPLATE = Template(
'''<?xml version="1.0" encoding="UTF-8"?>
<projectDescription>
\t<name>${project_name}</name>
\t<comment></comment>
\t<projects>
\t</projects>
\t<buildSpec>
\t\t<buildCommand>
\t\t\t<name>org.eclipse.xtext.ui.shared.xtextBuilder</name>
\t\t\t<arguments>
\t\t\t</arguments>
\t\t</buildCommand>
\t</buildSpec>
\t<natures>
\t\t<nature>com.sigasi.hdt.vhdl.ui.vhdlNature</nature>
\t\t<nature>org.eclipse.xtext.ui.shared.xtextNature</nature>
\t</natures>
\t<linkedResources>
${links}\t</linkedResources>
</projectDescription>''')

    __DEFAULT_LINKS=[
        ["Common Libraries",Template("virtual:/virtual")],
        ["Common Libraries/IEEE",Template("sigasiresource:/vhdl/${version}/IEEE")],
        ["Common Libraries/IEEE Synopsys",Template("sigasiresource:/vhdl/${version}/IEEE%20Synopsys")],
        ["Common Libraries/STD",Template("sigasiresource:/vhdl/${version}/STD")],
    ]

    def __init__(self, project_name, version=93):
        if version not in {93, 2002, 2008}:
             raise ValueError('Only 93, 2002 and 2008 are allowed as VHDL version number')
        self.__project_name = project_name
        self.__version = version
        self.__links = []
        self.__add_default_links()

    def __add_default_links(self):
        for name, template in self.__DEFAULT_LINKS:
            self.__links.append([name, template.substitute(version=self.__version), 2, False])

    def __str__(self):
        links = ""
        for [name, location, link_type, is_path] in self.__links:
            location_type = "location" if is_path else "locationURI"
            links += self.__LINK_TEMPLATE.substitute(
                        name=name,
                        link_type=link_type,
                        loc_type=location_type,
                        location=location)

        return self.__PROJECT_FILE_TEMPLATE.substitute(
            project_name = self.__project_name,
            links=links
        )

    def add_link(self, name, location, link_type=1):
        if link_type not in {1, 2}:
             raise ValueError('Only types 1 and 2 are allowed. 1 is file, 2 is folder')
        self.__links.append([name, location, link_type, True])

    def write(self, destination):
        project_file = os.path.join(destination, ".project")
        f = open(project_file, 'wb')
        try:
            f.write(str(self))
        finally:
            f.close()


class SigasiProjectCreator():
    """This class helps you to easily create a Sigasi project (".project")
    and library mapping (".library_mapping.xml") file.

    Typical example:
        creator = SigasiProjectCreator(project_name, 93)
        creator.add_link("test.vhd", "/home/heeckhau/shared/test.vhd")
        creator.add_mapping(test.vhd, "myLib")
        creator.write("/home/heeckhau/test/")

    """

    def __init__(self, project_name, version=93):
        self.__libraryMappingFileCreator = LibraryMappingFileCreator()
        self.__projectFileCreator = ProjectFileCreator(project_name, version)

    def add_link(self, name, location, link_type=1):
        if link_type not in {1, 2}:
             raise ValueError('Only types 1 and 2 are allowed. 1 is file, 2 is folder')
        self.__projectFileCreator.add_link(name, location, link_type)

    def add_mapping(self, path, library):
        self.__libraryMappingFileCreator.add_mapping(path, library)

    def unmap(self, path):
        self.__libraryMappingFileCreator.unmap(path)

    def write(self, destination):
        self.__projectFileCreator.write(destination)
        self.__libraryMappingFileCreator.write(destination)

    def add_unisim(self, unisim_location):
        self.__projectFileCreator.add_link("Common Libraries/unisim", unisim_location, 2)
        self.__libraryMappingFileCreator.add_mapping("Common Libraries/unisim","unisims")
        self.__libraryMappingFileCreator.unmap("Common Libraries/unisim/primitive")
        self.__libraryMappingFileCreator.unmap("Common Libraries/unisim/secureip")

    def add_unimacro(self, unimacro_location):
        self.__projectFileCreator.add_link("Common Libraries/unimacro", unimacro_location, 2)
        self.__libraryMappingFileCreator.add_mapping("Common Libraries/unimacro/unimacro_VCOMP.vhd", "unimacro")

