SELECT COUNT(*) FROM weather WHERE Date_Time IS NULL
   OR Temp_C IS NULL
   OR Dew_Point_Temp_C IS NULL
   OR Rel_Hum_Percent IS NULL
   OR Wind_Speed_km_h IS NULL
   OR Visibility_km IS NULL
   OR Press_kPa IS NULL
   OR Weather IS NULL;
