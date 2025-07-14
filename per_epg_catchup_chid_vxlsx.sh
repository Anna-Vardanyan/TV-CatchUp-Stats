#!/bin/bash

for chid in 023 045 058 060 064 067 068 071 072 073 074 075 117 291 300 301 302 303 304 305
   do mkdir -p $chid
      for i in {01..30}
         do ./per_epg_catchup_chid_vxlsx.py 202004/all_cups_stats.log-202004$i $chid/$chid"_all_cups_202004"$i.txt $chid/$chid"_epg_date_count_202004"$i.xlsx $chid
      done
   done
