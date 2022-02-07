from diagrams import Diagram,Cluster
from diagrams.aws.database import RDS
from diagrams.programming.language import Python
from diagrams.onprem.compute import Server
from diagrams.generic.storage import Storage
from diagrams.onprem.ci import GitlabCI
from diagrams.onprem.analytics import Tableau
from diagrams.onprem.client import Users




with Diagram(name="ICPS Scenario Evaluation", filename= "pic/icps_etl", show=True):
    graph_attrs = {
        "shape": "box",
        "style": "dashed",
        "labeljust": "l",
        "pencolor": "#AEB6BE",
        "fontname": "Times-Roman",
        "fontsize": "14",
    }
    
 
    with Cluster("Check and transfer new files every minute",graph_attr=graph_attrs):
        with Cluster("Direct access only for planners") as c:
            icps =  Storage("ICPS")
            Users("Planners") >> icps
        server = Server("sxnda82724")
        icps >> server
        
        
        with Cluster("new files triggers script", graph_attr=graph_attrs):
            script = Python()
            server >> script
                

    server >> RDS("Back up Files")
    script >> Tableau()
    

