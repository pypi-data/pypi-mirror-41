#
# TAWF ain't web framework.
#
# Copyright (C) 2015 by Artur Wroblewski <wrobell@pld-linux.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import asyncio

from tawf import Application

import logging
logging.basicConfig(level=logging.DEBUG)

app = Application()

@app.route('/hello/{word}')
def hello(word):
    return 'hello {}'.format(word)

if __name__ == '__main__':
    # on win:
    # loop = asyncio.SelectorEventLoop()
    # asyncio.set_event_loop(loop)

    app.listen(8090, address='0.0.0.0')
    loop = asyncio.get_event_loop()
    loop.run_forever()


# vim: sw=4:et:ai
