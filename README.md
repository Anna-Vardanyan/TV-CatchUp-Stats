# TV-CatchUp-Stats

This project automates the aggregation and analysis of **TV catch-up statistics** collected from multiple RTSP Linux servers.

## Process stages:

### 1.
Connect to all RTSP Linux servers (18) and download daily logs for the previous month.

### 2.
Concatenate all 18 logs from servers into single daily files per each month days.

### 3.
Count number of successful catch-up requests per catch-up asset per TV channel, find missing channel IDs (if no asset from specific channel were not requested in specific month days) and fill missing counts by 0.

### 4.
For each catch-up asset ID of each channel ID, retrieve the EPG (Electronic Program Guide) Name from the TV DB (MariaDB) and build the excel files containing the per channel program catch-up stats per day.

### 5.
Build an excel file listing all channels with per day popularity matrix for the month under consideration.
