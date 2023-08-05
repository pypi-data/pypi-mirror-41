# pintail - Build static sites from collections of Mallard documents
# Copyright (c) 2016 Shaun McCance <shaunm@gnome.org>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import pintail.site

class SearchProvider(pintail.site.Extendable):
    def __init__(self, site):
        self.site = site

    def index_site(self):
        for subdir in self.site.root.iter_directories():
            self.index_directory(subdir)

    def index_directory(self, directory):
        langs = [None]
        if not self.site.get_filter(directory):
            return
        if self.site.translation_provider is not None:
            langs += self.site.translation_provider.get_directory_langs(directory)
        for page in directory.pages:
            if not self.site.get_filter(page):
                continue
            if not page.searchable:
                continue
            dms = page.get_search_domains()
            if dms[0] == 'none':
                continue
            for lc in langs:
                self.index_page(page, lang=lc)

    def index_page(self, page, lang=None):
        pass
