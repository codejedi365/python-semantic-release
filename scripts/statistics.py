from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from textwrap import dedent
from typing import TYPE_CHECKING

import tomli
from flatdict import FlatDict
from google.cloud.bigquery import Client as BigQueryClient

if TYPE_CHECKING:
    pass

DATA_PYPI_DOWNLOADS_TABLE = "bigquery-public-data.pypi.file_downloads"
DATA_PYPI_UPLOADS_TABLE = "bigquery-public-data.pypi.distribution_metadata"


def execute_query(client: BigQueryClient, query: str):
    query_job = client.query(query)
    return query_job.result()  # Waits for job to complete.


def print_statistics():
    print("Monthly Statistics")
    print("------------------")
    print("Average Downloads/Week: ")
    print("TOP 3 Most Downloaded Version(s): ")
    print("Most Popular Python Version: ")
    print("Most Popular Operating System: ")
    # Downloading in a CI? -- Can I detect GitHub actions since CI=True and pip usage?

    print("Yearly Statistics")
    print("-----------------")
    print("Average Downloads/Month: ")  # 411,726/month in 2024
    print("TOP 3 Most Downloaded Version(s): ")  # 7.33.2, 7.34.6, 7.29.0
    print("Most Popular Python Version: ")  # 3.9
    print("Most Popular Operating System: ")  # Linux

    # Trends
    # Difference in last month vs this month
    # Adoption rate of new versions (growth rate from release to now)
    # Detect Change in most popular versions (change in top 3)
    # Detect Change in Python version popularity


