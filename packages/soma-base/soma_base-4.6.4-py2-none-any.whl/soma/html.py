# -*- coding: utf-8 -*-

#  This software and supporting documentation are distributed by
#      Institut Federatif de Recherche 49
#      CEA/NeuroSpin, Batiment 145,
#      91191 Gif-sur-Yvette cedex
#      France
#
# This software is governed by the CeCILL-B license under
# French law and abiding by the rules of distribution of free software.
# You can  use, modify and/or redistribute the software under the
# terms of the CeCILL-B license as circulated by CEA, CNRS
# and INRIA at the following URL "http://www.cecill.info".
#
# As a counterpart to the access to the source code and  rights to copy,
# modify and redistribute granted by the license, users are provided only
# with a limited warranty  and the software's author,  the holder of the
# economic rights,  and the successive licensors  have only  limited
# liability.
#
# In this respect, the user's attention is drawn to the risks associated
# with loading,  using,  modifying and/or developing or reproducing the
# software by the user in light of its specific status of free software,
# that may mean  that it is complicated to manipulate,  and  that  also
# therefore means  that it is reserved for developers  and  experienced
# professionals having in-depth computer knowledge. Users are therefore
# encouraged to load and test the software's suitability as regards their
# requirements in conditions enabling the security of their systems and/or
# data to be ensured and,  more generally, to use and operate it in the
# same conditions as regards security.
#
# The fact that you are presently reading this means that you have had
# knowledge of the CeCILL-B license and that you accept its terms.

'''
Utility functions for HTML format.

* author: Yann Cointepas
* organization: NeuroSpin
* license: `CeCILL B <http://www.cecill.info/licences/Licence_CeCILL-B_V1-en.html>`_
'''
__docformat__ = "restructuredtext en"

try:
    import htmlentitydefs
except ImportError:
    # python3
    import html.entities as htmlentitydefs
import six
import sys

if sys.version_info[0] >= 3:
    unicode = str

#------------------------------------------------------------------------------
#: mapping of charaters to be escaped for HTML
_htmlEscape = None
_lesserHtmlEscape = None


def htmlEscape(msg):
    """
    Replace special characters in the message by their correponding html entity.

    - returns: *unicode*
    """
    global _htmlEscape
    if _htmlEscape is None:
        if sys.version_info[0] >= 3:
            _htmlEscape = dict([(ord(j), u'&' + i + u';')
                              for i, j
                                  in six.iteritems(htmlentitydefs.entitydefs)
                                  if len(j) == 1])
        else:
            # htmlentitydefs is apparently encoded in iso-8859-1
            # (*NOT* defaultencoding)
            # (and this is not specified in the source code)
            encoding = 'iso-8859-1'
            _htmlEscape = dict(
                [(ord(j.decode(encoding)), u'&' + i.decode(encoding) + u';')
                 for i, j in six.iteritems(htmlentitydefs.entitydefs)
                 if len(j) == 1])
    return unicode(msg).translate(_htmlEscape)


def lesserHtmlEscape(msg):
    """
    Replace special characters in the message by their correponding html entity.

    - returns: *unicode*
    """
    global _lesserHtmlEscape
    if _lesserHtmlEscape is None:
        if sys.version_info[0] >= 3:
            _lesserHtmlEscape = dict([(ord(j), u'&' + i + u';')
                                    for i, j
                                    in six.iteritems(htmlentitydefs.entitydefs)
                                    if len(j) == 1 and j not in
                                        (u'"', u'é', u'à', u'è', u'â', u'ê',
                                         u'ô', u'î', u'û', u'ù', u'ö', )])
        else:
            # htmlentitydefs is apparently encoded in iso-8859-1
            # (*NOT* defaultencoding)
            # (and this is not specified in the source code)
            encoding = 'iso-8859-1'
            _lesserHtmlEscape = dict(
                [(ord(j.decode(encoding)), u'&' + i.decode(encoding) + u';')
                 for i, j in six.iteritems(htmlentitydefs.entitydefs)
                 if len(j) == 1 and j.decode(encoding) not in
                    (u'"', u'é', u'à', u'è', u'â', u'ê',
                     u'ô', u'î', u'û', u'ù', u'ö', )])
    return unicode(msg).translate(_lesserHtmlEscape)
