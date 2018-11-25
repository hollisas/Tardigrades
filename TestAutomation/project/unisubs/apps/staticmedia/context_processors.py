# Amara, universalsubtitles.org
#
# Copyright (C) 2013 Participatory Culture Foundation
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see
# http://www.gnu.org/licenses/agpl-3.0.html.

from django.conf import settings
from staticmedia import utils

def staticmedia(request):
    """Add media-related context variables to the context."""
    return {
        'MEDIA_URL': settings.MEDIA_URL,
        'STATIC_URL': utils.static_url(),
        'LOGO_URL': settings.LOGO_URL,
        'PCF_LOGO_URL': settings.PCF_LOGO_URL,
    }