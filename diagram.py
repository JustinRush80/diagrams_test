from diagrams import Diagram
from diagrams.aws.compute import Lambda
from diagrams.aws.database import RDS
from diagrams.programming.language import Python
from diagrams.onprem.compute import Server


with Diagram("pic/ICPS ETL", show=False, outformat="svg"):
    Server("ICPS") >> Server("ODS") >> Python() >> RDS("ods_dev")

