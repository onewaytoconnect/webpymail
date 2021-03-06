# sabapp - Simple Address Book Application
# Copyright (C) 2008 Helder Guerreiro

# This file is part of sabapp.
#
# sabapp is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# sabapp is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with sabapp.  If not, see <http://www.gnu.org/licenses/>.

#
# Helder Guerreiro <helder@tretas.org>
#

from django.conf.urls import url

from sabapp import views

# Manage:
urlpatterns = [
    url(r'^add/$', views.manage_address, name='add_address'),
    url(r'^edit/(?P<address_id>\d+)/$', views.manage_address,
        name='edit_address'),
    url(r'^del/(?P<address_id>\d+)/$', views.delete_address,
        name='delete_address'),
    ]

# Browse:
urlpatterns += [
    url(r'^$', views.browse_addresses, name='browse_addresses'),
    url(r'^compose/$', views.compose_to_addresses,
        name='compose_to_addresses'),
    ]
