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

# An enumeration representing the different forms a verb and its associated
# phrase can take.
class Form(Enum):
    # The bare infinitive is the base form of the verb.
    BARE_INFINITIVE = 0
    # In English, the gerund form refers to the usage of a verb as a noun. For
    # example, I like swimming. In more general terms, gerunds
    # are usually formed from the base word with -ing added to the
    # end.
    GERUND = 1
    # The imperative form of a verb is the one used when the grammatical
    # mood is one of expressing a command or giving a direct request.
    IMPERATIVE = 2
    # The infinitive form represents the base form of the verb, with our
    # without the particle "to".
    INFINITIVE = 3
    # Normal form represents the base verb.
    NORMAL = 4
    # Most verbs will have only a single form for the past tense. However, some
    # verbs will have two forms, one for the simple past tense and one for the
    # past participle (also knowns as passive participle or perfect
    # participle). The part participle represents the second of these two
    # forms.
    PAST_PARTICIPLE = 5
    # The present participle is identical in form to the gerund and is normally
    # used in the active voice. However, the gerund is meant to highlight a
    # verb being used as a noun. The present participle remains as a verb.
    PRESENT_PARTICIPLE = 6

    def __str__(self):
        return self.name
