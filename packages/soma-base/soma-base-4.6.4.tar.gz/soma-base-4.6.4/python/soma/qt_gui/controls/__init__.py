#
# SOMA - Copyright (C) CEA, 2015
# Distributed under the terms of the CeCILL-B license, as published by
# the CEA-CNRS-INRIA. Refer to the LICENSE file or to
# http://www.cecill.info/licences/Licence_CeCILL-B_V1-en.html
# for details.
#

# Soma import
from .Str import StrControlWidget
from .Float import FloatControlWidget
from .Int import IntControlWidget
from .Enum import EnumControlWidget
from .List import ListControlWidget
from .List_offscreen import OffscreenListControlWidget
from .Bool import BoolControlWidget
from .File import FileControlWidget
from .Directory import DirectoryControlWidget
from .Dict import DictControlWidget
from .Controller import ControllerControlWidget

# Define a structure that will contain the mapping between the string trait
# descriptions and the associated control classes
controls = {}

# Register all control class
controls["Str"] = StrControlWidget
controls["Unicode"] = StrControlWidget
controls["String"] = StrControlWidget
controls["Any"] = StrControlWidget
controls["Float"] = FloatControlWidget
controls["Int"] = IntControlWidget
controls["Enum"] = EnumControlWidget
controls["Bool"] = BoolControlWidget
controls["File"] = FileControlWidget
controls["Directory"] = DirectoryControlWidget
controls["List"] = ListControlWidget
controls["Instance"] = ControllerControlWidget
controls["TraitInstance"] = ControllerControlWidget
controls["ControllerTrait"] = ControllerControlWidget
controls["Dict"] = DictControlWidget
