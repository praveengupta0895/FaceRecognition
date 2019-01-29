import sqlite3
import cv2

conn = sqlite3.connect('Timestamp_Data.db')
print "Timestamp database opened successfully";

conn.execute("DELETE  from TIMESTAMP_DATA ;")
conn.commit()

print "Total number of rows deleted :", conn.total_changes
