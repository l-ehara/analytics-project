SELECT 
    country_name, 
    year, 
    inflation 
FROM df_melted 
WHERE 
    country_name = '{{ selected_country }}' 
    AND inflation IS NOT NULL
