from psda.io_data.input import (
    excel_to_df_school,
    excel_to_df_population
)
from psda.io_data.output import (
    output_csv,
    output_report
)
from psda.process.fix_data import fix_school
from psda.process.process_data import (
    create_dict_of_districts,
    compute_ratio,
    compute_students_per_school,
    process_school
)
from psda.stats.compute import (
    stat_students_per_school,
    stat_students_per_teacher
)


# INPUT
path_to_school_data = "./data/wykaz_placowek.xlsx"
path_to_population_data = "./data/tabela12.xls"
df_schools = excel_to_df_school(path_to_school_data)
df_population = excel_to_df_population(path_to_population_data)

# FIXING INCONSISTENCY IN DATA & PROCESSING DATA
dict_of_districts = create_dict_of_districts(df_population)
df_schools_fixed = fix_school(df_schools, dict_of_districts)
df_schools_processed = process_school(df_schools_fixed, dict_of_districts)

# COMPUTING STATISTICS
students_total = df_schools.students.sum()
students_processed = df_schools_processed.students.sum()
frac_of_students_dropped = 1 - (students_processed / students_total)
spt1 = stat_students_per_teacher(df_schools_processed, ["district_type", "school_type"])
spt2 = stat_students_per_teacher(df_schools_processed, ["voivo", "county", "district", "school_type"])
sps = stat_students_per_school(df_schools_processed, ["district_type"])

# OUTPUT
output_csv(spt1, "stat_students_per_teacher_by_district_type_school_type")
output_csv(spt2, "stat_students_per_teacher_by_voivodeship_county_district_school_type")
output_csv(sps, "stat_students_per_school_by_district_type_year")
output_report(df_schools, df_schools_processed, "report")