if __name__ == "__main__":
    pyproject_toml = FlatDict(
        tomli.loads(Path("pyproject.toml").read_text()), delimiter="."
    )
    PROJECT_NAME = pyproject_toml["project.name"]

    # timezone aware date object
    todays_date = datetime.now(timezone.utc).astimezone()
    client = BigQueryClient()

    # -- Only query the last 12 months of history
    yearly_dwnloads_per_month_query = dedent(
        """\
        SELECT
            COUNT(*) AS num_downloads,
            DATE_TRUNC(DATE(timestamp), MONTH) AS `month`
        FROM `bigquery-public-data.pypi.file_downloads`
        WHERE
            file.project = 'python-semantic-release'
        AND
            details.installer.name != 'bandersnatch'
        AND
            details.installer.name IS NOT NULL
        AND DATE(timestamp)
            BETWEEN DATE_TRUNC(DATE_SUB(CURRENT_DATE(), INTERVAL 11 MONTH), MONTH)
            AND CURRENT_DATE()
        GROUP BY `month`
        ORDER BY `month` DESC
        """
    )

    monthly_download_totals = execute_query(client, yearly_dwnloads_per_month_query)
    # Query results from 26 November 2024
    # monthly_download_totals = [
    #     {"num_downloads": "694086", "month": "2024-11-01"},
    #     {"num_downloads": "592320", "month": "2024-10-01"},
    #     {"num_downloads": "597927", "month": "2024-09-01"},
    #     {"num_downloads": "441164", "month": "2024-08-01"},
    #     {"num_downloads": "396260", "month": "2024-07-01"},
    #     {"num_downloads": "315072", "month": "2024-06-01"},
    #     {"num_downloads": "320001", "month": "2024-05-01"},
    #     {"num_downloads": "309450", "month": "2024-04-01"},
    #     {"num_downloads": "343425", "month": "2024-03-01"},
    #     {"num_downloads": "317188", "month": "2024-02-01"},
    #     {"num_downloads": "324304", "month": "2024-01-01"},
    #     {"num_downloads": "289517", "month": "2023-12-01"},
    # ]

    print_statistics()

    yearly_downloads_per_psr_version_query = dedent(
        """\
        SELECT
            REGEXP_EXTRACT(file.version, r"[0-9]+\\.[0-9]+") AS psr_version,
            COUNT(*) AS num_downloads,
        FROM `bigquery-public-data.pypi.file_downloads`
        WHERE
            file.project = 'python-semantic-release'
        AND
            details.installer.name != 'bandersnatch'
        AND
            details.installer.name IS NOT NULL
        AND DATE(timestamp)
            BETWEEN DATE_TRUNC(DATE_SUB(CURRENT_DATE(), INTERVAL 11 MONTH), MONTH)
            AND CURRENT_DATE()
        GROUP BY psr_version
        ORDER BY num_downloads DESC
        """
    )

    yearly_downloads_per_psr_version = execute_query(
        client, yearly_downloads_per_psr_version_query
    )
    # Query results from 28 November 2024
    yearly_downloads_per_psr_version = [
        {"psr_version": "7.33", "num_downloads": "1199619"},
        {"psr_version": "9.8", "num_downloads": "651296"},
        {"psr_version": "7.34", "num_downloads": "493056"},
        {"psr_version": "7.29", "num_downloads": "446695"},
        {"psr_version": "7.15", "num_downloads": "390470"},
        {"psr_version": "7.2", "num_downloads": "367649"},
        {"psr_version": "8.7", "num_downloads": "258593"},
        {"psr_version": "7.32", "num_downloads": "162925"},
        {"psr_version": "9.1", "num_downloads": "87521"},
        {"psr_version": "9.12", "num_downloads": "75443"},
        {"psr_version": "9.7", "num_downloads": "69090"},
        {"psr_version": "9.4", "num_downloads": "66323"},
        {"psr_version": "8.5", "num_downloads": "63823"},
        {"psr_version": "7.28", "num_downloads": "62842"},
        {"psr_version": "8.0", "num_downloads": "59967"},
        {"psr_version": "8.3", "num_downloads": "55424"},
        {"psr_version": "8.1", "num_downloads": "55380"},
        {"psr_version": "9.14", "num_downloads": "54455"},
        {"psr_version": "9.9", "num_downloads": "33176"},
        {"psr_version": "9.3", "num_downloads": "32779"},
        {"psr_version": "7.31", "num_downloads": "24755"},
        {"psr_version": "9.5", "num_downloads": "24127"},
        {"psr_version": "9.0", "num_downloads": "22150"},
        {"psr_version": "9.6", "num_downloads": "21857"},
        {"psr_version": "9.11", "num_downloads": "19029"},
        {"psr_version": "7.19", "num_downloads": "18862"},
        {"psr_version": "9.10", "num_downloads": "17988"},
        {"psr_version": "9.2", "num_downloads": "17423"},
        {"psr_version": "7.27", "num_downloads": "13870"},
        {"psr_version": "7.25", "num_downloads": "10604"},
        {"psr_version": "8.4", "num_downloads": "5918"},
        {"psr_version": "8.2", "num_downloads": "5747"},
        {"psr_version": "7.13", "num_downloads": "5340"},
        {"psr_version": "8.6", "num_downloads": "5193"},
        {"psr_version": "7.16", "num_downloads": "4927"},
        {"psr_version": "9.13", "num_downloads": "3912"},
        {"psr_version": "7.30", "num_downloads": "2505"},
        {"psr_version": "7.23", "num_downloads": "2288"},
        {"psr_version": "7.26", "num_downloads": "2168"},
        {"psr_version": "7.7", "num_downloads": "2114"},
        {"psr_version": "7.24", "num_downloads": "2082"},
        {"psr_version": "3.3", "num_downloads": "1675"},
        {"psr_version": "4.3", "num_downloads": "1571"},
        {"psr_version": "0.5", "num_downloads": "1083"},
        {"psr_version": "7.12", "num_downloads": "1008"},
        {"psr_version": "3.10", "num_downloads": "998"},
        {"psr_version": "7.22", "num_downloads": "886"},
        {"psr_version": "7.20", "num_downloads": "785"},
        {"psr_version": "7.21", "num_downloads": "780"},
        {"psr_version": "5.2", "num_downloads": "769"},
        {"psr_version": "7.18", "num_downloads": "748"},
        {"psr_version": "7.17", "num_downloads": "744"},
        {"psr_version": "3.11", "num_downloads": "744"},
        {"psr_version": "7.8", "num_downloads": "714"},
        {"psr_version": "7.14", "num_downloads": "684"},
        {"psr_version": "5.0", "num_downloads": "667"},
        {"psr_version": "7.3", "num_downloads": "652"},
        {"psr_version": "6.0", "num_downloads": "612"},
        {"psr_version": "4.1", "num_downloads": "611"},
        {"psr_version": "7.1", "num_downloads": "555"},
        {"psr_version": "3.2", "num_downloads": "545"},
        {"psr_version": "2.1", "num_downloads": "526"},
        {"psr_version": "6.4", "num_downloads": "521"},
        {"psr_version": "4.12", "num_downloads": "511"},
        {"psr_version": "7.4", "num_downloads": "465"},
        {"psr_version": "3.9", "num_downloads": "456"},
        {"psr_version": "6.3", "num_downloads": "456"},
        {"psr_version": "4.0", "num_downloads": "453"},
        {"psr_version": "0.3", "num_downloads": "430"},
        {"psr_version": "4.7", "num_downloads": "408"},
        {"psr_version": "4.5", "num_downloads": "407"},
        {"psr_version": "3.4", "num_downloads": "395"},
        {"psr_version": "3.5", "num_downloads": "391"},
        {"psr_version": "3.7", "num_downloads": "310"},
        {"psr_version": "3.6", "num_downloads": "304"},
        {"psr_version": "7.0", "num_downloads": "289"},
        {"psr_version": "7.9", "num_downloads": "252"},
        {"psr_version": "5.1", "num_downloads": "244"},
        {"psr_version": "7.11", "num_downloads": "242"},
        {"psr_version": "4.6", "num_downloads": "239"},
        {"psr_version": "7.10", "num_downloads": "237"},
        {"psr_version": "7.5", "num_downloads": "233"},
        {"psr_version": "6.2", "num_downloads": "233"},
        {"psr_version": "3.8", "num_downloads": "231"},
        {"psr_version": "6.1", "num_downloads": "231"},
        {"psr_version": "7.6", "num_downloads": "230"},
        {"psr_version": "0.9", "num_downloads": "225"},
        {"psr_version": "4.4", "num_downloads": "215"},
        {"psr_version": "0.4", "num_downloads": "214"},
        {"psr_version": "4.8", "num_downloads": "211"},
        {"psr_version": "4.2", "num_downloads": "210"},
        {"psr_version": "4.10", "num_downloads": "210"},
        {"psr_version": "4.11", "num_downloads": "204"},
        {"psr_version": "4.9", "num_downloads": "203"},
        {"psr_version": "1.0", "num_downloads": "117"},
        {"psr_version": "0.6", "num_downloads": "111"},
        {"psr_version": "3.0", "num_downloads": "111"},
        {"psr_version": "0.7", "num_downloads": "110"},
        {"psr_version": "3.1", "num_downloads": "109"},
        {"psr_version": "0.8", "num_downloads": "108"},
        {"psr_version": "2.0", "num_downloads": "108"},
    ]

    #     {"psr_version": "7.33.2", "num_downloads": "757042"},
    #     {"psr_version": "7.34.6", "num_downloads": "498464"},
    #     {"psr_version": "7.29.0", "num_downloads": "486059"},
    #     {"psr_version": "7.2.2", "num_downloads": "421335"},
    #     {"psr_version": "7.33.0", "num_downloads": "382033"},
    #     {"psr_version": "7.15.3", "num_downloads": "380188"},
    #     {"psr_version": "8.7.0", "num_downloads": "259018"},
    #     {"psr_version": "9.8.4", "num_downloads": "202668"},
    #     {"psr_version": "9.8.6", "num_downloads": "112084"},
    #     {"psr_version": "9.8.8", "num_downloads": "107331"},
    #     {"psr_version": "7.32.1", "num_downloads": "95282"},
    #     {"psr_version": "8.3.0", "num_downloads": "93200"},
    #     {"psr_version": "7.28.1", "num_downloads": "62129"},
    #     {"psr_version": "9.1.1", "num_downloads": "62004"},
    #     {"psr_version": "9.12.0", "num_downloads": "59540"},
    #     {"psr_version": "7.32.2", "num_downloads": "58409"},
    #     {"psr_version": "9.8.3", "num_downloads": "56626"},
    #     {"psr_version": "9.8.5", "num_downloads": "51177"},
    #     {"psr_version": "9.14.0", "num_downloads": "46559"},
    #     {"psr_version": "7.33.3", "num_downloads": "44974"},
    #     {"psr_version": "8.0.8", "num_downloads": "41137"},
    #     {"psr_version": "9.8.7", "num_downloads": "40687"},
    #     {"psr_version": "9.7.3", "num_downloads": "36945"},
    #     {"psr_version": "9.8.1", "num_downloads": "35315"},
    #     {"psr_version": "8.5.1", "num_downloads": "34717"},
    #     {"psr_version": "9.9.0", "num_downloads": "33423"},
    #     {"psr_version": "8.1.2", "num_downloads": "33198"},
    #     {"psr_version": "9.4.2", "num_downloads": "29278"},
    #     {"psr_version": "9.1.0", "num_downloads": "27522"},
    #     {"psr_version": "9.5.0", "num_downloads": "25021"},
    #     {"psr_version": "9.8.0", "num_downloads": "22789"},
    #     {"psr_version": "9.6.0", "num_downloads": "22488"},
    #     {"psr_version": "9.3.1", "num_downloads": "22353"},
    #     {"psr_version": "9.4.1", "num_downloads": "21201"},
    #     {"psr_version": "7.32.0", "num_downloads": "21147"},
    #     {"psr_version": "9.8.9", "num_downloads": "20569"},
    #     {"psr_version": "8.1.1", "num_downloads": "19857"},
    #     {"psr_version": "9.4.0", "num_downloads": "18678"},
    #     {"psr_version": "9.0.3", "num_downloads": "18392"},
    #     {"psr_version": "8.5.0", "num_downloads": "18024"},
    #     {"psr_version": "7.19.2", "num_downloads": "16611"},
    #     {"psr_version": "7.29.6", "num_downloads": "16094"},
    #     {"psr_version": "9.7.1", "num_downloads": "15443"},
    #     {"psr_version": "7.31.2", "num_downloads": "14920"},
    #     {"psr_version": "7.27.0", "num_downloads": "14327"},
    #     {"psr_version": "7.33.5", "num_downloads": "14327"},
    #     {"psr_version": "8.5.2", "num_downloads": "13773"},
    #     {"psr_version": "9.7.2", "num_downloads": "12870"},
    #     {"psr_version": "9.3.0", "num_downloads": "12221"},
    #     {"psr_version": "9.11.1", "num_downloads": "12136"},
    #     {"psr_version": "7.34.0", "num_downloads": "11178"},
    #     {"psr_version": "9.10.0", "num_downloads": "10342"},
    #     {"psr_version": "9.12.2", "num_downloads": "9449"},
    #     {"psr_version": "9.2.2", "num_downloads": "9332"},
    #     {"psr_version": "8.0.5", "num_downloads": "9185"},
    #     {"psr_version": "8.1.0", "num_downloads": "8880"},
    #     {"psr_version": "9.10.1", "num_downloads": "8623"},
    #     {"psr_version": "9.7.0", "num_downloads": "7537"},
    #     {"psr_version": "9.11.0", "num_downloads": "7482"},
    #     {"psr_version": "9.8.2", "num_downloads": "7146"},
    #     {"psr_version": "8.2.0", "num_downloads": "6988"},
    #     {"psr_version": "7.34.3", "num_downloads": "6985"},
    #     {"psr_version": "8.4.0", "num_downloads": "6802"},
    #     {"psr_version": "8.0.4", "num_downloads": "6708"},
    #     {"psr_version": "7.34.4", "num_downloads": "6206"},
    #     {"psr_version": "9.12.1", "num_downloads": "6197"},
    #     {"psr_version": "9.2.0", "num_downloads": "6180"},
    #     {"psr_version": "8.6.0", "num_downloads": "6067"},
    #     {"psr_version": "7.33.1", "num_downloads": "5482"},
    #     {"psr_version": "9.0.2", "num_downloads": "5404"},
    #     {"psr_version": "7.25.2", "num_downloads": "5400"},
    #     {"psr_version": "7.31.4", "num_downloads": "5372"},
    #     {"psr_version": "7.33.4", "num_downloads": "5193"},
    #     {"psr_version": "7.25.1", "num_downloads": "5148"},
    #     {"psr_version": "7.13.2", "num_downloads": "4609"},
    #     {"psr_version": "7.31.0", "num_downloads": "4330"},
    #     {"psr_version": "7.28.0", "num_downloads": "4313"},
    #     {"psr_version": "9.2.1", "num_downloads": "4248"},
    #     {"psr_version": "9.13.0", "num_downloads": "3837"},
    #     {"psr_version": "8.0.7", "num_downloads": "3776"},
    #     {"psr_version": "8.0.0", "num_downloads": "3575"},
    #     {"psr_version": "7.31.1", "num_downloads": "3019"},
    #     {"psr_version": "7.23.0", "num_downloads": "2818"},
    #     {"psr_version": "7.34.5", "num_downloads": "2695"},
    #     {"psr_version": "7.26.0", "num_downloads": "2685"},
    #     {"psr_version": "7.24.0", "num_downloads": "2603"},
    #     {"psr_version": "7.7.0", "num_downloads": "2502"},
    #     {"psr_version": "7.34.2", "num_downloads": "2494"},
    #     {"psr_version": "8.0.6", "num_downloads": "2475"},
    #     {"psr_version": "7.16.2", "num_downloads": "2379"},
    #     {"psr_version": "7.19.1", "num_downloads": "2362"},
    #     {"psr_version": "8.0.2", "num_downloads": "2261"},
    #     {"psr_version": "8.0.3", "num_downloads": "2229"},
    #     {"psr_version": "7.27.1", "num_downloads": "2145"},
    #     {"psr_version": "7.29.1", "num_downloads": "2096"},
    #     {"psr_version": "8.0.1", "num_downloads": "2033"},
    #     {"psr_version": "7.29.4", "num_downloads": "1772"},
    #     {"psr_version": "7.15.4", "num_downloads": "1732"},
    #     {"psr_version": "7.29.2", "num_downloads": "1665"},
    #     {"psr_version": "7.25.0", "num_downloads": "1579"},
    #     {"psr_version": "7.31.3", "num_downloads": "1485"},
    #     {"psr_version": "7.15.5", "num_downloads": "1455"},
    #     {"psr_version": "7.29.5", "num_downloads": "1453"},
    #     {"psr_version": "7.12.0", "num_downloads": "1415"},
    #     {"psr_version": "7.15.1", "num_downloads": "1395"},
    #     {"psr_version": "7.29.3", "num_downloads": "1323"},
    #     {"psr_version": "7.1.1", "num_downloads": "1302"},
    #     {"psr_version": "7.22.0", "num_downloads": "1282"},
    #     {"psr_version": "7.30.2", "num_downloads": "1278"},
    #     {"psr_version": "7.30.1", "num_downloads": "1260"},
    #     {"psr_version": "7.16.1", "num_downloads": "1248"},
    #     {"psr_version": "7.29.7", "num_downloads": "1246"},
    #     {"psr_version": "7.15.0", "num_downloads": "1233"},
    #     {"psr_version": "7.30.0", "num_downloads": "1225"},
    #     {"psr_version": "7.34.1", "num_downloads": "1209"},
    #     {"psr_version": "5.2.0", "num_downloads": "1197"},
    #     {"psr_version": "7.20.0", "num_downloads": "1181"},
    #     {"psr_version": "7.21.0", "num_downloads": "1178"},
    #     {"psr_version": "7.15.6", "num_downloads": "1178"},
    #     {"psr_version": "7.19.0", "num_downloads": "1146"},
    #     {"psr_version": "7.16.0", "num_downloads": "1139"},
    #     {"psr_version": "7.16.3", "num_downloads": "1137"},
    #     {"psr_version": "7.18.0", "num_downloads": "1136"},
    #     {"psr_version": "7.17.0", "num_downloads": "1135"},
    #     {"psr_version": "7.16.4", "num_downloads": "1130"},
    #     {"psr_version": "7.3.0", "num_downloads": "1112"},
    #     {"psr_version": "3.11.2", "num_downloads": "1106"},
    #     {"psr_version": "7.14.0", "num_downloads": "1075"},
    #     {"psr_version": "7.13.1", "num_downloads": "1070"},
    #     {"psr_version": "7.13.0", "num_downloads": "1064"},
    #     {"psr_version": "3.3.0", "num_downloads": "1023"},
    #     {"psr_version": "3.9.0", "num_downloads": "993"},
    #     {"psr_version": "7.2.1", "num_downloads": "908"},
    #     {"psr_version": "4.3.3", "num_downloads": "906"},
    #     {"psr_version": "7.2.5", "num_downloads": "851"},
    #     {"psr_version": "3.3.2", "num_downloads": "817"},
    #     {"psr_version": "7.2.0", "num_downloads": "814"},
    #     {"psr_version": "3.4.0", "num_downloads": "810"},
    #     {"psr_version": "3.3.3", "num_downloads": "806"},
    #     {"psr_version": "3.5.0", "num_downloads": "805"},
    #     {"psr_version": "4.3.2", "num_downloads": "802"},
    #     {"psr_version": "3.3.1", "num_downloads": "792"},
    #     {"psr_version": "6.0.0", "num_downloads": "697"},
    #     {"psr_version": "8.0.0rc4", "num_downloads": "673"},
    #     {"psr_version": "8.0.0rc3", "num_downloads": "671"},
    #     {"psr_version": "4.12.1", "num_downloads": "630"},
    #     {"psr_version": "6.4.1", "num_downloads": "618"},
    #     {"psr_version": "3.10.0", "num_downloads": "618"},
    #     {"psr_version": "3.7.1", "num_downloads": "614"},
    #     {"psr_version": "5.0.2", "num_downloads": "614"},
    #     {"psr_version": "4.3.0", "num_downloads": "614"},
    #     {"psr_version": "7.0.0", "num_downloads": "612"},
    #     {"psr_version": "3.6.0", "num_downloads": "608"},
    #     {"psr_version": "8.0.0rc2", "num_downloads": "574"},
    #     {"psr_version": "7.11.0", "num_downloads": "573"},
    #     {"psr_version": "7.9.0", "num_downloads": "573"},
    #     {"psr_version": "3.2.1", "num_downloads": "568"},
    #     {"psr_version": "7.2.4", "num_downloads": "559"},
    #     {"psr_version": "7.8.1", "num_downloads": "558"},
    #     {"psr_version": "5.1.0", "num_downloads": "558"},
    #     {"psr_version": "7.8.0", "num_downloads": "558"},
    #     {"psr_version": "7.10.0", "num_downloads": "558"},
    #     {"psr_version": "7.4.0", "num_downloads": "555"},
    #     {"psr_version": "7.1.0", "num_downloads": "551"},
    #     {"psr_version": "7.5.0", "num_downloads": "545"},
    #     {"psr_version": "6.2.0", "num_downloads": "545"},
    #     {"psr_version": "4.6.0", "num_downloads": "545"},
    #     {"psr_version": "7.8.2", "num_downloads": "544"},
    #     {"psr_version": "7.4.1", "num_downloads": "544"},
    #     {"psr_version": "7.6.0", "num_downloads": "543"},
    #     {"psr_version": "6.0.1", "num_downloads": "543"},
    #     {"psr_version": "6.3.0", "num_downloads": "542"},
    #     {"psr_version": "6.1.0", "num_downloads": "541"},
    #     {"psr_version": "6.3.1", "num_downloads": "539"},
    #     {"psr_version": "6.4.0", "num_downloads": "538"},
    #     {"psr_version": "4.10.0", "num_downloads": "526"},
    #     {"psr_version": "7.2.3", "num_downloads": "525"},
    #     {"psr_version": "4.4.0", "num_downloads": "524"},
    #     {"psr_version": "4.7.0", "num_downloads": "519"},
    #     {"psr_version": "4.2.0", "num_downloads": "517"},
    #     {"psr_version": "4.12.0", "num_downloads": "515"},
    #     {"psr_version": "4.8.0", "num_downloads": "514"},
    #     {"psr_version": "4.3.4", "num_downloads": "513"},
    #     {"psr_version": "4.5.0", "num_downloads": "513"},
    #     {"psr_version": "4.11.0", "num_downloads": "513"},
    #     {"psr_version": "5.0.0", "num_downloads": "512"},
    #     {"psr_version": "4.5.1", "num_downloads": "510"},
    #     {"psr_version": "4.1.1", "num_downloads": "510"},
    #     {"psr_version": "4.1.0", "num_downloads": "509"},
    #     {"psr_version": "4.3.1", "num_downloads": "507"},
    #     {"psr_version": "5.0.1", "num_downloads": "507"},
    #     {"psr_version": "4.9.0", "num_downloads": "506"},
    #     {"psr_version": "4.1.2", "num_downloads": "506"},
    #     {"psr_version": "3.11.0", "num_downloads": "504"},
    #     {"psr_version": "4.7.1", "num_downloads": "501"},
    #     {"psr_version": "8.0.0rc1", "num_downloads": "501"},
    #     {"psr_version": "8.0.0a8", "num_downloads": "500"},
    #     {"psr_version": "8.0.0a6", "num_downloads": "500"},
    #     {"psr_version": "4.0.1", "num_downloads": "500"},
    #     {"psr_version": "8.0.0a7", "num_downloads": "496"},
    #     {"psr_version": "8.0.0a5", "num_downloads": "495"},
    #     {"psr_version": "8.0.0a4", "num_downloads": "486"},
    #     {"psr_version": "8.0.0a3", "num_downloads": "484"},
    #     {"psr_version": "3.10.2", "num_downloads": "399"},
    #     {"psr_version": "0.5.1", "num_downloads": "397"},
    #     {"psr_version": "3.8.1", "num_downloads": "396"},
    #     {"psr_version": "3.10.1", "num_downloads": "396"},
    #     {"psr_version": "3.10.3", "num_downloads": "392"},
    #     {"psr_version": "3.11.1", "num_downloads": "392"},
    #     {"psr_version": "0.3.2", "num_downloads": "387"},
    #     {"psr_version": "0.5.4", "num_downloads": "386"},
    #     {"psr_version": "0.5.0", "num_downloads": "385"},
    #     {"psr_version": "0.4.0", "num_downloads": "385"},
    #     {"psr_version": "0.5.2", "num_downloads": "384"},
    #     {"psr_version": "3.2.0", "num_downloads": "383"},
    #     {"psr_version": "0.3.1", "num_downloads": "382"},
    #     {"psr_version": "0.5.3", "num_downloads": "379"},
    #     {"psr_version": "4.0.0", "num_downloads": "320"},
    #     {"psr_version": "4.0.2", "num_downloads": "290"},
    #     {"psr_version": "0.7.0", "num_downloads": "279"},
    #     {"psr_version": "2.1.3", "num_downloads": "279"},
    #     {"psr_version": "1.0.0", "num_downloads": "277"},
    #     {"psr_version": "0.6.0", "num_downloads": "276"},
    #     {"psr_version": "0.8.0", "num_downloads": "274"},
    #     {"psr_version": "0.9.0", "num_downloads": "272"},
    #     {"psr_version": "2.0.0", "num_downloads": "272"},
    #     {"psr_version": "0.9.1", "num_downloads": "271"},
    #     {"psr_version": "2.1.0", "num_downloads": "270"},
    #     {"psr_version": "3.0.0", "num_downloads": "269"},
    #     {"psr_version": "3.1.0", "num_downloads": "267"},
    #     {"psr_version": "2.1.1", "num_downloads": "266"},
    #     {"psr_version": "2.1.2", "num_downloads": "266"},
    #     {"psr_version": "2.1.4", "num_downloads": "260"},
    # ]

    yearly_downloads_per_python_version_query = dedent(
        """\
        SELECT
            REGEXP_EXTRACT(details.python, r"[0-9]+\\.[0-9]+") AS python_version,
            COUNT(*) AS num_downloads,
        FROM `bigquery-public-data.pypi.file_downloads`
        WHERE
            file.project = 'python-semantic-release'
        AND
            details.installer.name != 'bandersnatch'
        AND
            details.installer.name IS NOT NULL
        AND DATE(timestamp)
            BETWEEN DATE_TRUNC(DATE_SUB(CURRENT_DATE(), INTERVAL 11 MONTH), MONTH)
            AND CURRENT_DATE()
        GROUP BY python_version
        ORDER BY num_downloads DESC
        """
    )

    yearly_downloads_per_python_version = execute_query(
        client, yearly_downloads_per_python_version_query
    )
    # Query results from 26 November 2024
    # yearly_downloads_per_python_version = [
    #     {"python_version": None, "num_downloads": "1448423"},
    #     {"python_version": "3.9", "num_downloads": "1032966"},
    #     {"python_version": "3.11", "num_downloads": "935699"},
    #     {"python_version": "3.10", "num_downloads": "757107"},
    #     {"python_version": "3.8", "num_downloads": "691441"},
    #     {"python_version": "3.12", "num_downloads": "304391"},
    #     {"python_version": "3.7", "num_downloads": "58234"},
    #     {"python_version": "3.13", "num_downloads": "15347"},
    #     {"python_version": "3.6", "num_downloads": "9407"},
    #     {"python_version": "2.7", "num_downloads": "4523"},
    #     {"python_version": "3.3", "num_downloads": "28"},
    #     {"python_version": "3.5", "num_downloads": "4"},
    # ]

    yearly_downloads_per_os_version_query = dedent(
        """\
        SELECT
            details.system.name AS os_type,
        COUNT(*) AS num_downloads,
        FROM `bigquery-public-data.pypi.file_downloads`
        WHERE
            file.project = 'python-semantic-release'
        AND
            details.installer.name != 'bandersnatch'
        AND
            details.installer.name IS NOT NULL
        AND DATE(timestamp)
            BETWEEN DATE_TRUNC(DATE_SUB(CURRENT_DATE(), INTERVAL 11 MONTH), MONTH)
            AND CURRENT_DATE()
        GROUP BY os_type
        ORDER BY num_downloads DESC
        """
    )
    # Query results from 26 November 2024
    # yearly_downloads_per_os_version = [
    #     {"os_type": "Linux", "num_downloads": "4752958"},
    #     {"os_type": None, "num_downloads": "416245"},
    #     {"os_type": "Windows", "num_downloads": "44473"},
    #     {"os_type": "Darwin", "num_downloads": "43726"},
    #     {"os_type": "CYGWIN_NT-6.1-7601", "num_downloads": "5"},
    #     {"os_type": "iOS", "num_downloads": "2"},
    #     {"os_type": "mobile", "num_downloads": "1"},
    # ]

    yearly_downloads_per_installer_query = dedent(
        """\
        SELECT
            details.installer.name AS installer,
            COUNT(*) AS num_downloads,
        FROM `bigquery-public-data.pypi.file_downloads`
        WHERE
            file.project = 'python-semantic-release'
        AND DATE(timestamp)
            BETWEEN DATE_TRUNC(DATE_SUB(CURRENT_DATE(), INTERVAL 12 MONTH), MONTH)
            AND CURRENT_DATE()
        GROUP BY installer
        ORDER BY num_downloads DESC
        """
    )

    yearly_downloads_per_installer = execute_query(
        client, yearly_downloads_per_installer_query
    )
    # Query results from 26 November 2024
    # yearly_downloads_per_installer = [
    #     {"installer": "pip", "num_downloads": "3757739"},
    #     {"installer": "poetry", "num_downloads": "1032345"},
    #     {"installer": "requests", "num_downloads": "254686"},
    #     {"installer": "bandersnatch", "num_downloads": "65166"},
    #     {"installer": None, "num_downloads": "62650"},
    #     {"installer": "uv", "num_downloads": "51423"},
    #     {"installer": "Browser", "num_downloads": "12680"},
    #     {"installer": "Nexus", "num_downloads": "12190"},
    #     {"installer": "pdm", "num_downloads": "8349"},
    #     {"installer": "devpi", "num_downloads": "259"},
    #     {"installer": "conda", "num_downloads": "115"},
    #     {"installer": "OS", "num_downloads": "106"},
    #     {"installer": "setuptools", "num_downloads": "39"},
    #     {"installer": "Artifactory", "num_downloads": "10"},
    # ]

    all_release_events_query = dedent(
        """\
        SELECT
            version AS psr_version,
            DATETIME_TRUNC(DATETIME(upload_time), SECOND) AS release_time,
            filename AS artifact,
        FROM `bigquery-public-data.pypi.distribution_metadata`
        WHERE
            name = 'python-semantic-release'
        AND
            packagetype = 'bdist_wheel'
        ORDER BY release_time DESC
    """
    )

    all_release_events = [
        {
            "psr_version": "9.14.0",
            "release_time": "2024-11-11T08:05:49",
            "artifact": "python_semantic_release-9.14.0-py3-none-any.whl",
        },
        {
            "psr_version": "9.13.0",
            "release_time": "2024-11-10T07:04:59",
            "artifact": "python_semantic_release-9.13.0-py3-none-any.whl",
        },
        {
            "psr_version": "9.12.2",
            "release_time": "2024-11-07T01:29:54",
            "artifact": "python_semantic_release-9.12.2-py3-none-any.whl",
        },
        {
            "psr_version": "9.12.1",
            "release_time": "2024-11-06T04:07:31",
            "artifact": "python_semantic_release-9.12.1-py3-none-any.whl",
        },
        {
            "psr_version": "9.12.0",
            "release_time": "2024-10-18T04:42:10",
            "artifact": "python_semantic_release-9.12.0-py3-none-any.whl",
        },
        {
            "psr_version": "9.11.1",
            "release_time": "2024-10-15T04:48:47",
            "artifact": "python_semantic_release-9.11.1-py3-none-any.whl",
        },
        {
            "psr_version": "9.11.0",
            "release_time": "2024-10-12T23:27:40",
            "artifact": "python_semantic_release-9.11.0-py3-none-any.whl",
        },
        {
            "psr_version": "9.10.1",
            "release_time": "2024-10-10T01:03:23",
            "artifact": "python_semantic_release-9.10.1-py3-none-any.whl",
        },
        {
            "psr_version": "9.10.0",
            "release_time": "2024-10-08T02:47:36",
            "artifact": "python_semantic_release-9.10.0-py3-none-any.whl",
        },
        {
            "psr_version": "9.9.0",
            "release_time": "2024-09-28T06:16:06",
            "artifact": "python_semantic_release-9.9.0-py3-none-any.whl",
        },
        {
            "psr_version": "9.8.9",
            "release_time": "2024-09-27T07:35:21",
            "artifact": "python_semantic_release-9.8.9-py3-none-any.whl",
        },
        {
            "psr_version": "9.8.8",
            "release_time": "2024-09-01T17:43:42",
            "artifact": "python_semantic_release-9.8.8-py3-none-any.whl",
        },
        {
            "psr_version": "9.8.7",
            "release_time": "2024-08-20T04:35:00",
            "artifact": "python_semantic_release-9.8.7-py3-none-any.whl",
        },
        {
            "psr_version": "9.8.6",
            "release_time": "2024-07-20T12:28:51",
            "artifact": "python_semantic_release-9.8.6-py3-none-any.whl",
        },
        {
            "psr_version": "9.8.5",
            "release_time": "2024-07-06T21:20:57",
            "artifact": "python_semantic_release-9.8.5-py3-none-any.whl",
        },
        {
            "psr_version": "9.8.4",
            "release_time": "2024-07-04T16:57:58",
            "artifact": "python_semantic_release-9.8.4-py3-none-any.whl",
        },
        {
            "psr_version": "9.8.3",
            "release_time": "2024-06-18T05:00:40",
            "artifact": "python_semantic_release-9.8.3-py3-none-any.whl",
        },
        {
            "psr_version": "9.8.2",
            "release_time": "2024-06-17T06:12:32",
            "artifact": "python_semantic_release-9.8.2-py3-none-any.whl",
        },
        {
            "psr_version": "9.8.1",
            "release_time": "2024-06-05T00:31:33",
            "artifact": "python_semantic_release-9.8.1-py3-none-any.whl",
        },
        {
            "psr_version": "9.8.0",
            "release_time": "2024-05-27T16:00:35",
            "artifact": "python_semantic_release-9.8.0-py3-none-any.whl",
        },
        {
            "psr_version": "9.7.3",
            "release_time": "2024-05-15T11:46:45",
            "artifact": "python_semantic_release-9.7.3-py3-none-any.whl",
        },
        {
            "psr_version": "9.7.2",
            "release_time": "2024-05-13T03:23:13",
            "artifact": "python_semantic_release-9.7.2-py3-none-any.whl",
        },
        {
            "psr_version": "9.7.1",
            "release_time": "2024-05-07T03:29:15",
            "artifact": "python_semantic_release-9.7.1-py3-none-any.whl",
        },
        {
            "psr_version": "9.7.0",
            "release_time": "2024-05-06T03:00:31",
            "artifact": "python_semantic_release-9.7.0-py3-none-any.whl",
        },
        {
            "psr_version": "9.6.0",
            "release_time": "2024-04-29T04:30:01",
            "artifact": "python_semantic_release-9.6.0-py3-none-any.whl",
        },
        {
            "psr_version": "9.5.0",
            "release_time": "2024-04-23T02:38:50",
            "artifact": "python_semantic_release-9.5.0-py3-none-any.whl",
        },
        {
            "psr_version": "9.4.2",
            "release_time": "2024-04-14T01:45:51",
            "artifact": "python_semantic_release-9.4.2-py3-none-any.whl",
        },
        {
            "psr_version": "9.4.1",
            "release_time": "2024-04-06T19:50:45",
            "artifact": "python_semantic_release-9.4.1-py3-none-any.whl",
        },
        {
            "psr_version": "9.4.0",
            "release_time": "2024-03-31T20:44:08",
            "artifact": "python_semantic_release-9.4.0-py3-none-any.whl",
        },
        {
            "psr_version": "9.3.1",
            "release_time": "2024-03-24T04:10:58",
            "artifact": "python_semantic_release-9.3.1-py3-none-any.whl",
        },
        {
            "psr_version": "9.3.0",
            "release_time": "2024-03-21T04:23:34",
            "artifact": "python_semantic_release-9.3.0-py3-none-any.whl",
        },
        {
            "psr_version": "9.2.2",
            "release_time": "2024-03-19T05:13:06",
            "artifact": "python_semantic_release-9.2.2-py3-none-any.whl",
        },
        {
            "psr_version": "9.2.1",
            "release_time": "2024-03-19T05:00:52",
            "artifact": "python_semantic_release-9.2.1-py3-none-any.whl",
        },
        {
            "psr_version": "9.2.0",
            "release_time": "2024-03-18T15:01:37",
            "artifact": "python_semantic_release-9.2.0-py3-none-any.whl",
        },
        {
            "psr_version": "9.1.1",
            "release_time": "2024-02-25T08:48:47",
            "artifact": "python_semantic_release-9.1.1-py3-none-any.whl",
        },
        {
            "psr_version": "9.1.0",
            "release_time": "2024-02-14T19:50:08",
            "artifact": "python_semantic_release-9.1.0-py3-none-any.whl",
        },
        {
            "psr_version": "9.0.3",
            "release_time": "2024-02-08T09:19:20",
            "artifact": "python_semantic_release-9.0.3-py3-none-any.whl",
        },
        {
            "psr_version": "9.0.2",
            "release_time": "2024-02-08T08:32:19",
            "artifact": "python_semantic_release-9.0.2-py3-none-any.whl",
        },
        {
            "psr_version": "8.7.0",
            "release_time": "2023-12-22T11:57:24",
            "artifact": "python_semantic_release-8.7.0-py3-none-any.whl",
        },
        {
            "psr_version": "8.6.0",
            "release_time": "2023-12-22T11:42:48",
            "artifact": "python_semantic_release-8.6.0-py3-none-any.whl",
        },
        {
            "psr_version": "8.5.2",
            "release_time": "2023-12-19T18:01:35",
            "artifact": "python_semantic_release-8.5.2-py3-none-any.whl",
        },
        {
            "psr_version": "8.5.1",
            "release_time": "2023-12-12T19:53:43",
            "artifact": "python_semantic_release-8.5.1-py3-none-any.whl",
        },
        {
            "psr_version": "8.5.0",
            "release_time": "2023-12-07T20:36:37",
            "artifact": "python_semantic_release-8.5.0-py3-none-any.whl",
        },
        {
            "psr_version": "8.4.0",
            "release_time": "2023-12-07T16:50:16",
            "artifact": "python_semantic_release-8.4.0-py3-none-any.whl",
        },
        {
            "psr_version": "8.3.0",
            "release_time": "2023-10-23T19:05:32",
            "artifact": "python_semantic_release-8.3.0-py3-none-any.whl",
        },
        {
            "psr_version": "8.2.0",
            "release_time": "2023-10-23T16:21:01",
            "artifact": "python_semantic_release-8.2.0-py3-none-any.whl",
        },
        {
            "psr_version": "8.1.2",
            "release_time": "2023-10-13T08:40:21",
            "artifact": "python_semantic_release-8.1.2-py3-none-any.whl",
        },
        {
            "psr_version": "8.1.1",
            "release_time": "2023-09-19T21:10:02",
            "artifact": "python_semantic_release-8.1.1-py3-none-any.whl",
        },
        {
            "psr_version": "8.1.0",
            "release_time": "2023-09-19T20:45:56",
            "artifact": "python_semantic_release-8.1.0-py3-none-any.whl",
        },
        {
            "psr_version": "8.0.8",
            "release_time": "2023-08-26T22:34:14",
            "artifact": "python_semantic_release-8.0.8-py3-none-any.whl",
        },
        {
            "psr_version": "8.0.7",
            "release_time": "2023-08-16T18:58:57",
            "artifact": "python_semantic_release-8.0.7-py3-none-any.whl",
        },
        {
            "psr_version": "8.0.6",
            "release_time": "2023-08-13T21:47:49",
            "artifact": "python_semantic_release-8.0.6-py3-none-any.whl",
        },
        {
            "psr_version": "8.0.5",
            "release_time": "2023-08-10T18:54:14",
            "artifact": "python_semantic_release-8.0.5-py3-none-any.whl",
        },
        {
            "psr_version": "8.0.4",
            "release_time": "2023-07-26T20:44:08",
            "artifact": "python_semantic_release-8.0.4-py3-none-any.whl",
        },
        {
            "psr_version": "8.0.3",
            "release_time": "2023-07-21T16:22:16",
            "artifact": "python_semantic_release-8.0.3-py3-none-any.whl",
        },
        {
            "psr_version": "8.0.2",
            "release_time": "2023-07-18T21:41:26",
            "artifact": "python_semantic_release-8.0.2-py3-none-any.whl",
        },
        {
            "psr_version": "8.0.1",
            "release_time": "2023-07-17T20:05:22",
            "artifact": "python_semantic_release-8.0.1-py3-none-any.whl",
        },
        {
            "psr_version": "8.0.0",
            "release_time": "2023-07-16T13:03:05",
            "artifact": "python_semantic_release-8.0.0-py3-none-any.whl",
        },
        {
            "psr_version": "8.0.0rc4",
            "release_time": "2023-07-09T17:02:11",
            "artifact": "python_semantic_release-8.0.0rc4-py3-none-any.whl",
        },
        {
            "psr_version": "8.0.0rc3",
            "release_time": "2023-07-01T23:24:36",
            "artifact": "python_semantic_release-8.0.0rc3-py3-none-any.whl",
        },
        {
            "psr_version": "8.0.0rc2",
            "release_time": "2023-06-28T08:40:38",
            "artifact": "python_semantic_release-8.0.0rc2-py3-none-any.whl",
        },
        {
            "psr_version": "8.0.0rc1",
            "release_time": "2023-06-17T14:19:34",
            "artifact": "python_semantic_release-8.0.0rc1-py3-none-any.whl",
        },
        {
            "psr_version": "7.34.6",
            "release_time": "2023-06-17T14:12:14",
            "artifact": "python_semantic_release-7.34.6-py3-none-any.whl",
        },
        {
            "psr_version": "7.34.5",
            "release_time": "2023-06-17T14:00:11",
            "artifact": "python_semantic_release-7.34.5-py3-none-any.whl",
        },
        {
            "psr_version": "7.34.4",
            "release_time": "2023-06-15T08:03:32",
            "artifact": "python_semantic_release-7.34.4-py3-none-any.whl",
        },
        {
            "psr_version": "8.0.0a8",
            "release_time": "2023-06-13T17:38:48",
            "artifact": "python_semantic_release-8.0.0a8-py3-none-any.whl",
        },
        {
            "psr_version": "8.0.0a7",
            "release_time": "2023-06-11T19:23:46",
            "artifact": "python_semantic_release-8.0.0a7-py3-none-any.whl",
        },
        {
            "psr_version": "8.0.0a6",
            "release_time": "2023-06-04T17:39:09",
            "artifact": "python_semantic_release-8.0.0a6-py3-none-any.whl",
        },
        {
            "psr_version": "7.34.3",
            "release_time": "2023-06-01T16:44:28",
            "artifact": "python_semantic_release-7.34.3-py3-none-any.whl",
        },
        {
            "psr_version": "7.34.2",
            "release_time": "2023-05-29T16:06:27",
            "artifact": "python_semantic_release-7.34.2-py3-none-any.whl",
        },
        {
            "psr_version": "7.34.1",
            "release_time": "2023-05-28T17:49:00",
            "artifact": "python_semantic_release-7.34.1-py3-none-any.whl",
        },
        {
            "psr_version": "7.34.0",
            "release_time": "2023-05-28T10:24:49",
            "artifact": "python_semantic_release-7.34.0-py3-none-any.whl",
        },
        {
            "psr_version": "7.33.5",
            "release_time": "2023-05-19T07:39:49",
            "artifact": "python_semantic_release-7.33.5-py3-none-any.whl",
        },
        {
            "psr_version": "7.33.4",
            "release_time": "2023-05-14T11:27:26",
            "artifact": "python_semantic_release-7.33.4-py3-none-any.whl",
        },
        {
            "psr_version": "7.33.3",
            "release_time": "2023-04-24T14:22:23",
            "artifact": "python_semantic_release-7.33.3-py3-none-any.whl",
        },
        {
            "psr_version": "8.0.0a5",
            "release_time": "2023-04-17T20:00:18",
            "artifact": "python_semantic_release-8.0.0a5-py3-none-any.whl",
        },
        {
            "psr_version": "8.0.0a4",
            "release_time": "2023-02-27T22:12:30",
            "artifact": "python_semantic_release-8.0.0a4-py3-none-any.whl",
        },
        {
            "psr_version": "7.33.2",
            "release_time": "2023-02-17T19:51:30",
            "artifact": "python_semantic_release-7.33.2-py3-none-any.whl",
        },
        {
            "psr_version": "8.0.0a3",
            "release_time": "2023-02-04T17:13:11",
            "artifact": "python_semantic_release-8.0.0a3-py3-none-any.whl",
        },
        {
            "psr_version": "7.33.1",
            "release_time": "2023-02-01T11:52:29",
            "artifact": "python_semantic_release-7.33.1-py3-none-any.whl",
        },
        {
            "psr_version": "7.33.0",
            "release_time": "2023-01-15T10:41:38",
            "artifact": "python_semantic_release-7.33.0-py3-none-any.whl",
        },
        {
            "psr_version": "7.32.2",
            "release_time": "2022-10-22T17:30:42",
            "artifact": "python_semantic_release-7.32.2-py3-none-any.whl",
        },
        {
            "psr_version": "7.32.1",
            "release_time": "2022-10-07T06:08:29",
            "artifact": "python_semantic_release-7.32.1-py3-none-any.whl",
        },
        {
            "psr_version": "7.32.0",
            "release_time": "2022-09-25T20:25:24",
            "artifact": "python_semantic_release-7.32.0-py3-none-any.whl",
        },
        {
            "psr_version": "7.31.4",
            "release_time": "2022-08-23T22:37:11",
            "artifact": "python_semantic_release-7.31.4-py3-none-any.whl",
        },
        {
            "psr_version": "7.31.3",
            "release_time": "2022-08-22T10:26:36",
            "artifact": "python_semantic_release-7.31.3-py3-none-any.whl",
        },
        {
            "psr_version": "7.31.2",
            "release_time": "2022-07-29T08:02:04",
            "artifact": "python_semantic_release-7.31.2-py3-none-any.whl",
        },
        {
            "psr_version": "7.31.1",
            "release_time": "2022-07-29T06:49:10",
            "artifact": "python_semantic_release-7.31.1-py3-none-any.whl",
        },
        {
            "psr_version": "7.31.0",
            "release_time": "2022-07-29T06:29:40",
            "artifact": "python_semantic_release-7.31.0-py3-none-any.whl",
        },
        {
            "psr_version": "7.30.2",
            "release_time": "2022-07-26T13:34:35",
            "artifact": "python_semantic_release-7.30.2-py3-none-any.whl",
        },
        {
            "psr_version": "7.30.1",
            "release_time": "2022-07-25T16:11:38",
            "artifact": "python_semantic_release-7.30.1-py3-none-any.whl",
        },
        {
            "psr_version": "7.30.0",
            "release_time": "2022-07-25T13:14:25",
            "artifact": "python_semantic_release-7.30.0-py3-none-any.whl",
        },
        {
            "psr_version": "7.29.7",
            "release_time": "2022-07-24T15:43:40",
            "artifact": "python_semantic_release-7.29.7-py3-none-any.whl",
        },
        {
            "psr_version": "7.29.6",
            "release_time": "2022-07-15T18:38:19",
            "artifact": "python_semantic_release-7.29.6-py3-none-any.whl",
        },
        {
            "psr_version": "7.29.5",
            "release_time": "2022-07-14T11:35:01",
            "artifact": "python_semantic_release-7.29.5-py3-none-any.whl",
        },
        {
            "psr_version": "7.29.4",
            "release_time": "2022-06-29T11:07:30",
            "artifact": "python_semantic_release-7.29.4-py3-none-any.whl",
        },
        {
            "psr_version": "7.29.3",
            "release_time": "2022-06-26T09:43:08",
            "artifact": "python_semantic_release-7.29.3-py3-none-any.whl",
        },
        {
            "psr_version": "7.29.2",
            "release_time": "2022-06-20T10:41:32",
            "artifact": "python_semantic_release-7.29.2-py3-none-any.whl",
        },
        {
            "psr_version": "7.29.1",
            "release_time": "2022-06-01T11:46:45",
            "artifact": "python_semantic_release-7.29.1-py3-none-any.whl",
        },
        {
            "psr_version": "7.29.0",
            "release_time": "2022-05-27T10:25:43",
            "artifact": "python_semantic_release-7.29.0-py3-none-any.whl",
        },
        {
            "psr_version": "7.28.1",
            "release_time": "2022-04-14T10:51:57",
            "artifact": "python_semantic_release-7.28.1-py3-none-any.whl",
        },
        {
            "psr_version": "7.28.0",
            "release_time": "2022-04-11T09:20:38",
            "artifact": "python_semantic_release-7.28.0-py3-none-any.whl",
        },
        {
            "psr_version": "7.27.1",
            "release_time": "2022-04-03T11:33:18",
            "artifact": "python_semantic_release-7.27.1-py3-none-any.whl",
        },
        {
            "psr_version": "7.27.0",
            "release_time": "2022-03-15T18:16:19",
            "artifact": "python_semantic_release-7.27.0-py3-none-any.whl",
        },
        {
            "psr_version": "7.26.0",
            "release_time": "2022-03-07T19:48:01",
            "artifact": "python_semantic_release-7.26.0-py3-none-any.whl",
        },
        {
            "psr_version": "7.25.2",
            "release_time": "2022-02-24T16:19:06",
            "artifact": "python_semantic_release-7.25.2-py3-none-any.whl",
        },
        {
            "psr_version": "7.25.1",
            "release_time": "2022-02-23T15:50:33",
            "artifact": "python_semantic_release-7.25.1-py3-none-any.whl",
        },
        {
            "psr_version": "7.25.0",
            "release_time": "2022-02-17T17:12:34",
            "artifact": "python_semantic_release-7.25.0-py3-none-any.whl",
        },
        {
            "psr_version": "7.24.0",
            "release_time": "2022-01-24T15:58:58",
            "artifact": "python_semantic_release-7.24.0-py3-none-any.whl",
        },
        {
            "psr_version": "7.23.0",
            "release_time": "2021-11-30T07:22:21",
            "artifact": "python_semantic_release-7.23.0-py3-none-any.whl",
        },
        {
            "psr_version": "7.22.0",
            "release_time": "2021-11-21T19:29:21",
            "artifact": "python_semantic_release-7.22.0-py3-none-any.whl",
        },
        {
            "psr_version": "7.21.0",
            "release_time": "2021-11-21T19:11:44",
            "artifact": "python_semantic_release-7.21.0-py3-none-any.whl",
        },
        {
            "psr_version": "7.20.0",
            "release_time": "2021-11-21T19:05:11",
            "artifact": "python_semantic_release-7.20.0-py3-none-any.whl",
        },
        {
            "psr_version": "7.19.2",
            "release_time": "2021-09-04T11:36:30",
            "artifact": "python_semantic_release-7.19.2-py3-none-any.whl",
        },
        {
            "psr_version": "7.19.1",
            "release_time": "2021-08-17T06:04:15",
            "artifact": "python_semantic_release-7.19.1-py3-none-any.whl",
        },
        {
            "psr_version": "7.19.0",
            "release_time": "2021-08-16T11:02:04",
            "artifact": "python_semantic_release-7.19.0-py3-none-any.whl",
        },
        {
            "psr_version": "7.18.0",
            "release_time": "2021-08-09T20:29:33",
            "artifact": "python_semantic_release-7.18.0-py3-none-any.whl",
        },
        {
            "psr_version": "7.17.0",
            "release_time": "2021-08-07T17:31:14",
            "artifact": "python_semantic_release-7.17.0-py3-none-any.whl",
        },
        {
            "psr_version": "7.16.4",
            "release_time": "2021-08-03T13:58:39",
            "artifact": "python_semantic_release-7.16.4-py3-none-any.whl",
        },
        {
            "psr_version": "7.16.3",
            "release_time": "2021-07-29T12:56:42",
            "artifact": "python_semantic_release-7.16.3-py3-none-any.whl",
        },
        {
            "psr_version": "7.16.2",
            "release_time": "2021-06-25T15:38:31",
            "artifact": "python_semantic_release-7.16.2-py3-none-any.whl",
        },
        {
            "psr_version": "7.16.1",
            "release_time": "2021-06-08T17:14:22",
            "artifact": "python_semantic_release-7.16.1-py3-none-any.whl",
        },
        {
            "psr_version": "7.16.0",
            "release_time": "2021-06-08T15:59:53",
            "artifact": "python_semantic_release-7.16.0-py3-none-any.whl",
        },
        {
            "psr_version": "7.15.6",
            "release_time": "2021-06-08T15:57:00",
            "artifact": "python_semantic_release-7.15.6-py3-none-any.whl",
        },
        {
            "psr_version": "7.15.5",
            "release_time": "2021-05-26T09:21:24",
            "artifact": "python_semantic_release-7.15.5-py3-none-any.whl",
        },
        {
            "psr_version": "7.15.4",
            "release_time": "2021-04-29T07:06:42",
            "artifact": "python_semantic_release-7.15.4-py3-none-any.whl",
        },
        {
            "psr_version": "7.15.3",
            "release_time": "2021-04-03T08:28:13",
            "artifact": "python_semantic_release-7.15.3-py3-none-any.whl",
        },
        {
            "psr_version": "7.15.1",
            "release_time": "2021-03-26T13:05:05",
            "artifact": "python_semantic_release-7.15.1-py3-none-any.whl",
        },
        {
            "psr_version": "7.15.0",
            "release_time": "2021-02-18T13:46:28",
            "artifact": "python_semantic_release-7.15.0-py3-none-any.whl",
        },
        {
            "psr_version": "7.14.0",
            "release_time": "2021-02-11T18:23:37",
            "artifact": "python_semantic_release-7.14.0-py3-none-any.whl",
        },
        {
            "psr_version": "7.13.2",
            "release_time": "2021-01-29T11:28:31",
            "artifact": "python_semantic_release-7.13.2-py3-none-any.whl",
        },
        {
            "psr_version": "7.13.1",
            "release_time": "2021-01-26T12:35:23",
            "artifact": "python_semantic_release-7.13.1-py3-none-any.whl",
        },
        {
            "psr_version": "7.13.0",
            "release_time": "2021-01-26T12:29:23",
            "artifact": "python_semantic_release-7.13.0-py3-none-any.whl",
        },
        {
            "psr_version": "7.12.0",
            "release_time": "2021-01-25T17:10:51",
            "artifact": "python_semantic_release-7.12.0-py3-none-any.whl",
        },
        {
            "psr_version": "7.11.0",
            "release_time": "2021-01-08T11:05:22",
            "artifact": "python_semantic_release-7.11.0-py3-none-any.whl",
        },
        {
            "psr_version": "7.10.0",
            "release_time": "2021-01-08T07:46:00",
            "artifact": "python_semantic_release-7.10.0-py3-none-any.whl",
        },
        {
            "psr_version": "7.9.0",
            "release_time": "2020-12-21T11:26:17",
            "artifact": "python_semantic_release-7.9.0-py3-none-any.whl",
        },
        {
            "psr_version": "7.8.2",
            "release_time": "2020-12-19T10:43:03",
            "artifact": "python_semantic_release-7.8.2-py3-none-any.whl",
        },
        {
            "psr_version": "7.8.1",
            "release_time": "2020-12-18T13:55:30",
            "artifact": "python_semantic_release-7.8.1-py3-none-any.whl",
        },
        {
            "psr_version": "7.8.0",
            "release_time": "2020-12-18T10:37:06",
            "artifact": "python_semantic_release-7.8.0-py3-none-any.whl",
        },
        {
            "psr_version": "7.7.0",
            "release_time": "2020-12-12T12:17:55",
            "artifact": "python_semantic_release-7.7.0-py3-none-any.whl",
        },
        {
            "psr_version": "7.6.0",
            "release_time": "2020-12-06T19:18:11",
            "artifact": "python_semantic_release-7.6.0-py3-none-any.whl",
        },
        {
            "psr_version": "7.5.0",
            "release_time": "2020-12-04T17:37:52",
            "artifact": "python_semantic_release-7.5.0-py3-none-any.whl",
        },
        {
            "psr_version": "7.4.1",
            "release_time": "2020-12-04T16:46:57",
            "artifact": "python_semantic_release-7.4.1-py3-none-any.whl",
        },
        {
            "psr_version": "7.4.0",
            "release_time": "2020-11-24T18:38:34",
            "artifact": "python_semantic_release-7.4.0-py3-none-any.whl",
        },
        {
            "psr_version": "7.3.0",
            "release_time": "2020-09-28T06:16:23",
            "artifact": "python_semantic_release-7.3.0-py3-none-any.whl",
        },
        {
            "psr_version": "7.2.5",
            "release_time": "2020-09-16T18:33:58",
            "artifact": "python_semantic_release-7.2.5-py3-none-any.whl",
        },
        {
            "psr_version": "7.2.4",
            "release_time": "2020-09-14T18:56:53",
            "artifact": "python_semantic_release-7.2.4-py3-none-any.whl",
        },
        {
            "psr_version": "7.2.3",
            "release_time": "2020-09-12T07:03:56",
            "artifact": "python_semantic_release-7.2.3-py3-none-any.whl",
        },
        {
            "psr_version": "7.2.2",
            "release_time": "2020-07-26T12:48:25",
            "artifact": "python_semantic_release-7.2.2-py3-none-any.whl",
        },
        {
            "psr_version": "7.2.1",
            "release_time": "2020-06-29T17:13:56",
            "artifact": "python_semantic_release-7.2.1-py3-none-any.whl",
        },
        {
            "psr_version": "7.2.0",
            "release_time": "2020-06-15T15:34:43",
            "artifact": "python_semantic_release-7.2.0-py3-none-any.whl",
        },
        {
            "psr_version": "7.1.1",
            "release_time": "2020-05-28T10:04:53",
            "artifact": "python_semantic_release-7.1.1-py3-none-any.whl",
        },
        {
            "psr_version": "7.1.0",
            "release_time": "2020-05-24T08:27:06",
            "artifact": "python_semantic_release-7.1.0-py3-none-any.whl",
        },
        {
            "psr_version": "7.0.0",
            "release_time": "2020-05-22T08:31:51",
            "artifact": "python_semantic_release-7.0.0-py3-none-any.whl",
        },
        {
            "psr_version": "6.4.1",
            "release_time": "2020-05-15T17:00:57",
            "artifact": "python_semantic_release-6.4.1-py3-none-any.whl",
        },
        {
            "psr_version": "6.4.0",
            "release_time": "2020-05-15T15:43:09",
            "artifact": "python_semantic_release-6.4.0-py3-none-any.whl",
        },
        {
            "psr_version": "6.4.0",
            "release_time": "2020-05-15T15:43:09",
            "artifact": "python_semantic_release-6.4.0-py3-none-any.whl",
        },
        {
            "psr_version": "6.3.1",
            "release_time": "2020-05-11T19:01:35",
            "artifact": "python_semantic_release-6.3.1-py3-none-any.whl",
        },
        {
            "psr_version": "6.3.0",
            "release_time": "2020-05-09T11:16:25",
            "artifact": "python_semantic_release-6.3.0-py3-none-any.whl",
        },
        {
            "psr_version": "6.2.0",
            "release_time": "2020-05-02T14:08:36",
            "artifact": "python_semantic_release-6.2.0-py3-none-any.whl",
        },
        {
            "psr_version": "6.1.0",
            "release_time": "2020-04-26T19:48:52",
            "artifact": "python_semantic_release-6.1.0-py3-none-any.whl",
        },
        {
            "psr_version": "6.0.1",
            "release_time": "2020-04-15T19:10:19",
            "artifact": "python_semantic_release-6.0.1-py3-none-any.whl",
        },
        {
            "psr_version": "6.0.0",
            "release_time": "2020-04-15T19:02:33",
            "artifact": "python_semantic_release-6.0.0-py3-none-any.whl",
        },
        {
            "psr_version": "5.2.0",
            "release_time": "2020-04-09T17:25:30",
            "artifact": "python_semantic_release-5.2.0-py3-none-any.whl",
        },
        {
            "psr_version": "5.1.0",
            "release_time": "2020-04-04T14:10:05",
            "artifact": "python_semantic_release-5.1.0-py3-none-any.whl",
        },
        {
            "psr_version": "5.0.2",
            "release_time": "2020-03-22T15:16:02",
            "artifact": "python_semantic_release-5.0.2-py3-none-any.whl",
        },
        {
            "psr_version": "5.0.1",
            "release_time": "2020-03-22T15:03:55",
            "artifact": "python_semantic_release-5.0.1-py3-none-any.whl",
        },
        {
            "psr_version": "5.0.0",
            "release_time": "2020-03-22T14:45:41",
            "artifact": "python_semantic_release-5.0.0-py3-none-any.whl",
        },
        {
            "psr_version": "4.12.0",
            "release_time": "2020-03-22T14:41:01",
            "artifact": "python_semantic_release-4.12.0-py3-none-any.whl",
        },
        {
            "psr_version": "4.12.1",
            "release_time": "2020-03-22T14:37:54",
            "artifact": "python_semantic_release-4.12.1-py3-none-any.whl",
        },
        {
            "psr_version": "4.11.0",
            "release_time": "2020-03-22T14:22:53",
            "artifact": "python_semantic_release-4.11.0-py3-none-any.whl",
        },
        {
            "psr_version": "4.10.0",
            "release_time": "2020-03-03T12:53:40",
            "artifact": "python_semantic_release-4.10.0-py3-none-any.whl",
        },
        {
            "psr_version": "4.9.0",
            "release_time": "2020-03-02T07:53:27",
            "artifact": "python_semantic_release-4.9.0-py3-none-any.whl",
        },
        {
            "psr_version": "4.8.0",
            "release_time": "2020-02-28T22:38:17",
            "artifact": "python_semantic_release-4.8.0-py3-none-any.whl",
        },
        {
            "psr_version": "4.7.1",
            "release_time": "2020-02-28T22:36:20",
            "artifact": "python_semantic_release-4.7.1-py3-none-any.whl",
        },
        {
            "psr_version": "4.7.1",
            "release_time": "2020-02-28T22:36:20",
            "artifact": "python_semantic_release-4.7.1-py3-none-any.whl",
        },
        {
            "psr_version": "4.7.0",
            "release_time": "2020-02-28T08:29:04",
            "artifact": "python_semantic_release-4.7.0-py3-none-any.whl",
        },
        {
            "psr_version": "4.6.0",
            "release_time": "2020-02-19T18:44:11",
            "artifact": "python_semantic_release-4.6.0-py3-none-any.whl",
        },
        {
            "psr_version": "4.5.1",
            "release_time": "2020-02-16T20:01:13",
            "artifact": "python_semantic_release-4.5.1-py3-none-any.whl",
        },
        {
            "psr_version": "4.5.1",
            "release_time": "2020-02-16T20:01:13",
            "artifact": "python_semantic_release-4.5.1-py3-none-any.whl",
        },
        {
            "psr_version": "4.5.1",
            "release_time": "2020-02-16T20:01:13",
            "artifact": "python_semantic_release-4.5.1-py3-none-any.whl",
        },
        {
            "psr_version": "4.5.0",
            "release_time": "2020-02-08T17:28:54",
            "artifact": "python_semantic_release-4.5.0-py3-none-any.whl",
        },
        {
            "psr_version": "4.4.0",
            "release_time": "2020-01-17T07:16:30",
            "artifact": "python_semantic_release-4.4.0-py3-none-any.whl",
        },
        {
            "psr_version": "4.4.0",
            "release_time": "2020-01-17T07:16:30",
            "artifact": "python_semantic_release-4.4.0-py3-none-any.whl",
        },
        {
            "psr_version": "4.4.0",
            "release_time": "2020-01-17T07:16:30",
            "artifact": "python_semantic_release-4.4.0-py3-none-any.whl",
        },
        {
            "psr_version": "4.3.4",
            "release_time": "2019-12-17T15:01:25",
            "artifact": "python_semantic_release-4.3.4-py3-none-any.whl",
        },
        {
            "psr_version": "4.3.3",
            "release_time": "2019-11-06T07:54:02",
            "artifact": "python_semantic_release-4.3.3-py3-none-any.whl",
        },
        {
            "psr_version": "4.3.2",
            "release_time": "2019-10-05T12:57:12",
            "artifact": "python_semantic_release-4.3.2-py3-none-any.whl",
        },
        {
            "psr_version": "4.3.1",
            "release_time": "2019-09-29T17:21:05",
            "artifact": "python_semantic_release-4.3.1-py3-none-any.whl",
        },
        {
            "psr_version": "4.3.0",
            "release_time": "2019-09-06T12:17:17",
            "artifact": "python_semantic_release-4.3.0-py3-none-any.whl",
        },
        {
            "psr_version": "4.2.0",
            "release_time": "2019-08-05T07:14:21",
            "artifact": "python_semantic_release-4.2.0-py3-none-any.whl",
        },
        {
            "psr_version": "4.1.2",
            "release_time": "2019-08-04T13:33:31",
            "artifact": "python_semantic_release-4.1.2-py3-none-any.whl",
        },
        {
            "psr_version": "4.1.1",
            "release_time": "2019-02-15T12:41:53",
            "artifact": "python_semantic_release-4.1.1-py3-none-any.whl",
        },
        {
            "psr_version": "4.1.0",
            "release_time": "2019-01-31T17:34:45",
            "artifact": "python_semantic_release-4.1.0-py3-none-any.whl",
        },
        {
            "psr_version": "4.0.2",
            "release_time": "2019-01-26T10:06:32",
            "artifact": "python_semantic_release-4.0.2-py3-none-any.whl",
        },
        {
            "psr_version": "4.0.1",
            "release_time": "2019-01-12T21:33:14",
            "artifact": "python_semantic_release-4.0.1-py3-none-any.whl",
        },
        {
            "psr_version": "4.0.0",
            "release_time": "2018-11-22T19:34:05",
            "artifact": "python_semantic_release-4.0.0-py3-none-any.whl",
        },
        {
            "psr_version": "3.11.2",
            "release_time": "2018-11-22T19:31:22",
            "artifact": "python_semantic_release-3.11.2-py3-none-any.whl",
        },
        {
            "psr_version": "3.11.2",
            "release_time": "2018-06-10T09:31:41",
            "artifact": "python_semantic_release-3.11.2-py2.py3-none-any.whl",
        },
        {
            "psr_version": "3.11.1",
            "release_time": "2018-06-06T20:42:31",
            "artifact": "python_semantic_release-3.11.1-py2.py3-none-any.whl",
        },
        {
            "psr_version": "3.11.0",
            "release_time": "2018-04-12T18:37:48",
            "artifact": "python_semantic_release-3.11.0-py2.py3-none-any.whl",
        },
        {
            "psr_version": "3.10.3",
            "release_time": "2018-01-29T13:01:44",
            "artifact": "python_semantic_release-3.10.3-py2.py3-none-any.whl",
        },
        {
            "psr_version": "3.10.2",
            "release_time": "2017-08-03T19:39:57",
            "artifact": "python_semantic_release-3.10.2-py2.py3-none-any.whl",
        },
        {
            "psr_version": "3.10.1",
            "release_time": "2017-07-22T18:43:06",
            "artifact": "python_semantic_release-3.10.1-py2.py3-none-any.whl",
        },
        {
            "psr_version": "3.10.0",
            "release_time": "2017-05-05T19:22:21",
            "artifact": "python_semantic_release-3.10.0-py2.py3-none-any.whl",
        },
        {
            "psr_version": "3.9.0",
            "release_time": "2016-07-03T09:43:40",
            "artifact": "python_semantic_release-3.9.0-py2.py3-none-any.whl",
        },
        {
            "psr_version": "3.8.1",
            "release_time": "2016-04-21T15:14:19",
            "artifact": "python_semantic_release-3.8.1-py2.py3-none-any.whl",
        },
        {
            "psr_version": "3.7.1",
            "release_time": "2016-03-15T07:40:29",
            "artifact": "python_semantic_release-3.7.1-py2.py3-none-any.whl",
        },
        {
            "psr_version": "3.6.0",
            "release_time": "2015-12-28T17:22:54",
            "artifact": "python_semantic_release-3.6.0-py2.py3-none-any.whl",
        },
        {
            "psr_version": "3.5.0",
            "release_time": "2015-12-22T21:12:20",
            "artifact": "python_semantic_release-3.5.0-py2.py3-none-any.whl",
        },
        {
            "psr_version": "3.4.0",
            "release_time": "2015-12-22T06:37:36",
            "artifact": "python_semantic_release-3.4.0-py2.py3-none-any.whl",
        },
        {
            "psr_version": "3.3.3",
            "release_time": "2015-12-21T15:05:55",
            "artifact": "python_semantic_release-3.3.3-py2.py3-none-any.whl",
        },
        {
            "psr_version": "3.3.3",
            "release_time": "2015-12-21T15:05:55",
            "artifact": "python_semantic_release-3.3.3-py2.py3-none-any.whl",
        },
        {
            "psr_version": "3.3.3",
            "release_time": "2015-12-21T15:05:55",
            "artifact": "python_semantic_release-3.3.3-py2.py3-none-any.whl",
        },
        {
            "psr_version": "3.3.2",
            "release_time": "2015-12-21T14:37:10",
            "artifact": "python_semantic_release-3.3.2-py2.py3-none-any.whl",
        },
        {
            "psr_version": "3.3.1",
            "release_time": "2015-12-21T06:50:56",
            "artifact": "python_semantic_release-3.3.1-py2.py3-none-any.whl",
        },
        {
            "psr_version": "3.3.0",
            "release_time": "2015-12-20T21:43:51",
            "artifact": "python_semantic_release-3.3.0-py2.py3-none-any.whl",
        },
        {
            "psr_version": "3.1.0",
            "release_time": "2015-08-31T18:00:39",
            "artifact": "python_semantic_release-3.1.0-py2.py3-none-any.whl",
        },
        {
            "psr_version": "3.0.0",
            "release_time": "2015-08-25T19:30:23",
            "artifact": "python_semantic_release-3.0.0-py2.py3-none-any.whl",
        },
        {
            "psr_version": "2.1.4",
            "release_time": "2015-08-23T22:30:20",
            "artifact": "python_semantic_release-2.1.4-py2.py3-none-any.whl",
        },
        {
            "psr_version": "2.1.3",
            "release_time": "2015-08-22T08:00:34",
            "artifact": "python_semantic_release-2.1.3-py2.py3-none-any.whl",
        },
        {
            "psr_version": "2.1.2",
            "release_time": "2015-08-20T06:17:02",
            "artifact": "python_semantic_release-2.1.2-py2.py3-none-any.whl",
        },
        {
            "psr_version": "2.1.1",
            "release_time": "2015-08-20T06:08:25",
            "artifact": "python_semantic_release-2.1.1-py2.py3-none-any.whl",
        },
        {
            "psr_version": "2.1.0",
            "release_time": "2015-08-19T22:24:23",
            "artifact": "python_semantic_release-2.1.0-py2.py3-none-any.whl",
        },
        {
            "psr_version": "2.0.0",
            "release_time": "2015-08-19T20:57:04",
            "artifact": "python_semantic_release-2.0.0-py2.py3-none-any.whl",
        },
        {
            "psr_version": "1.0.0",
            "release_time": "2015-08-04T08:30:18",
            "artifact": "python_semantic_release-1.0.0-py2.py3-none-any.whl",
        },
        {
            "psr_version": "0.9.1",
            "release_time": "2015-08-04T06:50:18",
            "artifact": "python_semantic_release-0.9.1-py2.py3-none-any.whl",
        },
        {
            "psr_version": "0.9.0",
            "release_time": "2015-08-03T21:08:25",
            "artifact": "python_semantic_release-0.9.0-py2.py3-none-any.whl",
        },
        {
            "psr_version": "0.8.0",
            "release_time": "2015-08-03T12:00:30",
            "artifact": "python_semantic_release-0.8.0-py3-none-any.whl",
        },
        {
            "psr_version": "0.7.0",
            "release_time": "2015-08-02T19:17:16",
            "artifact": "python_semantic_release-0.7.0-py3-none-any.whl",
        },
        {
            "psr_version": "0.6.0",
            "release_time": "2015-08-02T04:56:12",
            "artifact": "python_semantic_release-0.6.0-py3-none-any.whl",
        },
        {
            "psr_version": "0.5.4",
            "release_time": "2015-07-29T08:43:58",
            "artifact": "python_semantic_release-0.5.4-py3-none-any.whl",
        },
        {
            "psr_version": "0.5.3",
            "release_time": "2015-07-28T19:02:20",
            "artifact": "python_semantic_release-0.5.3-py3-none-any.whl",
        },
        {
            "psr_version": "0.5.2",
            "release_time": "2015-07-28T16:32:00",
            "artifact": "python_semantic_release-0.5.2-py3-none-any.whl",
        },
        {
            "psr_version": "0.5.1",
            "release_time": "2015-07-28T16:25:24",
            "artifact": "python_semantic_release-0.5.1-py3-none-any.whl",
        },
        {
            "psr_version": "0.5.1",
            "release_time": "2015-07-28T16:25:24",
            "artifact": "python_semantic_release-0.5.1-py3-none-any.whl",
        },
        {
            "psr_version": "0.5.0",
            "release_time": "2015-07-28T16:08:31",
            "artifact": "python_semantic_release-0.5.0-py3-none-any.whl",
        },
        {
            "psr_version": "0.4.0",
            "release_time": "2015-07-28T09:44:43",
            "artifact": "python_semantic_release-0.4.0-py3-none-any.whl",
        },
        {
            "psr_version": "0.4.0",
            "release_time": "2015-07-28T09:44:43",
            "artifact": "python_semantic_release-0.4.0-py3-none-any.whl",
        },
        {
            "psr_version": "0.3.2",
            "release_time": "2015-07-28T08:13:27",
            "artifact": "python_semantic_release-0.3.2-py3-none-any.whl",
        },
        {
            "psr_version": "0.3.1",
            "release_time": "2015-07-27T22:15:32",
            "artifact": "python_semantic_release-0.3.1-py3-none-any.whl",
        },
    ]
