# The contents of this file are subject to the Mozilla Public License
# Version 1.1 (the "License"); you may not use this file except in
# compliance with the License. You may obtain a copy of the License at
# http://www.mozilla.org/MPL/
#
# Software distributed under the License is distributed on an "AS IS"
# basis, WITHOUT WARRANTY OF ANY KIND, either express or implied. See the
# License for the specific language governing rights and limitations
# under the License.
#
# The Original Code is "Simplenlg".
#
# The Initial Developer of the Original Code is Ehud Reiter, Albert Gatt and Dave Westwater.
# Portions created by Ehud Reiter, Albert Gatt and Dave Westwater are
# Copyright (C) 2010-11 The University of Aberdeen. All Rights Reserved.
#
# Contributor(s): Ehud Reiter, Albert Gatt, Dave Wewstwater, Roman Kutlak, Margaret Mitchell.

from enum import Enum


# This is an enumeration of the two different types of clauses used in the
# SimplNLG package.
class ClauseStatus(Enum):
     # This enumeration represents a matrix clause. A matrix clause is not
     # subordinate to any other clause and therefore sits at the top-level of
     #the clause hierarchy, typically spanning the whole sentence.
    MATRIX = 0
     # The subordinate clauses are contained within a higher clause.
    SUBORDINATE = 1

    def __str__(self):
        return self.name
