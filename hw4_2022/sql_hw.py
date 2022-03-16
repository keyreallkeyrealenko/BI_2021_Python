import sqlite3
import pandas as pd
import matplotlib.pyplot as plt


def describe_dataframe(dataframe):
    """The introduction function to explore the dataframe"""
    print(dataframe.shape)
    print(dataframe.head())
    print(dataframe.info())
    plt.rcParams["figure.figsize"] = (12, 8)
    plt.plot(dataframe['count'], lw=3, c='r')
    plt.xlabel('species ID')
    plt.ylabel('number of reads belonging to the species')
    plt.show()


def create_sql_table(dataframe, connect):
    """Save pandas.DataFrame dataframe file as a SQL-table and return sqlite3.cursor instance"""
    cursor = connect.cursor()
    dataframe.to_sql('metagenome', connect, if_exists='replace', index=False)
    return cursor


def filter_table(cursor, method='percent', percent=1, count=5000):
    """This function filters SQL-table
    - percent_filter – filters SQL-table  by species present percent
    - count_filter – filters SQL-table by number of reads belonging to species
    - method – {percent, count}, default - percent. Decide how to filter SQL-table. """

    def percent_filter(cur, per):
        subset = cur.execute(f"""SELECT * FROM metagenome WHERE percent > {per}""").fetchall()
        return pd.DataFrame(subset, columns=['species', 'count', 'percent'])

    def count_filter(cur, cnt):
        subset = cur.execute(f"""SELECT * FROM metagenome WHERE count > {cnt}""").fetchall()
        return pd.DataFrame(subset, columns=['species', 'count', 'percent'])

    if method == 'percent':
        return percent_filter(cursor, percent)
    elif method == 'count':
        return count_filter(cursor, count)
    else:
        raise ValueError('Available methods are: percent and count')


def count_reads(cursor):
    """This function count number of total defined reads in SQL-table"""
    return cursor.execute("""SELECT sum(count) FROM metagenome""").fetchone()[0]


def delete_row(cursor, species):
    """Delete row with specific species ID and recount percent column"""
    cursor.execute(f"""DELETE FROM metagenome WHERE species ='{species}'""")
    total_number = count_reads(cursor)
    cursor.execute(f"""UPDATE metagenome SET percent = CAST(count*100 AS float) / {total_number}""")
    return cursor


def main():
    # This is 16S sequencing data obtained by my own from tick gut
    conn = sqlite3.connect('metagenome.db')
    data = pd.read_csv('./classified_species_BC_15.csv')
    describe_dataframe(data)
    cur = create_sql_table(data, connect=conn)
    data_flt_count = filter_table(cur, method='count', count=1000)
    print(data_flt_count.tail())
    data_flt_percent = filter_table(cur, method='percent', percent=5)
    print(data_flt_percent.tail())
    reads = count_reads(cur)
    print(f"Total number of reads: {reads}")
    delete_row(cursor= cur, species='Methylobacterium goesingense')
    conn.commit()


if __name__ == '__main__':
    main()
