/* libtcod
 * Copyright © 2008-2019 Jice and the libtcod contributors.
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are met:
 *     * Redistributions of source code must retain the above copyright
 *       notice, this list of conditions and the following disclaimer.
 *     * Redistributions in binary form must reproduce the above copyright
 *       notice, this list of conditions and the following disclaimer in the
 *       documentation and/or other materials provided with the distribution.
 *     * The name of copyright holder nor the names of its contributors may not
 *       be used to endorse or promote products derived from this software
 *       without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
 * ``AS IS'' AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED
 * TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
 * PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR
 * CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
 * EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
 * PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS;
 * OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
 * WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR
 * OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
 * ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */
#include "drawing.h"

#include "../libtcod_int.h"
#include "../console.h"
/**
 *  Clamp the given values to fit within a console.
 */
static void TCOD_console_clamp(int cx, int cy, int cw, int ch,
                               int *x, int *y, int *w, int *h)
{
  if (*x + *w > cw) { *w = cw - *x; }
  if (*y + *h > ch) { *h = ch - *y; }
  if (*x < cx) {
    *w -= cx - *x;
    *x = cx;
  }
  if (*y < cy) {
    *h -= cy - *y;
    *y = cy;
  }
}
void TCOD_console_rect(TCOD_Console* con, int x, int y, int rw, int rh,
                       bool clear, TCOD_bkgnd_flag_t flag)
{
  con = TCOD_console_validate_(con);
  TCOD_IFNOT(con) { return; }
  TCOD_ASSERT(TCOD_console_is_index_valid_(con, x, y));
  TCOD_ASSERT(x + rw <= con->w && y + rh <= con->h);

  TCOD_console_clamp(0, 0, con->w, con->h, &x, &y, &rw, &rh);
  TCOD_IFNOT(rw > 0 && rh > 0) { return; }
  for (int cx = x; cx < x + rw; ++cx) {
    for (int cy = y; cy < y + rh; ++cy) {
      TCOD_console_set_char_background(con, cx, cy, con->back, flag);
      if (clear) {
        con->ch_array[cx + cy * con->w] = ' ';
      }
    }
  }
}
void TCOD_console_hline(TCOD_Console* con,int x, int y, int l,
                        TCOD_bkgnd_flag_t flag)
{
  for (int i = x; i < x + l; ++i) {
    TCOD_console_put_char(con, i, y, TCOD_CHAR_HLINE, flag);
  }
}
void TCOD_console_vline(TCOD_Console* con,int x, int y, int l,
                        TCOD_bkgnd_flag_t flag)
{
  for (int i = y; i < y + l; ++i) {
    TCOD_console_put_char(con, x, i, TCOD_CHAR_VLINE, flag);
  }
}
